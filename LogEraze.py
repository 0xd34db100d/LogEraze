import colorama
import psutil
import pyfiglet
from os import path, listdir, getenv, remove, system
from numpy import *
from readchar import readkey, key
import glob
from time import sleep
from sys import exit
from ctypes import windll
from shutil import rmtree

windll.kernel32.SetConsoleTitleW("LogEraze")
colorama.init()

# FUNCTIONS
def get_subs(a):
    return [name for name in listdir(a)
            if path.isdir(path.join(a, name))]


def DeleteTrash(RPATH, TEMPF):
    try:
        temp = glob.glob(RPATH + "\\logs\\*")
        for f in temp:
            if path.isfile(f):
                remove(f)
            else:
                rmtree(f)
        temp = glob.glob(RPATH + "\\logs\\.*")
        for f in temp:
            if path.isfile(f):
                remove(f)
            else:
                rmtree(f)
    except Exception as e:
        print(colorama.Fore.MAGENTA +
              "[ERROR] Cleared logs, but some errors appeared!")
        print(e, '\n')
    print(colorama.Fore.MAGENTA + "[SUCCESS] Cleared logs!")
    try:
        temp = glob.glob(RPATH + "\\Downloads\\*")
        for f in temp:
            if path.isfile(f):
                remove(f)
            else:
                rmtree(f)
        temp = glob.glob(RPATH + "\\Downloads\\.*")
        for f in temp:
            if path.isfile(f):
                remove(f)
            else:
                rmtree(f)
    except Exception as e:
        print(colorama.Fore.MAGENTA +
              "[ERROR] Cleared Downloads, but some errors appeared!")
        print(e, '\n')
    print(colorama.Fore.MAGENTA + "[SUCCESS] Cleared Downloads!")
    try:
        temp = glob.glob(RPATH + "\\LocalStorage\\*")
        for f in temp:
            if path.isfile(f):
                remove(f)
            else:
                rmtree(f)
        temp = glob.glob(RPATH + "\\LocalStorage\\.*")
        for f in temp:
            if path.isfile(f):
                remove(f)
            else:
                rmtree(f)
    except Exception as e:
        print(colorama.Fore.MAGENTA +
              "[ERROR] Cleared LocalStorage, but some errors appeared!")
        print(e, '\n')
    print(colorama.Fore.MAGENTA + "[SUCCESS] Cleared LocalStorage!")
    if path.exists(RPATH + "\\AnalysticsSettings.xml"):
        remove(RPATH + "\\AnalysticsSettings.xml")
        print(colorama.Fore.MAGENTA +
              "[SUCCESS] Deleted AnalysticsSettings.xml!")
    if path.exists(RPATH + "\\frm.cfg"):
        remove(RPATH + "\\frm.cfg")
        print(colorama.Fore.MAGENTA + "[SUCCESS] Deleted frm.cfg!")
    if path.exists(RPATH + "\\GlobalBasicSettings_13.xml"):
        remove(RPATH + "\\GlobalBasicSettings_13.xml")
        print(colorama.Fore.MAGENTA +
              "[SUCCESS] Deleted GlobalBasicSettings_13.xml!")
    print(colorama.Fore.MAGENTA +
          "[INFO] Starting deleting LocalTemp Roblox *.log, crashpad_roblox files and folders...")
    try:
        temp = glob.glob(TEMPF + "\\*.log")
        for f in temp:
            remove(f)
        if path.exists(TEMPF + "\\Roblox"):
            temp = glob.glob(TEMPF + "\\Roblox\\*")
            for f in temp:
                if path.isfile(f):
                    remove(f)
                else:
                    rmtree(f)
            temp = glob.glob(TEMPF + "\\Roblox\\.*")
            for f in temp:
                if path.isfile(f):
                    remove(f)
                else:
                    rmtree(f)
        if path.exists(TEMPF + "\\crashpad_roblox"):
            temp = glob.glob(TEMPF + "\\crashpad_roblox\\*")
            for f in temp:
                if path.isfile(f):
                    remove(f)
                else:
                    rmtree(f)
            temp = glob.glob(TEMPF + "\\crashpad_roblox\\.*")
            for f in temp:
                if path.isfile(f):
                    remove(f)
                else:
                    rmtree(f)
    except Exception as e:
        print(colorama.Fore.MAGENTA +
              "[ERROR] Cleared LocalTemp, but some errors appeared!")
        print(e, '\n')
    print(colorama.Fore.MAGENTA + "[SUCCESS] Cleared LocalTemp!")


