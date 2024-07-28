import win32.win32gui
import win32.win32process
import psutil
import ctypes
import time
import sys

VERSION = "0.1"
NOSTALE_CLIENT_EXECUTABLE = "NostaleClientX.exe"
IDLE_TIME_IN_SEC = 60
OUT = False
if "--out" in sys.argv:
    OUT = True
    OUT_file = open("output.log", "a")
    sys.stdout = OUT_file

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible

def check_processes():
    procs = {p.pid: p.info for p in psutil.process_iter(['name', 'username'])}
    ret = []
    for pid, data in procs.items():
        if data["name"] == NOSTALE_CLIENT_EXECUTABLE:
            ret.append(pid)
    return ret

def get_hwnds_for_pid(pid):
    def callback(hwnd, hwnds):
        _, found_pid = win32.win32process.GetWindowThreadProcessId(hwnd)

        if found_pid == pid:
            hwnds.append(hwnd)
        return True
    hwnds = []
    win32.win32gui.EnumWindows(callback, hwnds)
    return hwnds

def check_pid(pid):
    any = False
    hwnd = get_hwnds_for_pid(pid)
    for h in hwnd:
        if win32.win32gui.IsWindowVisible(h) == 1:
            any = True
    return True if any == False else False

def check():
    pids = check_processes()
    kill_pids = []
    for pid in pids:
        if check_pid(pid) == True:
            kill_pids.append(pid)
    print(f"Killing PIDs: {kill_pids}")
    for pid in kill_pids:
        p = psutil.Process(pid)
        p.kill()
        del(p)

if __name__ == "__main__":
    print(f"NosTale Auto Process Closer v{VERSION}")
    print(f"This tool runs every {IDLE_TIME_IN_SEC} seconds and kills any instance of '{NOSTALE_CLIENT_EXECUTABLE}' without an active window.")
    t1 = time.time()
    while True:
        try:
            t2 = time.time()
            if t2 - t1 >= IDLE_TIME_IN_SEC:
                print("Checking!")
                check()
                t1 = t2
            time.sleep(1)
        except KeyboardInterrupt:
            print("Exiting!")
            if OUT == True:
                OUT_file.close()
            break