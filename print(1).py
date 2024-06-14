import pyautogui

size = pyautogui.size()
#print(size)

print(pyautogui.position())
pyautogui.moveTo(200, 100, duration=5)
print(pyautogui.position())
p = pyautogui.position()
pyautogui.moveTo(p[0]+100, p[1]+300, duration=1)
print(pyautogui.position())
pyautogui.moveTo(p.x+200, p.y+400, duration=1)