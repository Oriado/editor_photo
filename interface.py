import tkinter as tk
import cv2
import numpy as np
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
from editor import *

photo_orig = None
photo_backup = None
mitka = None
slider_yaskravist=None
slider_vysota=None
slider_shyryna=None
slider_kontrast=None
slider_sepia=None
slider_teplyi=None
slider_cholodnyi=None
slider_shum=None
slider_p=None
slider_vinet=None
frame_pravo=None


def vidkryty_photo():
    global photo_orig
    global photo_backup
    shliach = filedialog.askopenfilename()
    if shliach:
        photo_orig = zavantazhyty_photo(shliach)
        photo_backup = photo_orig
        pokazaty_photo(photo_backup)


def pokazaty_photo(photo):
    zobrazhenna = Image.fromarray(photo)
    zobrazhenna.thumbnail((frame_pravo.winfo_width(), frame_pravo.winfo_height()), Image.LANCZOS)
    tk_photo = ImageTk.PhotoImage(zobrazhenna)
    mitka.config(image=tk_photo)
    mitka.image = tk_photo        

def zastosuvaty_gray():
    global photo_orig
    photo_orig = gray_photo(photo_orig)
    pokazaty_photo(photo_orig)

def zastosuvaty_yaskravist():
    global photo_orig
    znachennya = slider_yaskravist.get()
    photo_orig = zminy_yaskravist(photo_backup, znachennya)
    pokazaty_photo(photo_orig)

def zastosuwaty_rozmir():
    if photo_orig is None:
        return
    znachennya_v = slider_vysota.get()
    znachennya_sh = slider_shyryna.get()
    result = zminy_rozmir(photo_orig, znachennya_sh, znachennya_v)
    pokazaty_photo(result)

def zastosuwaty_dzerkalo():
    global photo_orig
    photo_orig = dzerkalo(photo_orig)
    pokazaty_photo(photo_orig)


def zastosuvaty_nedatyv():
    global photo_orig
    photo_orig = negativ(photo_orig) 
    pokazaty_photo(photo_orig) 

def zastosuwaty_poverny():
    global photo_orig
    photo_orig = povernuty(photo_orig)
    pokazaty_photo(photo_orig) 

def zastosuvaty_kontrast():
    global photo_orig
    znachennya_k = slider_kontrast.get()
    photo_orig = zminy_kontrast(photo_backup, znachennya_k)
    pokazaty_photo(photo_orig)

def zastosuvaty_malunok():
    global photo_orig
    photo_orig = malunok(photo_orig)
    pokazaty_photo(photo_orig)   

def zastosuvaty_rozmyttya():
    global photo_orig
    photo_orig = rozmyttya(photo_orig)
    pokazaty_photo(photo_orig)

def zastosuvaty_piksel():
    global photo_orig
    photo_orig = piksel(photo_orig)
    pokazaty_photo(photo_orig)

def zastosuvaty_sepia():
    global photo_orig
    znachennya_sepia = slider_sepia.get()
    photo_orig = sepia(photo_backup, znachennya_sepia)
    pokazaty_photo(photo_orig)   

def zastosuvaty_krai():
    global photo_orig
    photo_orig = defect_krai(photo_orig)
    pokazaty_photo(photo_orig) 

def zastoruvaty_akvarel():
    global photo_orig
    photo_orig = akvarel(photo_orig)
    pokazaty_photo(photo_orig)

def zastosuvaty_emboss():
    global photo_orig
    photo_orig = emboss(photo_orig)
    pokazaty_photo(photo_orig)   

def zastosuvaty_teplyi():
    global photo_orig
    znachennya_t = slider_teplyi.get()
    photo_orig = teplyi_color(photo_backup, znachennya_t)
    pokazaty_photo(photo_orig)            

def zastosuvaty_cholodnyi():
    global photo_orig
    znachennya_ch = slider_cholodnyi.get()
    photo_orig = cholodnyi_color(photo_backup, znachennya_ch)
    pokazaty_photo(photo_orig) 

def zastosuvaty_shum():
    global photo_orig
    znachennya_sh = slider_shum.get()
    photo_orig = shum(photo_backup, znachennya_sh)
    pokazaty_photo(photo_orig)

def zastosuvaty_rizkist():
    global photo_orig
    photo_orig = rizkist(photo_orig)
    pokazaty_photo(photo_orig) 

def zastosuvaty_post():
    global photo_orig
    znachennya_p = slider_p.get()
    photo_orig = posteryzacja(photo_backup, znachennya_p) 
    pokazaty_photo(photo_orig)  

def zastosuvaty_vanetku():
    global photo_orig
    znachennya_vinet = slider_vinet.get()
    photo_orig = vinetka(photo_backup, znachennya_vinet)
    pokazaty_photo(photo_orig)             

def skynuty_filtry():
    global photo_orig 
    global photo_backup
    photo_orig = photo_backup
    pokazaty_photo(photo_orig)  

def zberehty_photo():
    shlyakh = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    if shlyakh:
        photo_zberezenia = cv2.cvtColor(photo_orig, cv2.COLOR_RGB2BGR)
        photo_zberezenia = np.uint8(photo_zberezenia)
        ext = shlyakh.split(".")[-1]
        _, buf = cv2.imencode(f".{ext}", photo_zberezenia)
        buf.tofile(shlyakh)

    
   
    

       