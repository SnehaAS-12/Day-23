#Create a browse option with a specific folder which has all the JPEG Files & create a Convert button to convert the image from JPEG to PNG – Basic Image converter App

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
root = tk.Tk()
canvas1 = tk.Canvas(root, width=550, height=550, bg='white', relief='raised')
canvas1.pack()
label1 = tk.Label(root, text='Image Conversion From JPEG To PNG')
label1.config(font=('algerian', 22))
canvas1.create_window(250,50, window=label1)
def getJPG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
browseButton_JPG = tk.Button(text="      Import JPG File     ", command=getJPG, bg='yellow', fg='black',font=('algerian', 16, 'bold'))
canvas1.create_window(200, 250,window=browseButton_JPG)
def convertToPNG():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)
saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='black', fg='yellow',font=('algerian', 16, 'bold'))
canvas1.create_window(280, 250,window=saveAsButton_PNG)
root.mainloop()


#Create another button as ‘fetch button’ and have a functionality of fetching the weather on a given location in text box

import pyowm
from tkinter import *
def omw() :
    api_key = "31688f276119b3907a13f19e4cf7c6b9"
    owm_obj=pyowm.OWM(api_key)
    city_name = city_f.get()
    obs_obj=owm_obj.weather_at_place(city_name)
    weather=obs_obj.get_weather()
    temp = weather.get_temperature('celsius')["temp"]
    humidity = weather.get_humidity()
    description = weather.get_detailed_status()
    temp_f.insert(15, str(temp)+ " Celcius " )
    humid_f.insert(15, str(humidity) + " %")
    desc_f.insert(10, str(description) )
def clear() :
    city_f.delete(0, END)
    temp_f.delete(0, END)
    humid_f.delete(0, END)
    desc_f.delete(0, END)
root = Tk()
root.title("Weather")
root.configure()
root.geometry("500x480")
label = Label(root, text = "Weather :" )
label1 = Label(root, text = "Enter City :")
label2 = Label(root, text = "Temperature :")
label3 = Label(root, text = "Humidity :")
label4 = Label(root, text = "Description  :")
city_f = Entry(root)
temp_f = Entry(root)
humid_f = Entry(root)
desc_f = Entry(root)
b1 = Button(root, text = "Toaday's Weather", command = omw)
b2 = Button(root, text = "Delete", command = clear)
label.grid(row = 0, column = 2)
label1.grid(row = 2, column = 2)
label2.grid(row = 5, column = 2)
label3.grid(row = 7, column = 2)
label4.grid(row = 9, column = 2)
city_f.grid(row = 3, column = 2, ipadx ="180")
temp_f.grid(row = 6, column = 2, ipadx ="180")
humid_f.grid(row = 8, column = 2, ipadx ="180")
desc_f.grid(row = 10, column = 2, ipadx ="180")
b1.grid(row = 4, column = 2)
b2.grid(row = 11, column = 2)
root.mainloop()


# Watermark Merger App

pip install imutils
from imutils import paths
import numpy as np
import argparse
import cv2
import os
ap = argparse.ArgumentParser()
ap.add_argument("-w", "--watermark", required=True,
	help="path to watermark image (assumed to be transparent PNG)")
ap.add_argument("-i", "--input", required=True,
	help="path to the input directory of images")
ap.add_argument("-o", "--output", required=True,
	help="path to the output directory")
ap.add_argument("-a", "--alpha", type=float, default=0.25,
	help="alpha transparency of the overlay (smaller is more transparent)")
ap.add_argument("-c", "--correct", type=int, default=1,
	help="flag used to handle if bug is displayed or not")
args = vars(ap.parse_args())
watermark = cv2.imread(args["watermark"], cv2.IMREAD_UNCHANGED)
(wH, wW) = watermark.shape[:2]
if args["correct"] > 0:
	(B, G, R, A) = cv2.split(watermark)
	B = cv2.bitwise_and(B, B, mask=A)
	G = cv2.bitwise_and(G, G, mask=A)
	R = cv2.bitwise_and(R, R, mask=A)
	watermark = cv2.merge([B, G, R, A])
for imagePath in paths.list_images(args["input"]):
	image = cv2.imread(imagePath)
	(h, w) = image.shape[:2]
	image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
	overlay = np.zeros((h, w, 4), dtype="uint8")
	overlay[h - wH - 10:h - 10, w - wW - 10:w - 10] = watermark
	output = image.copy()
	cv2.addWeighted(overlay, args["alpha"], output, 1.0, 0, output)
	filename = imagePath[imagePath.rfind(os.path.sep) + 1:]
	p = os.path.sep.join((args["output"], filename))
	cv2.imwrite(p, output)
	