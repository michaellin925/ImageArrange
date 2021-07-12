# To Do:
# convert non-jpg file into jpg
# rename every file into "imgyyyymmddxxx" where xxx is the serial number
# move renamed files to other folder

# only targeting jpg, jfif, png?

import os
import time
import shutil
from datetime import datetime
from PIL import Image


def convert_jfif_to_jpg(jfif_file):
	img = Image.open(jfif_file)
	img.save(jfif_file[:-5] + ".jpg")

def convert_png_to_jpg(png_file):
	img = Image.open(png_file)
	img.save(png_file[:-4] + ".jpg")

def rename_image(jpg_file):
	pass


def main():

	dir_path = os.path.dirname(os.path.abspath(__file__))
	date_time = str(datatime.fromtimestamp(int(time.time())))
	date_time_num = ''

	for char in date_time:
		if char != '-' and char != ' ' and char != ':':
			date_time_num += char

	date_time_num = date_time_num[:-2]		


	for file in os.listdir(dir_path)

if __name__ == "__main__":
	main()