import pyautogui

p = pyautogui.position()
print(p)
pyautogui.click(3680, 95, duration=1)
pyautogui.click(p.x=50, p.y+100, duration=1)
pyautogui.click()
pyautogui.doubleclick()
pyautogui.click(clicks=50)
pyautogui.rightClick()
