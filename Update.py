# Hare Krishna!
import pyautogui
import webbrowser
import pymysql
import email,smtplib, ssl
import mss.tools
import ctypes
import time
import datetime

# to set screensize based clicks
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(screensize)

# to timestamp
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %I:%M %p')

connection = pymysql.connect("localhost", "root", "root", "messages")
cursor = connection.cursor()

sql_query = "Select branch,sid,Recipient,body,whatsapp from whatsapp where whatsapp='N'"
cursor.execute(sql_query)
# fetch all of the rows from the query
data = cursor.fetchall()
# print the rows
for row in data:
    branch = row[0]
    sid = row[1]
    recipient = row[2]
    body = row[3]
    whatsapp = row[4]

    chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    url = "https://api.whatsapp.com/send?phone=" + recipient + "&text=" + body
    webbrowser.get(chromedir).open(url)
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
        #sendBtn2Location = pyautogui.locateOnScreen("send2.png")
        #pyautogui.click('send2.png')

        time.sleep(1)
        if screensize == (1600, 900):
            pyautogui.moveTo(1411, 151)
        elif screensize == (1366, 768):
            pyautogui.moveTo(1278, 101)
        pyautogui.click()
        #attach1BtnLocation = pyautogui.locateOnScreen("attachment.png")
        #pyautogui.click('attachment.png')

        time.sleep(1)
        if screensize == (1600, 900):
            pyautogui.moveTo(1411, 359)
        elif screensize == (1366, 768):
            pyautogui.moveTo(1279, 309)
        pyautogui.click()
        #attach2BtnLocation = pyautogui.locateOnScreen("attachment2.png")
        #pyautogui.click('attachment2.png')

        time.sleep(1)
        if screensize == (1600, 900):
            pyautogui.moveTo(202, 446)
        elif screensize == (1366, 768):
            pyautogui.moveTo(203, 415)
        pyautogui.click()
        # pyautogui.typewrite(r'C:\xampp\htdocs\xampp')
        pyautogui.typewrite(branch + sid + '.pdf')
        pyautogui.press('enter')

        time.sleep(5)
        if screensize == (1600, 900):
            pyautogui.moveTo(1427, 717)
        elif screensize == (1366, 768):
            pyautogui.moveTo(1293, 604)
        pyautogui.click()
        # attach3BtnLocation = pyautogui.locateOnScreen("attachment3.png")
        # pyautogui.click('attachment3.png')

        time.sleep(10)
        closeBtnLocation = pyautogui.locateOnScreen("close.png")
        pyautogui.click('close.png')
        time.sleep(1)
        pyautogui.press('enter')  # press the Enter key

    except Exception as e:
        print(e)
        img = pyautogui.screenshot()
        img.save('img.jpg')

        from email import encoders
        from email.mime.base import MIMEBase
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        subject = "Whatsapp Automation Error for SID.No: " + branch + sid
        body = "This is an email with attachment sent from Python Whatsapp Automation"
        sender_email = "biolinehopes@gmail.com"
        receiver_email = "jeanscircuits@gmail.com"
        password = "Bioline@2019"

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        message.attach(MIMEText(body, "plain"))

        filename = "img.jpg"  # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
            # Registering Error and making way to next report to send
            conn = pymysql.connect("localhost", "root", "root", "messages")
            cur = conn.cursor()
            update_query = "update whatsapp set whatsapp='E', log = %s where sid = %s"
            val = (st, sid)
            cur.execute(update_query, val)
            conn.commit()
            cur.close()
            conn.close()

        pyautogui.press('esc')
        pyautogui.press('esc')
        # Screenshot
        with mss.mss() as sct:
            # The screen part to capture
            monitor = {"top": 103, "left": 252, "width": 407, "height": 572}
            output = "status.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            print(output)

        closeBtnLocation = pyautogui.locateOnScreen("close.png")
        pyautogui.click('close.png')

    else:
        print("Success!")
        try:
            conn = pymysql.connect("localhost", "root", "root", "messages")
            cur = conn.cursor()
            update_query = "update whatsapp set whatsapp='S', log = %s where sid = %s"
            val = (st, sid)
            cur.execute(update_query, val)
            conn.commit()
            print(update_query)
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

cursor.close()
connection.close()
