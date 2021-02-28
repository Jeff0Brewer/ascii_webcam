import math, cv2, os, sys, subprocess
from platform import system

class ASCIIdrawer:
	# class for ascii drawing of image stream
	def __init__(self, img_w, img_h):
		col, lin = os.get_terminal_size()
		ascii_aspect = 0.5
		chars = ' `-~^=olTIO0'

		self.img_w = img_w
		self.img_h = img_h
		self.w = col
		self.h = round(col*img_h/img_w*ascii_aspect)
		self.chars = [c for c in chars]
		self.char_max = len(self.chars) - 1
		self.val_max = 255*3

	def draw(self, img):
		scaled = cv2.resize(img, (self.w, self.h))
		buf = ''
		for y in range(self.h):
			for x in range(self.w - 1, 0, -1):
				buf += self.chars[math.floor(sum(scaled[y][x])/self.val_max*self.char_max)]
			buf += '\n'
		subprocess.check_call(['cls' if system().lower() == 'windows' else 'clear'], shell=True)
		sys.stdout.write(buf)
		sys.stdout.flush()

cam = cv2.VideoCapture(0)
ret, frame = cam.read()
drawer = ASCIIdrawer(len(frame[0]), len(frame))

while True:
	ret, frame = cam.read()
	drawer.draw(frame)