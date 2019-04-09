# Hare Krishna!
import pyautogui
import webbrowser
import pymysql
import ctypes
import time
import datetime

from threading import Timer, Thread, Event
class PT():

    def __init__(self, t, hFunction):
        self.t = t
        self.hFunction = hFunction
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

def printer():
    # function to loop
    # to set screensize based clicks
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    print(screensize)

    # to timestamp
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %I:%M %p')

    connection = pymysql.connect("localhost", "root", "root", "messages")
    cursor = connection.cursor()

    sql_query = "Select branch,sid,Recipient,body,whatsapp,id from whatsapp where whatsapp='N'"
    cursor.execute(sql_query)
    # fetch all of the rows from the query
    data = cursor.fetchall()
    # print the rows
    for row in data:

        recipient = row[2]
        body = row[3]
        ids = row[5]

        chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        url = "https://api.whatsapp.com/send?phone=91" + recipient + "&text=" + body
        webbrowser.get(chromedir).open(url)

        user32 = ctypes.WinDLL('user32')
        SW_MAXIMISE = 3
        hWnd = user32.GetForegroundWindow()
        user32.ShowWindow(hWnd, SW_MAXIMISE)

        try:
            time.sleep(5)
            if screensize == (1600, 900):
                pyautogui.moveTo(792, 350)
            elif screensize == (1366, 768):
                pyautogui.moveTo(669, 318)
            pyautogui.click()
            # sendBtnLocation = pyautogui.locateOnScreen("send.png")
            # pyautogui.click('send.png')

            time.sleep(10)
            if screensize == (1600, 900):
                pyautogui.moveTo(1463, 810)
            elif screensize == (1366, 768):
                pyautogui.moveTo(1329, 696)
            pyautogui.click()

            #sendbuttonlocation = pyautogui.locateOnScreen("send2.png")
            #pyautogui.click('send2.png')

            if screensize == (1600, 900):
                pyautogui.moveTo(472, 15)
            elif screensize == (1366, 768):
                pyautogui.moveTo(1329, 696)
            pyautogui.click()

            time.sleep(1)
            pyautogui.press('enter')  # press the Enter key

        except Exception as e:
            print(e)
            pyautogui.press('esc')
            pyautogui.press('esc')

            closeBtnLocation = pyautogui.locateOnScreen("close.png")
            pyautogui.click('close.png')

        else:
            print("Success!")
            try:
                conn = pymysql.connect("localhost", "root", "root", "messages")
                cur = conn.cursor()
                update_query = "update whatsapp set whatsapp='S' where id = %s" % ids
                cur.execute(update_query)
                conn.commit()
                print(update_query)
            except Exception as e:
                print(e)
            finally:
                cur.close()
                conn.close()

    cursor.close()
    connection.close()
    print(st)
    time.sleep(60)

t = PT(1, printer)

t.start()

