import os
import subprocess as sp
import time
import wmi

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'notepadwin' : 'C:\\Windows\\System32\\notepad.exe',
    'discord': "C:\\Users\\deepak\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'taskmgr' : 'C:\\Windows\\System32\\Taskmgr.exe',
}


def open_notepad():
    os.startfile(paths['notepadwin'])
    print("notepad opened successfully")
    time.sleep(5)

def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')
    print("cmd opened successfully")
    time.sleep(5)

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    print("camera opened successfully")
    #time.sleep(5)

def open_calculator():
    sp.Popen(paths['calculator'])
    print("calculator opened successfully")
    time.sleep(5)

def open_taskmanager():
    os.startfile(paths['taskmgr'])
    print("task manager opened successfully")
    time.sleep(5)

def open_chrome():
    """os.startfile(paths['chrome'])
    os.system("chrome")"""
    print("chrome opened successfully")
    time.sleep(5)

def open_msedge():
    os.system('start msedge')
    print("edge opened successfully")
    time.sleep(5)

def open_settings():
    os.system('start microsoft.systemsettings:', shell=True)
    print("settings opened successfully")
    time.sleep(5)

def logoff():
    sp.call(["shutdown", "/l"])
    time.sleep(5)
#logfile trash
def trash_logfile():
    os.remove("logfile.txt")
    time.sleep(5)
"""
def close_cmd():
    terminate("cmd.exe")
    
def close_camera():
    terminate("WindowsCamera.exe")
    
def close_notepad():
    terminate("notepad++.exe")
    
def close_msedge():
    terminate("msedge.exe")
    
def close_chrome():
    terminate("chrome.exe")
    
def close_taskmanager():
    terminate("Taskmgr.exe")
    
def close_settings():
    terminate("SystemSettings.exe")
    
def close_calculator():
    terminate(" ")

def terminate(procname):
    try:
        f = wmi.WMI()
        flag = 0
        for p in f.Win32_Process():
            if procname == p.Name:
                p.Terminate()
                flag = 1
        print("{0} terimated successfully".format(pname)) if flag == 1 else print("No Process found")       
    
    except:
        print("Something went wrong, termination")"""
