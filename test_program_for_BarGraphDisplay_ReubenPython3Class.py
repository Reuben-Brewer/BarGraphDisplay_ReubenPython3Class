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
from BarGraphDisplay_ReubenPython3Class import *
from MyPrint_ReubenPython2and3Class import *
#################################################

#################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
#################################################

#################################################
from tkinter import * #Python 3
import tkinter.font as tkFont #Python 3
from tkinter import ttk
#################################################

#################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global BarGraphDisplay_ReubenPython3ClassObject
    global BarGraphDisplay_OPEN_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    global SINUSOIDAL_INPUT_TO_COMMAND_1
    global SINUSOIDAL_INPUT_TO_COMMAND_2

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if BarGraphDisplay_OPEN_FLAG == 1:
                BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("Var1", SINUSOIDAL_INPUT_TO_COMMAND_1) #TOO SLOW TO UPDATE FROM NON-GUI THREAD!
                BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("Var2", SINUSOIDAL_INPUT_TO_COMMAND_2) #TOO SLOW TO UPDATE FROM NON-GUI THREAD!

                BarGraphDisplay_ReubenPython3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_BarGraphDisplay
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_BarGraphDisplay = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_BarGraphDisplay, text='   BarGraphDisplay   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_BarGraphDisplay = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_BarGraphDisplay_ReubenPython3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 0

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_SINUSOIDAL_TEST_FLAG
    USE_SINUSOIDAL_TEST_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_BarGraphDisplay
    global GUI_COLUMN_BarGraphDisplay
    global GUI_PADX_BarGraphDisplay
    global GUI_PADY_BarGraphDisplay
    global GUI_ROWSPAN_BarGraphDisplay
    global GUI_COLUMNSPAN_BarGraphDisplay
    GUI_ROW_BarGraphDisplay = 1

    GUI_COLUMN_BarGraphDisplay = 0
    GUI_PADX_BarGraphDisplay = 1
    GUI_PADY_BarGraphDisplay = 10
    GUI_ROWSPAN_BarGraphDisplay = 1
    GUI_COLUMNSPAN_BarGraphDisplay = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 2

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 10
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 900

    global root_height
    root_height = 900

    global TabControlObject
    global Tab_MainControls
    global Tab_BarGraphDisplay
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150) #RGB
    TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150)  # RGB
    TKinter_LightBlueColor = '#%02x%02x%02x' % (150, 150, 255) #RGB
    TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150) #RGB
    TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240) #RGB

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global SINUSOIDAL_INPUT_TO_COMMAND_1
    SINUSOIDAL_INPUT_TO_COMMAND_1 = 0.0

    global SINUSOIDAL_INPUT_TO_COMMAND_2
    SINUSOIDAL_INPUT_TO_COMMAND_2 = 0.0

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle = 2.0

    global SINUSOIDAL_MOTION_INPUT_MinValue_1
    SINUSOIDAL_MOTION_INPUT_MinValue_1 = -50.0

    global SINUSOIDAL_MOTION_INPUT_MaxValue_1
    SINUSOIDAL_MOTION_INPUT_MaxValue_1 = 50.0

    global SINUSOIDAL_MOTION_INPUT_MinValue_2
    SINUSOIDAL_MOTION_INPUT_MinValue_2 = -25

    global SINUSOIDAL_MOTION_INPUT_MaxValue_2
    SINUSOIDAL_MOTION_INPUT_MaxValue_2 = 25
    #################################################
    #################################################

    #################################################
    #################################################
    global BarGraphDisplay_ReubenPython3ClassObject

    global BarGraphDisplay_OPEN_FLAG
    BarGraphDisplay_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_BarGraphDisplay = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################
    global BarGraphDisplay_Variables_ListOfDicts
    BarGraphDisplay_Variables_ListOfDicts = [dict([("Name", "Var1"), ("StartingValue", 50.0), ("MinValue", -100), ("MaxValue", 100)]),
                                             dict([("Name", "Var2"), ("StartingValue", -25), ("MinValue", -50), ("MaxValue", 50)]),
                                             dict([("Name", "foo"), ("StartingValue", 33), ("MinValue", -33), ("MaxValue", 33), ("FontSize", 8), ("PositiveColor", TKinter_LightBlueColor), ("NegativeColor", TKinter_LightYellowColor)])]

    global BarGraphDisplay_ReubenPython3ClassObject_GUIparametersDict
    BarGraphDisplay_ReubenPython3ClassObject_GUIparametersDict = dict([("root", Tab_BarGraphDisplay),
                                    ("GUI_ROW", GUI_ROW_BarGraphDisplay),
                                    ("GUI_COLUMN", GUI_COLUMN_BarGraphDisplay),
                                    ("GUI_PADX", GUI_PADX_BarGraphDisplay),
                                    ("GUI_PADY", GUI_PADY_BarGraphDisplay),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_BarGraphDisplay),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_BarGraphDisplay)])

    global BarGraphDisplay_ReubenPython3ClassObject_setup_dict
    BarGraphDisplay_ReubenPython3ClassObject_setup_dict = dict([("GUIparametersDict", BarGraphDisplay_ReubenPython3ClassObject_GUIparametersDict),
                                                                ("Variables_ListOfDicts", BarGraphDisplay_Variables_ListOfDicts),
                                                                ("Canvas_Width", 500),
                                                                ("Canvas_Height", 300),
                                                                ("BarWidth", 100),
                                                                ("BarPadX", 10),
                                                                ("FontSize", 12),
                                                                ("NegativeColor", TKinter_LightRedColor),
                                                                ("PositiveColor", TKinter_LightGreenColor)])

    try:
        BarGraphDisplay_ReubenPython3ClassObject = BarGraphDisplay_ReubenPython3Class(BarGraphDisplay_ReubenPython3ClassObject_setup_dict)
        BarGraphDisplay_OPEN_FLAG = BarGraphDisplay_ReubenPython3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

    except:
        exceptions = sys.exc_info()[0]
        print("BarGraphDisplay_ReubenPython3ClassObject __init__: Exceptions: %s" % exceptions, 0)
        traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MyPrint_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if BarGraphDisplay_OPEN_FLAG != 1:
        print("Failed to open BarGraphDisplay_ReubenPython3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1 and MyPrint_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_BarGraphDisplay_ReubenPython3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):
        try:
            ###################################################
            ###################################################
            CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
            ###################################################
            ###################################################

            ################################################### SET's
            ###################################################
            if USE_SINUSOIDAL_TEST_FLAG == 1:
                time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)

                SINUSOIDAL_INPUT_TO_COMMAND_1 = (SINUSOIDAL_MOTION_INPUT_MaxValue_1 + SINUSOIDAL_MOTION_INPUT_MinValue_1)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue_1 - SINUSOIDAL_MOTION_INPUT_MinValue_1)*math.sin(time_gain*CurrentTime_MainLoopThread)
                SINUSOIDAL_INPUT_TO_COMMAND_2 = (SINUSOIDAL_MOTION_INPUT_MaxValue_2 + SINUSOIDAL_MOTION_INPUT_MinValue_2)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue_2 - SINUSOIDAL_MOTION_INPUT_MinValue_2)*math.sin(time_gain*CurrentTime_MainLoopThread + math.pi/4.0)
            ###################################################
            ###################################################

        except:
            exceptions = sys.exc_info()[0]
            print("test_program_for_BarGraphDisplay_ReubenPython3Class: while(EXIT_PROGRAM_FLAG == 0) Exceptions: %s" % exceptions)
            traceback.print_exc()

        time.sleep(0.002)
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_BarGraphDisplay_ReubenPython3Class.")

    #################################################
    if BarGraphDisplay_OPEN_FLAG == 1:
        BarGraphDisplay_ReubenPython3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################