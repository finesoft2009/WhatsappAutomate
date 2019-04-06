import webbrowser
chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
url = "https://api.whatsapp.com/send?phone="+"919578413023"+"&text="+"HareRama!"
webbrowser.get(chromedir).open(url)
