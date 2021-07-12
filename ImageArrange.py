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

def rename_image(jpg_file, time_string, serial_number):
	img = Image.open(jpg_file)

	if serial_number < 10:
		new_file_name = "img" + time_string + "000" + serial_number + ".jpg"
	elif serial_number < 100:
		new_file_name = "img" + time_string + "00" + serial_number + ".jpg"
	elif serial_number < 1000:
		new_file_name = "img" + time_string + "0" + serial_number + ".jpg"
	else:
		new_file_name = "img" + time_string + serial_number + ".jpg"

	img.save(new_file_name)
	print("File", jpg_file, "renamed into", new_file_name)


def main():

	dir_path = os.path.dirname(os.path.abspath(__file__))
	date_time = str(datetime.fromtimestamp(int(time.time())))
	date_time_num = ''

	for char in date_time:
		if char != '-' and char != ' ' and char != ':':
			date_time_num += char
	
	jfif_file_counter = 0
	png_file_counter = 0
	jpg_file_counter = 0

	for file in os.listdir(dir_path):
		if file.endswith(".jfif"):
			print("Converting JFIF file:", file)
			convert_jfif_to_jpg(file)
			jfif_file_counter += 1

		if file.endswith(".png"):
			print("Converting PNG file:", file)
			convert_png_to_jpg(file)
			png_file_counter += 1

		if file.endswith(".jpg"):
			jpg_file_counter += 1

	print("Total JFIF files converted:", jfif_file_counter)
	print("Total PNG files converted:", png_file_counter)
	print("Total JPG files found:", jpg_file_counter)

	serial_number = 1
	rename_counter = 0

	for file in os.listdir(dir_path):
		if file.endswith(".jpg"):
			rename_image(file, date_time_num, serial_number)
			serial_number += 1
			rename_counter += 1

	print("Total files renamed:", rename_counter)

	lock_screen_path = "C:/Users/micha/Pictures/LockScreen/"
	move_counter = 0

	for file in os.listdir(dir_path):
		if file.startswith("img"):
			shutil.move(os.path.join(dir_path, file), lock_screen_path)
			move_counter += 1

	print("Total files moved:", move_counter)

	if move_counter == rename_counter:
		for file in os.listdir(dir_path):
			if not file.endswith(".py"):
				os.remove(file)


if __name__ == "__main__":
	main()

