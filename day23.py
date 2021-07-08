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


#Create two browse button and place the .pdf file for the buttons and create a merge pdf option -  Watermark Merger App

import tkinter as tk
from tkinter.filedialog import askopenfilename
from PyPDF2 import PdfFileMerger, PdfFileReader
from pathlib import Path
filelist = []
merger = PdfFileMerger()
def open_file(files):
    filepath = askopenfilename(
        filetypes=[("PDF Files","*.pdf"), ("All Files", "*.*")]
    )
    if not(filepath and Path(filepath).exists()):
        return
    files.append(filepath)
    lbl_items["text"] = '\n'.join(str(f) for f in files)
    if len(files) >= 2 and btn_merge['state'] == "disabled":
        btn_merge["state"] = "normal"
def merge_pdfs(files):
    for f in files:
        merger.append(PdfFileReader(open(f, "rb")))  
    output_filename = ent_output_name.get()
    if not output_filename:
        output_filename = "Merged.pdf"
    elif ".pdf" not in output_filename:
        output_filename += ".pdf"
    merger.write(output_filename)
window = tk.Tk()
window.title("PDF_Merger")
window.geometry("600x600")
window.resizable(0,0)
fr_bg1 = tk.Frame(window, bd=3)
lbl_open = tk.Label(fr_bg1, text="Choose the PDFs to join: (2 and above)")
lbl_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_open = tk.Button(fr_bg1, text="Open file",bg='white', fg='yellow,font=('algerian', 16, 'bold') ,
                command=lambda: open_file(filelist))
btn_open.grid(row=1, column=0, sticky="ew", padx=5)
lbl_items = tk.Label(fr_bg1, text="")
lbl_items.grid(row=2, column=0, pady=5)
fr_bg1.pack()
fr_bg2 = tk.Frame(window, bd=3)
lbl_to_merge = tk.Label(fr_bg2, text="Merge selected files (in PDF)")
lbl_to_merge.grid(row=0, column=0, sticky="ew", padx="5", pady="5")
ent_output_name = tk.Entry(master=fr_bg2, width=7)
ent_output_name.grid(row=1, column=0, sticky="ew")
btn_merge = tk.Button(fr_bg2,bg='white',font=('algerian', 16, 'bold') ,
                text="Merge PDF",
                state="disabled",
                command=lambda: merge_pdfs(filelist))
btn_merge.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
fr_bg2.pack()
btn_exit = tk.Button(window, text="Exit", command=window.destroy, bd=2, bg='white', fg='yellow',font=('algerian', 16, 'bold') ,)
btn_exit.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.FALSE)
if __name__ == "__main__":
    window.mainloop()
