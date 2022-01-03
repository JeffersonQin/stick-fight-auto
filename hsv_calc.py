import cv2

# read image
yellow = cv2.imread('./imgs/yellow-3.png')

# convert colorspace to hsv
hsv = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)

h_max = s_max = v_max = 0
h_min = s_min = v_min = 255

for row in range(hsv.shape[0]):
	for col in range(hsv.shape[1]):
		# get hsv values
		h, s, v = hsv[row, col]
		if not (h == 0 and s == 0 and v == 255):
			# update min and max values
			h_min = min(h_min, h)
			h_max = max(h_max, h)
			s_min = min(s_min, s)
			s_max = max(s_max, s)
			v_min = min(v_min, v)
			v_max = max(v_max, v)
			print(f'valid color: h: {h}, h_max: {h_max}, h_min: {h_min}, s: {s}, s_max: {s_max}, s_min: {s_min}, v: {v}, v_max: {v_max}, v_min: {v_min}')
