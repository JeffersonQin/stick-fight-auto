import cv2
import numpy as np
import time
import win32gui
import win32ui
import win32con
import win32api

lower_yellow = (20, 198, 219)
upper_yellow = (24, 209, 249)
dpi_scale = 1.25
bmpfilenamename = "screenshot.bmp"

while True:
	start = time.time()
	# get window handle
	hwnd = win32gui.FindWindow('UnityWndClass', 'Stick Fight: The Game')
	# get window position
	rect = win32gui.GetWindowRect(hwnd)
	x = rect[0]
	y = rect[1]
	w = int((rect[2] - x) * dpi_scale)
	h = int((rect[3] - y) * dpi_scale)
	# take screenshot
	wDC = win32gui.GetWindowDC(hwnd)
	dcObj=win32ui.CreateDCFromHandle(wDC)
	cDC=dcObj.CreateCompatibleDC()
	dataBitMap = win32ui.CreateBitmap()
	dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
	cDC.SelectObject(dataBitMap)
	cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
	dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
	# Free Resources
	dcObj.DeleteDC()
	cDC.DeleteDC()
	win32gui.ReleaseDC(hwnd, wDC)
	win32gui.DeleteObject(dataBitMap.GetHandle())
	# read screenshot
	img = cv2.imread(bmpfilenamename)
	# convert colorspace to hsv
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# filter yellow
	yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

	# calculate center of mass
	# Find indices where we have mass
	mass_x, mass_y = np.where(yellow >= 255)
	# mass_x and mass_y are the list of x indices and y indices of mass pixels

	cent_x = np.average(mass_y)
	cent_y = np.average(mass_x)
	print('center:', cent_x, cent_y)
	if cent_x > 0 and cent_y > 0:
		# calculate mouse position
		mouse_x = int(cent_x / dpi_scale) + x
		mouse_y = int(cent_y / dpi_scale) + y
		print('mouse:', mouse_x, mouse_y)
		# control mouse
		win32api.SetCursorPos((mouse_x, mouse_y))
	end = time.time()

	# cv2.imwrite(f'screenshot-{end}.png', img)
	# cv2.imwrite(f'screenshot-{end}-mask.png', yellow)
	
	print('time:', end - start)
