import webbrowser

print(webbrowser.get())

url = 'http://www.naver.com'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
# 프로그램을 종료하면 웹브라우저도 같이 닫힘