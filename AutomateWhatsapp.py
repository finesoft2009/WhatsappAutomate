# "Hare Krishna!"
import pyautogui
import time
import webbrowser
import pymysql
import email,smtplib,ssl

try:
    connection = pymysql.connect("localhost", "root", "root", "messages")
    cursor = connection.cursor()

    sql_query = "Select branch,sid,Recipient,body,whatsapp from messages where whatsapp='N'"
    cursor.execute(sql_query)
    data = cursor.fetchall()

    for record in data:
        branch = record[0]
        sid = record[1]
        recipient = record[2]
        body = record[3]
        whatsapp = record[4]

        # print(data, end="\n")
        print("SID.No: %s ""\n"
        "Branch: %s ""\n"
        "Recipient: %s ""\n"
        "Body: %s " % (sid, branch, recipient, body))
    cursor.close()
    connection.close()

    chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    url = "https://api.whatsapp.com/send?phone=" + recipient + "&text=" + body
    webbrowser.get(chromedir).open(url)

    time.sleep(5)
    pyautogui.moveTo(792, 371)
    pyautogui.click()
    #sendBtnLocation = pyautogui.locateOnScreen("send.png")
    #pyautogui.click('send.png')
   
    time.sleep(10)
    sendBtn2Location = pyautogui.locateOnScreen("send2.png")
    pyautogui.click('send2.png')
    time.sleep(1)
    # attach .pdf file
    attach1BtnLocation = pyautogui.locateOnScreen("attachment.png")
    pyautogui.click('attachment.png')
    time.sleep(1)
    attach2BtnLocation = pyautogui.locateOnScreen("attachment2.png")
    pyautogui.click('attachment2.png')
    time.sleep(1)
    pyautogui.moveTo(209, 674)
    pyautogui.click()
    # pyautogui.typewrite(r'C:\xampp\htdocs\xampp')
    pyautogui.typewrite(branch+sid+'.txt')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.moveTo(243, 134)
    pyautogui.doubleClick()
    # if no file found?:( will go here...
    time.sleep(2)
    attach3BtnLocation = pyautogui.locateOnScreen("attachment3.png")
    pyautogui.click('attachment3.png')
    time.sleep(10)
    closeBtnLocation = pyautogui.locateOnScreen("close.png")
    pyautogui.click('close.png')
    time.sleep(2)
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
    try:
        conn = pymysql.connect("localhost", "root", "root", "messages")
        cur = conn.cursor()
        update_query = "update messages set whatsapp='E' where sid = %s" % sid
        cur.execute(update_query)
        conn.commit()
        print(update_query)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()

    pyautogui.press('esc')
    pyautogui.press('esc')
    closeBtnLocation = pyautogui.locateOnScreen("close.png")
    pyautogui.click('close.png')

else:
    print("Success!")
    try:
        conn = pymysql.connect("localhost", "root", "root", "messages")
        cur = conn.cursor()
        update_query = "update messages set whatsapp='S' where sid = %s" % sid
        cur.execute(update_query)
        conn.commit()
        print(update_query)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
