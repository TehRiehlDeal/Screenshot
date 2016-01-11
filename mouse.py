from pymouse import PyMouse
import time

m = PyMouse()
i = 0
while i < 603:
    m.click(30,300,1)
    time.sleep(1)
    m.click(980,515,1)
    time.sleep(1)
    m.click(1125,715,1)
    time.sleep(1)
    m.press(638,94,1)
    time.sleep(1)
    m.release(1395,1055,1)
    time.sleep(1)
    m.click(1135,675)
    time.sleep(1)
    m.click(1825,60)
    time.sleep(1)
    i = i + 1
