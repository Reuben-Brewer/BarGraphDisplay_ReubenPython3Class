# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision B, 08/31/2024

Verified working on: Python 3.8 for Windows 10 64-bit (no Ubuntu, Raspberry Pi, or Mac testing yet).
'''

__author__ = 'reuben.brewer'

#################################################
import os
import sys
import platform
import time
import datetime
import math
import collections
import inspect #To enable 'TellWhichFileWereIn'
import traceback
#################################################

#################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
#################################################

#################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#################################################

class BarGraphDisplay_ReubenPython3Class(Frame): #Subclass the Tkinter Frame

    ##########################################################################################################
    ##########################################################################################################
    def __init__(self, setup_dict): #Subclass the Tkinter Frame

        print("#################### BarGraphDisplay_ReubenPython3Class __init__ starting. ####################")

        #########################################################
        #########################################################
        self.GUI_ready_to_be_updated_flag = 0
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = -1

        #################################################
        self.TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150) #RGB
        self.TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150) #RGB
        self.TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
        self.TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
        self.TKinter_WhiteColor = '#%02x%02x%02x' % (255, 255, 255)  # RGB
        #################################################

        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if platform.system() == "Linux":

            if "raspberrypi" in platform.uname(): #os.uname() doesn't work in windows
                self.my_platform = "pi"
            else:
                self.my_platform = "linux"

        elif platform.system() == "Windows":
            self.my_platform = "windows"

        elif platform.system() == "Darwin":
            self.my_platform = "mac"

        else:
            self.my_platform = "other"

        print("BarGraphDisplay_ReubenPython3Class __init__: The OS platform is: " + self.my_platform)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "GUIparametersDict" in setup_dict:
            self.GUIparametersDict = setup_dict["GUIparametersDict"]

            ##########################################
            if "root" in self.GUIparametersDict:
                self.root = self.GUIparametersDict["root"]
            else:
                print("BarGraphDisplay_ReubenPython3Class __init__: ERROR, must pass in 'root'")
                return
            ##########################################

            ##########################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("BarGraphDisplay_ReubenPython3Class __init__: GUI_ROW: " + str(self.GUI_ROW))
            ##########################################

            ##########################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("BarGraphDisplay_ReubenPython3Class __init__: GUI_COLUMN: " + str(self.GUI_COLUMN))
            ##########################################

            ##########################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("BarGraphDisplay_ReubenPython3Class __init__: GUI_PADX: " + str(self.GUI_PADX))
            ##########################################

            ##########################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("BarGraphDisplay_ReubenPython3Class __init__: GUI_PADY: " + str(self.GUI_PADY))
            ##########################################

            ##########################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 1.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("BarGraphDisplay_ReubenPython3Class __init__: GUI_ROWSPAN: " + str(self.GUI_ROWSPAN))
            ##########################################

            ##########################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 1.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("BarGraphDisplay_ReubenPython3Class __init__: GUI_COLUMNSPAN: " + str(self.GUI_COLUMNSPAN))
            ##########################################

            ##########################################
            if "GUI_STICKY" in self.GUIparametersDict:
                self.GUI_STICKY = str(self.GUIparametersDict["GUI_STICKY"])
            else:
                self.GUI_STICKY = "w"

            print("BarGraphDisplay_ReubenPython3Class __init__: GUI_STICKY: " + str(self.GUI_STICKY))
            ##########################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("BarGraphDisplay_ReubenPython3Class __init__: No GUIparametersDict present, setting USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))

        #print("GUIparametersDict = " + str(self.GUIparametersDict))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Canvas_Width" in setup_dict:
            self.Canvas_Width = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Canvas_Width", setup_dict["Canvas_Width"], 100.0, 1000.0))
        else:
            self.Canvas_Width = 250

        print("BarGraphDisplay_ReubenPython3Class __init__: Canvas_Width: " + str(self.Canvas_Width))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "Canvas_Height" in setup_dict:
            self.Canvas_Height = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Canvas_Height", setup_dict["Canvas_Height"], 100.0, 1000.0))
        else:
            self.Canvas_Height = 150

        print("BarGraphDisplay_ReubenPython3Class __init__: Canvas_Height: " + str(self.Canvas_Height))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "BarWidth" in setup_dict:
            self.BarWidth = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("BarWidth", setup_dict["BarWidth"], 10.0, 500.0))
        else:
            self.BarWidth = 10

        print("BarGraphDisplay_ReubenPython3Class __init__: BarWidth: " + str(self.BarWidth))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "BarPadX" in setup_dict:
            self.BarPadX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("BarPadX", setup_dict["BarPadX"], 1.0, 100.0))
        else:
            self.BarPadX = 1

        print("BarGraphDisplay_ReubenPython3Class __init__: BarPadX: " + str(self.BarPadX))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "FontSize" in setup_dict:
            self.FontSize = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("FontSize", setup_dict["FontSize"], 8.0, 48.0))
        else:
            self.FontSize = 8

        print("BarGraphDisplay_ReubenPython3Class __init__: FontSize: " + str(self.FontSize))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "PositiveColor" in setup_dict:
            self.PositiveColor = setup_dict["PositiveColor"]
        else:
            self.PositiveColor = self.TKinter_LightGreenColor

        print("BarGraphDisplay_ReubenPython3Class __init__: PositiveColor: " + str(self.PositiveColor))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "NegativeColor" in setup_dict:
            self.NegativeColor = setup_dict["NegativeColor"]
        else:
            self.NegativeColor = self.TKinter_LightRedColor

        print("BarGraphDisplay_ReubenPython3Class __init__: NegativeColor: " + str(self.NegativeColor))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        try:
            self.Variables_DictOfDicts = dict()

            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            if "Variables_ListOfDicts" in setup_dict:
                Variables_ListOfDicts_TEMP = setup_dict["Variables_ListOfDicts"]

                #########################################################
                #########################################################
                #########################################################
                #########################################################
                #########################################################
                #########################################################
                if self.IsInputList(Variables_ListOfDicts_TEMP) == 1:

                    #########################################################
                    #########################################################
                    #########################################################
                    #########################################################
                    #########################################################
                    for Variable_Index, Variable_Dict in enumerate(Variables_ListOfDicts_TEMP):

                        #########################################################
                        #########################################################
                        #########################################################
                        #########################################################

                        #############################
                        if "Name" in Variable_Dict:
                            Variable_name = Variable_Dict["Name"]
                        else:
                            print("BarGraphDisplay_ReubenPython2and3Class  __init__ ERROR: Must include 'name' for each variable.")
                            return
                        #############################

                        #############################
                        if "MinValue" in Variable_Dict:
                            Variable_MinValue =  self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", MinValue", Variable_Dict["MinValue"], -sys.float_info.max, sys.float_info.max)
                        else:
                            Variable_MinValue = -sys.float_info.max
                        #############################

                        #############################
                        if "MaxValue" in Variable_Dict:
                            Variable_MaxValue =  self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", MaxValue", Variable_Dict["MaxValue"], -sys.float_info.max, sys.float_info.max)
                        else:
                            Variable_MaxValue = sys.float_info.max
                        #############################

                        #############################
                        if "StartingValue" in Variable_Dict:
                            Variable_StartingValue_validated = self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", StartingValue", Variable_Dict["StartingValue"], Variable_MinValue, Variable_MaxValue)
                        else:
                            Variable_StartingValue_validated = 0.0
                        #############################

                        ############################# can over-ride the global setting
                        if "NegativeColor" in Variable_Dict:
                            Variable_NegativeColor = Variable_Dict["NegativeColor"]
                        else:
                            Variable_NegativeColor = self.NegativeColor
                        #############################

                        ############################# can over-ride the global setting
                        if "PositiveColor" in Variable_Dict:
                            Variable_PositiveColor = Variable_Dict["PositiveColor"]
                        else:
                            Variable_PositiveColor = self.PositiveColor
                        #############################

                        ############################# can over-ride the global setting
                        if "FontSize" in Variable_Dict:
                            Variable_FontSize = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", FontSize", Variable_Dict["FontSize"], 8, 500))
                        else:
                            Variable_FontSize = self.FontSize
                        #############################

                        ############################# can over-ride the global setting
                        if "BarPadX" in Variable_Dict:
                            Variable_BarPadX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise(Variable_name + ", BarPadX", Variable_Dict["BarPadX"], 1, 500))
                        else:
                            Variable_BarPadX = self.BarPadX
                        #############################

                        #########################################################
                        self.Variables_DictOfDicts[Variable_name] = dict([("Value", Variable_StartingValue_validated),
                                                                        ("Index", Variable_Index),
                                                                        ("StartingValue", Variable_StartingValue_validated),
                                                                        ("MinValue", Variable_MinValue),
                                                                        ("MaxValue", Variable_MaxValue),
                                                                        ("PositiveColor", Variable_PositiveColor),
                                                                        ("NegativeColor", Variable_NegativeColor),
                                                                        ("BarWidth", self.BarWidth),
                                                                        ("FontSize", Variable_FontSize),
                                                                        ("BarPadX", Variable_BarPadX),
                                                                        ("CanvasRectangleCoordinates", [0]*4),
                                                                        ("CanvasTextCoordinates", [0]*2)])
                                                #########################################################

                        #########################################################
                        #########################################################
                        #########################################################
                        #########################################################

                    #########################################################
                    #########################################################
                    #########################################################
                    #########################################################
                    #########################################################

                #########################################################
                #########################################################
                #########################################################
                #########################################################
                #########################################################
                #########################################################

            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            else:
                pass
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################

            #########################################################
            Ymin = 0
            Ymax = 0
            for VariableNameString in self.Variables_DictOfDicts:
                Ymin_temp = self.Variables_DictOfDicts[VariableNameString]["MinValue"]
                Ymax_temp = self.Variables_DictOfDicts[VariableNameString]["MaxValue"]

                if Ymin_temp < Ymin:
                    Ymin = Ymin_temp

                if Ymax_temp > Ymax:
                    Ymax = Ymax_temp

            self.MinValue_AcrossAllVariables = Ymin
            self.MaxValue_AcrossAllVariables = Ymax
            #########################################################

            print("Variables_DictOfDicts: " + str(self.Variables_DictOfDicts))
            print("MinValue_AcrossAllVariables: " + str(self.MinValue_AcrossAllVariables))
            print("MaxValue_AcrossAllVariables: " + str(self.MaxValue_AcrossAllVariables))

            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################
            #########################################################

        except:
            exceptions = sys.exc_info()[0]
            print("BarGraphDisplay_ReubenPython2and3Class  __init__: Variables_ListOfDicts, Exceptions: %s" % exceptions)
            traceback.print_exc()
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ProcessSetupDictInputsTheCanBeLiveChanged(setup_dict)
        #########################################################
        #########################################################
    
        #########################################################
        #########################################################
        self.myFrame = Frame(self.root)

        self.myFrame.grid(row = self.GUI_ROW,
                          column = self.GUI_COLUMN,
                          padx = self.GUI_PADX,
                          pady = self.GUI_PADY,
                          rowspan = self.GUI_ROWSPAN,
                          columnspan= self.GUI_COLUMNSPAN,
                          sticky = self.GUI_STICKY)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.Canvas_BorderWidth = 1

        self.MyCanvas = Canvas(self.myFrame,
                                width=self.Canvas_Width,
                                height=self.Canvas_Height,
                                bg="white",
                                highlightbackground="black")

        self.MyCanvas["highlightthickness"] = 0  #IMPORTANT Remove light grey border around the Canvas
        self.MyCanvas["bd"] = 0 #IMPORTANT Setting "bd", along with "highlightthickness" to 0 makes the Canvas be in the (0,0) pixel location instead of offset by those thicknesses
        self.MyCanvas.grid(row=0, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        for VariableNameString in self.Variables_DictOfDicts:
            self.CreateAndDrawRectangleOnCanvas_CanvasCoord(VariableNameString)
            self.CreateAndDrawVariableTextOnCanvas_CanvasCoord(VariableNameString)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.InitialUpdateHasBeenPerformedFlag = 0
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        time.sleep(0.1)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.GUI_ready_to_be_updated_flag = 1
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 1
        #########################################################
        #########################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def __del__(self):
        pass
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ExitProgram_Callback(self):
        pass
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ProcessSetupDictInputsTheCanBeLiveChanged(self, setup_dict):
        pass

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber):

        try:
            InputNumber_ConvertedToFloat = float(InputNumber)

        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThrough0and1values_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be 0 or 1 (value was " +
                          str(InputNumber_ConvertedToFloat) +
                          "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            #input("Press any key to continue")
            #sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValueue, RangeMaxValueue):
        try:
            InputNumber_ConvertedToFloat = float(InputNumber)

        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat >= RangeMinValueue and InputNumber_ConvertedToFloat <= RangeMaxValueue:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be in the range [" +
                          str(RangeMinValueue) +
                          ", " +
                          str(RangeMaxValueue) +
                          "] (value was " +
                          str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            #input("Press any key to continue")
            #sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def TellWhichFileWereIn(self):

        #We used to use this method, but it gave us the root calling file, not the class calling file
        #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

        frame = inspect.stack()[1]
        filename = frame[1][frame[1].rfind("\\") + 1:]
        filename = filename.replace(".py","")

        return filename
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def IsInputList(self, InputToCheck):

        result = isinstance(InputToCheck, list)
        return result
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def LimitNumber_FloatOutputOnly(self, min_val, max_val, test_val):
        if test_val > max_val:
            test_val = max_val

        elif test_val < min_val:
            test_val = min_val

        else:
            test_val = test_val

        test_val = float(test_val)

        return test_val
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateValue(self, VariableNameString, Value):

        try:
            self.Variables_DictOfDicts[VariableNameString]["Value"] = self.LimitNumber_FloatOutputOnly(self.Variables_DictOfDicts[VariableNameString]["MinValue"],
                                                                                                       self.Variables_DictOfDicts[VariableNameString]["MaxValue"],
                                                                                                       Value)

            self.GetRectangleCoordinatesListOnCanvas_CanvasCoord(VariableNameString)
            self.GetTextCoordinatesListOnCanvas_CanvasCoord(VariableNameString)

        except:
            exceptions = sys.exc_info()[0]
            print("UpdateValue: VariableNameString = " + str(VariableNameString) + ", Value = " + str(Value) + ", Exceptions: %s" % exceptions)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def CreateAndDrawRectangleOnCanvas_CanvasCoord(self, VariableNameString):

        try:
            self.GetRectangleCoordinatesListOnCanvas_CanvasCoord(VariableNameString) #Update the coordinates based on value

            self.Variables_DictOfDicts[VariableNameString]["Rectangle"] = self.MyCanvas.create_rectangle(self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][0],
                                                                                        self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][1],
                                                                                        self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][2],
                                                                                        self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][3],
                                                                                        outline="black",
                                                                                        fill=self.Variables_DictOfDicts[VariableNameString]["PositiveColor"],
                                                                                        width=self.Canvas_BorderWidth,
                                                                                        tags="RectangleOnCanvas_Tag")

        except:
            exceptions = sys.exc_info()[0]
            print("CreateAndDrawRectangleOnCanvas_CanvasCoord: Exceptions: %s" % exceptions)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetRectangleCoordinatesListOnCanvas_CanvasCoord(self, VariableNameString):

        try:
            XcoordDummy = 0

            RectanglePointList_Corner0 = self.ConvertMathPointToCanvasCoordinates([XcoordDummy, 0])
            RectanglePointList_Corner1 = self.ConvertMathPointToCanvasCoordinates([XcoordDummy, self.Variables_DictOfDicts[VariableNameString]["Value"]])

            self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][0] = 0.5*self.Canvas_BorderWidth + self.Variables_DictOfDicts[VariableNameString]["Index"]*(self.Variables_DictOfDicts[VariableNameString]["BarWidth"] + self.Variables_DictOfDicts[VariableNameString]["BarPadX"])
            self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][1] = RectanglePointList_Corner0[1]
            self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][2] = self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][0] + self.Variables_DictOfDicts[VariableNameString]["BarWidth"]
            self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][3] = RectanglePointList_Corner1[1] - 0.5 * self.Canvas_BorderWidth

            # -1 #The -1 accounts for indexing at 0

        except:
            exceptions = sys.exc_info()[0]
            print("GetRectangleCoordinatesListOnCanvas_CanvasCoord: Exceptions: %s" % exceptions)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def CreateAndDrawVariableTextOnCanvas_CanvasCoord(self, VariableNameString):

        try:

            self.GetTextCoordinatesListOnCanvas_CanvasCoord(VariableNameString)

            self.Variables_DictOfDicts[VariableNameString]["Text"] = self.MyCanvas.create_text(self.Variables_DictOfDicts[VariableNameString]["CanvasTextCoordinates"][0],
                                                                                                self.Variables_DictOfDicts[VariableNameString]["CanvasTextCoordinates"][1],
                                                                                                font=("Helvetica", int(self.Variables_DictOfDicts[VariableNameString]["FontSize"])),
                                                                                                text = VariableNameString)
        except:
            exceptions = sys.exc_info()[0]
            print("CreateAndDrawVariableTextOnCanvas_CanvasCoord: Exceptions: %s" % exceptions)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetTextCoordinatesListOnCanvas_CanvasCoord(self, VariableNameString):

        try:

            x =  (self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][0] + self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][2])/2.0

            #Set text in the middle of the color bar
            #y = (self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][1] + self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][3])/2.0

            #Set text fixed at the bottom of the graph
            y = self.ConvertMathPointToCanvasCoordinates([0, 0.85*self.MinValue_AcrossAllVariables])[1]

            self.Variables_DictOfDicts[VariableNameString]["CanvasTextCoordinates"][0] = x
            self.Variables_DictOfDicts[VariableNameString]["CanvasTextCoordinates"][1] = y

        except:
            exceptions = sys.exc_info()[0]
            print("GetTextCoordinatesListOnCanvas_CanvasCoord: Exceptions: %s" % exceptions)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ConvertMathPointToCanvasCoordinates(self, PointListXY):

        try:
            ##########################################################################################################
            x = PointListXY[0]
            y = PointListXY[1]

            W = self.Canvas_Width
            H = 1.0*self.Canvas_Height

            GraphBoxOutline_X0 = 0
            GraphBoxOutline_Y0 = 0
            ##########################################################################################################

            ##########################################################################################################
            X_min = -1.0
            X_max = 1.0

            Y_min = self.MinValue_AcrossAllVariables
            Y_max = self.MaxValue_AcrossAllVariables
            ##########################################################################################################

            ##########################################################################################################
            m_Xaxis = ((W - GraphBoxOutline_X0)/(X_max - X_min))
            b_Xaxis = W - m_Xaxis*X_max

            X_out = m_Xaxis*x + b_Xaxis
            ##########################################################################################################

            ##########################################################################################################
            m_Yaxis = ((H - GraphBoxOutline_Y0) / (Y_max - Y_min))
            b_Yaxis = H - m_Yaxis * Y_max

            Y_out = m_Yaxis * y + b_Yaxis
            ##########################################################################################################

            ##########################################################################################################
            X_out = X_out
            Y_out = self.MyCanvas.winfo_height() - Y_out #Flip/invert y-axis
            ##########################################################################################################

            return [X_out, Y_out]

        except:
            exceptions = sys.exc_info()[0]
            print("ConvertMathPointToCanvasCoordinates: Exceptions: %s" % exceptions)
            traceback.print_exc()
            return [-11111.0] * 2
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

        number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

        ListOfStringsToJoin = []

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if isinstance(input, str) == 1:
            ListOfStringsToJoin.append(input)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
            element = float(input)
            prefix_string = "{:." + str(number_of_decimal_places) + "f}"
            element_as_string = prefix_string.format(element)

            ##########################################################################################################
            ##########################################################################################################
            if element >= 0:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
                element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
            else:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
            ##########################################################################################################
            ##########################################################################################################

            ListOfStringsToJoin.append(element_as_string)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, list) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append(self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, tuple) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append("TUPLE" + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, dict) == 1:

            if len(input) > 0:
                for Key in input: #RECURSION
                    ListOfStringsToJoin.append(str(Key) + ": " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a dict()
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        else:
            ListOfStringsToJoin.append(str(input))
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if len(ListOfStringsToJoin) > 1:

            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            StringToReturn = ""
            for Index, StringToProcess in enumerate(ListOfStringsToJoin):

                ################################################
                if Index == 0: #The first element
                    if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                        StringToReturn = "{"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                        StringToReturn = "("
                    else:
                        StringToReturn = "["

                    StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
                ################################################

                ################################################
                elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                    StringToReturn = StringToReturn + StringToProcess + ", "
                ################################################

                ################################################
                else: #The last element
                    StringToReturn = StringToReturn + StringToProcess

                    if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                        StringToReturn = StringToReturn + "}"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                        StringToReturn = StringToReturn + ")"
                    else:
                        StringToReturn = StringToReturn + "]"

                ################################################

            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################

        elif len(ListOfStringsToJoin) == 1:
            StringToReturn = ListOfStringsToJoin[0]

        else:
            StringToReturn = ListOfStringsToJoin

        return StringToReturn
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_update_clock(self):

            #######################################################
            #######################################################
            #######################################################
            #######################################################
            if self.GUI_ready_to_be_updated_flag == 1:

                #######################################################
                #######################################################
                #######################################################
                try:

                    #######################################################
                    #######################################################
                    if self.InitialUpdateHasBeenPerformedFlag == 0:

                        #######################################################
                        for VariableNameString in self.Variables_DictOfDicts:
                            self.UpdateValue(VariableNameString, self.Variables_DictOfDicts[VariableNameString]["Value"])
                        #######################################################

                        self.InitialUpdateHasBeenPerformedFlag = 1
                    #######################################################
                    #######################################################

                    ####################################################### Debug drawing functions, unicorn
                    #######################################################

                    Xdummy = 0
                    Debug_PointCoords_CanvasCoord_1 = self.ConvertMathPointToCanvasCoordinates([Xdummy, -25])
                    Debug_PointCoords_CanvasCoord_2 = self.ConvertMathPointToCanvasCoordinates([Xdummy, 50])

                    #self.Variables_DictOfDicts["Var1"]["CanvasRectangleCoordinates"][1] = Debug_PointCoords_CanvasCoord_1[1]
                    #self.Variables_DictOfDicts["Var1"]["CanvasRectangleCoordinates"][3] = Debug_PointCoords_CanvasCoord_2[1]

                    #######################################################
                    ####################################################### Debug drawing functions, unicorn

                    #######################################################
                    #######################################################
                    for VariableNameString in self.Variables_DictOfDicts:

                        #######################################################
                        self.MyCanvas.coords(self.Variables_DictOfDicts[VariableNameString]["Rectangle"],
                                            self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][0],
                                            self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][1],
                                            self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][2],
                                            self.Variables_DictOfDicts[VariableNameString]["CanvasRectangleCoordinates"][3])
                        #######################################################

                        #######################################################
                        self.MyCanvas.coords(self.Variables_DictOfDicts[VariableNameString]["Text"],
                                             self.Variables_DictOfDicts[VariableNameString]["CanvasTextCoordinates"][0],
                                             self.Variables_DictOfDicts[VariableNameString]["CanvasTextCoordinates"][1])
                        #######################################################

                        #######################################################
                        if self.Variables_DictOfDicts[VariableNameString]["Value"] < 0:
                            self.MyCanvas.itemconfig(self.Variables_DictOfDicts[VariableNameString]["Rectangle"],
                                                     fill=self.Variables_DictOfDicts[VariableNameString]["NegativeColor"],
                                                     outline=self.Variables_DictOfDicts[VariableNameString]["NegativeColor"])
                        else:
                            self.MyCanvas.itemconfig(self.Variables_DictOfDicts[VariableNameString]["Rectangle"],
                                                     fill=self.Variables_DictOfDicts[VariableNameString]["PositiveColor"],
                                                     outline=self.Variables_DictOfDicts[VariableNameString]["PositiveColor"])
                        #######################################################

                        #######################################################
                        self.MyCanvas.itemconfig(self.Variables_DictOfDicts[VariableNameString]["Text"], text=VariableNameString + "\n" +
                                                                                                              self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.Variables_DictOfDicts[VariableNameString]["Value"], 0, 3))
                        #######################################################

                    #######################################################
                    #######################################################

                    #######################################################
                    #######################################################
                    self.Crosshairs_HorizontalLine_Yvalue = 0
                    
                    HorizontalLineCoords_LeftOfLine_CanvasCoord = self.ConvertMathPointToCanvasCoordinates([-1.0, self.Crosshairs_HorizontalLine_Yvalue])
                    HorizontalLineCoords_RightOfLine_CanvasCoord = self.ConvertMathPointToCanvasCoordinates([1.0, self.Crosshairs_HorizontalLine_Yvalue])

                    self.MyCanvas.delete("HorizontalLine_tag")
                    self.MyCanvas.create_line(HorizontalLineCoords_LeftOfLine_CanvasCoord[0] + 1*self.Canvas_BorderWidth, #Don't cross the border
                                                         HorizontalLineCoords_LeftOfLine_CanvasCoord[1],
                                                         HorizontalLineCoords_RightOfLine_CanvasCoord[0] - 1*self.Canvas_BorderWidth, #Don't cross the border
                                                         HorizontalLineCoords_RightOfLine_CanvasCoord[1],
                                                         fill="black",
                                                         width=1,
                                                         tags="HorizontalLine_tag")
                    #######################################################
                    #######################################################
                    
                except:
                    exceptions = sys.exc_info()[0]
                    print("BarGraphDisplay_ReubenPython3Class GUI_update_clock ERROR: Exceptions: %s" % exceptions)
                    traceback.print_exc()
                #######################################################
                #######################################################
                #######################################################

            #######################################################
            #######################################################
            #######################################################
            #######################################################

    ##########################################################################################################
    ##########################################################################################################