def KillRoblox():
    for proc in psutil.process_iter():
        if proc.name() == ROBLOXNAME:
            try:
                proc.suspend()
                print(colorama.Fore.MAGENTA + "[SUSPEND] Suspended Roblox!")
                proc.kill()
                print(colorama.Fore.MAGENTA + "[KILL] Killed Roblox!")
            except Exception as e:
                print(colorama.Fore.MAGENTA +
                      "[ERROR] Killed Roblox, but some errors appeared!")
                print(e, '\n')


def Welcome():
    system("cls")
    print(colorama.Fore.MAGENTA + pyfiglet.figlet_format('LogEraze'))
    print('Version: 1; By John Strider :3 @ 2022\n')
    print(colorama.Fore.MAGENTA + 'Current Roblox path: ' +
          colorama.Fore.WHITE + RobloxPath + '\n')
    print(colorama.Fore.MAGENTA + 'Current installed Roblox versions: ')
    for i in CurrentVersions:
        print(colorama.Fore.MAGENTA + " - " + colorama.Fore.WHITE + i)
    print(colorama.Fore.WHITE + "\n\n\n> Q - Delete logs",
          "\n> E - Kill Roblox and delete logs", "\n> ESC - Exit")


# VARIABLES
ROBLOXNAME = "RobloxPlayerBeta.exe"
try:
    ROBLOXPATHLIST = ["0"]
    for proc in psutil.process_iter():
        if proc.name() == ROBLOXNAME:
            ROBLOXPATHLIST = proc.exe().split('\\')
    ROBLOXPATHLIST[0] = ROBLOXPATHLIST[0] + '\\'
    versionsindex = ROBLOXPATHLIST.index('Versions')
    robloxindex = ROBLOXPATHLIST.index('Roblox')

    VersionsPath = path.join(*ROBLOXPATHLIST[:versionsindex + 1])
    RobloxPath = path.join(*ROBLOXPATHLIST[:robloxindex + 1])

except (ValueError, NameError):
    print(colorama.Fore.MAGENTA +
          "[ERROR] Can't get Roblox path from process, trying APPDATA Search...")
    RobloxPath = getenv('APPDATA').split('\\')
    RobloxPath[0] = RobloxPath[0] + '\\'
    del RobloxPath[-1]
    RobloxPath.extend(['Local', 'Roblox'])
    VersionsPath = RobloxPath.copy()
    VersionsPath.extend(['Versions'])
    VersionsPath = path.join(*VersionsPath)
    RobloxPath = path.join(*RobloxPath)

CurrentVersions = get_subs(VersionsPath)
TempFolder = getenv('APPDATA').split('\\')
TempFolder[0] = TempFolder[0] + '\\'
del TempFolder[-1]
TempFolder.extend(['Local', 'Temp'])
TempFolder = path.join(*TempFolder)

print(colorama.Fore.MAGENTA + "[SUCCESS] Found all we need!")

# MAIN
while True:
    Welcome()
    k = ""
    try:
        k = readkey()
    except Exception:
        pass
    if k == "q":
        print(colorama.Fore.WHITE, "\n>----- Running -----<\n")
        DeleteTrash(RobloxPath, TempFolder)
        print(colorama.Fore.WHITE, "\n>---- Canceled! ----<\n")
        k = ""
        try:
            k = readkey()
        except Exception:
            pass
    if k == "e":
        print(colorama.Fore.WHITE, "\n>----- Running -----<\n")
        KillRoblox()
        sleep(1)
        DeleteTrash(RobloxPath, TempFolder)
        print(colorama.Fore.WHITE, "\n>---- Canceled! ----<\n")
        k = ""
        try:
            k = readkey()
        except Exception:
            pass
    if k == key.ESC:
        exit(0)
