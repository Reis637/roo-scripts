import pydirectinput
import time

screenWidth, screenHeight = pydirectinput.size()

plantarX, plantarY = 1670, 810
acelerarX, acelerarY = 1570, 690
cosecharX, cosecharY = 1670, 810

print(5)
time.sleep(3)


currentMouseX, currentMouseY = pydirectinput.position()
print(str(currentMouseX) + ", " + str(currentMouseY))