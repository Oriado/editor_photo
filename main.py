import tkinter as tk
import interface
from interface import *

vikno = tk.Tk()
vikno.title("Редактор фото")
vikno.state("zoomed")

canvas = tk.Canvas(vikno, width=110)
canvas.pack(side=tk.LEFT, fill=tk.Y)
scroll = tk.Scrollbar(vikno, orient=tk.VERTICAL, command=canvas.yview)
scroll.pack(side=tk.LEFT, fill=tk.Y)

canvas.configure(yscrollcommand=scroll.set)

frame_livo = tk.Frame(canvas)
canvas.create_window((0,0), window=frame_livo, anchor=tk.NW)
frame_livo.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

frame_pravo = tk.Frame(vikno)
frame_pravo.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

interface.frame_pravo = frame_pravo

mitka = tk.Label(frame_pravo)
mitka.pack()
interface.mitka = mitka

btn0=tk.Button(frame_livo, text="Відкрити фото", command=vidkryty_photo)
btn0.pack(anchor=tk.W)

btn1=tk.Button(frame_livo, text="Чорно-біле", command=zastosuvaty_gray)
btn1.pack(anchor=tk.W)

# btn2=tk.Button(frame_livo, text="Яскравість", command=zastosuvaty_yaskravist)
# btn2.pack(anchor=tk.W)

# btn3=tk.Button(frame_livo, text="Розмір", command=zastosuwaty_rozmir)
# btn3.pack(anchor=tk.W)

btn6=tk.Button(frame_livo, text="Дзеркало", command=zastosuwaty_dzerkalo)
btn6.pack(anchor=tk.W)

btn8=tk.Button(frame_livo, text="Поворот", command=zastosuwaty_poverny)
btn8.pack(anchor=tk.W)

btn7=tk.Button(frame_livo, text="Негатив", command=zastosuvaty_nedatyv)
btn7.pack(anchor=tk.W)


# btn8=tk.Button(frame_livo, text="Контраст", command=zastosuvaty_kontrast)
# btn8.pack(anchor=tk.W)

btn9=tk.Button(frame_livo, text="Малюнок", command=zastosuvaty_malunok)
btn9.pack(anchor=tk.W)

btn10=tk.Button(frame_livo, text="Розмиття", command=zastosuvaty_rozmyttya)
btn10.pack(anchor=tk.W)

btn11=tk.Button(frame_livo, text="Пікселі", command=zastosuvaty_piksel)
btn11.pack(anchor=tk.W)

# btn12=tk.Button(frame_livo, text="Сепія", command=zastosuvaty_sepia)
# btn12.pack(anchor=tk.W)

btn12=tk.Button(frame_livo, text="Виївлення країв",command=zastosuvaty_krai)
btn12.pack(anchor=tk.W)

btn13=tk.Button(frame_livo, text="Акварель", command=zastoruvaty_akvarel)
btn13.pack(anchor=tk.W)

btn14=tk.Button(frame_livo, text="Метал", command=zastosuvaty_emboss)
btn14.pack(anchor=tk.W)

btn15=tk.Button(frame_livo, text="Різкість", command=zastosuvaty_rizkist)
btn15.pack(anchor=tk.W)

btn4=tk.Button(frame_livo, text="Скинути фільтри", command=skynuty_filtry)
btn4.pack(anchor=tk.W)

btn5=tk.Button(frame_livo, text="Зберегти фото", command=zberehty_photo)
btn5.pack(anchor=tk.W)

slider_yaskravist= tk.Scale(frame_livo,label ="Яскравість", from_=-50, to=50, orient=tk.HORIZONTAL, command=lambda x: zastosuvaty_yaskravist())
slider_yaskravist.pack(anchor=tk.W)

slider_vysota=tk.Scale(frame_livo,label = "Розмір вертикалі", from_=100, to=1080, orient=tk.HORIZONTAL, command=lambda x: zastosuwaty_rozmir())
slider_vysota.set(600)
slider_vysota.pack(anchor=tk.W)

slider_shyryna=tk.Scale(frame_livo,label = "Розмір горизонталі", from_=100, to=1920, orient=tk.HORIZONTAL, command=lambda x: zastosuwaty_rozmir())
slider_shyryna.set(800)
slider_shyryna.pack(anchor=tk.W)

slider_kontrast=tk.Scale(frame_livo,label = "Контраст", from_=0.1, to=3, resolution=0.1, orient=tk.HORIZONTAL, command=lambda x: zastosuvaty_kontrast())
slider_kontrast.pack(anchor=tk.W)

slider_sepia=tk.Scale(frame_livo,label = "Сепія", from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=lambda x: zastosuvaty_sepia())
slider_sepia.pack(anchor=tk.W)

slider_teplyi=tk.Scale(frame_livo,label = "Теплий відтінок", from_=0, to=50, resolution=0.1, orient=tk.HORIZONTAL, command=lambda x: zastosuvaty_teplyi())
slider_teplyi.pack(anchor=tk.W)

slider_cholodnyi=tk.Scale(frame_livo,label = "Холодний відтінок", from_=0, to=50, resolution=0.1, orient=tk.HORIZONTAL, command=lambda x: zastosuvaty_cholodnyi())
slider_cholodnyi.pack(anchor=tk.W)

slider_shum=tk.Scale(frame_livo,label = "Шум", from_=0, to=100, resolution=0.1, orient=tk.HORIZONTAL, command=lambda x: zastosuvaty_shum())
slider_shum.pack(anchor=tk.W)

slider_p=tk.Scale(frame_livo,label = "Пастерізація", from_=1, to=64, resolution=0.1, orient=tk.HORIZONTAL, command=lambda x: zastosuvaty_post())
slider_p.pack(anchor=tk.W)

slider_vinet=tk.Scale(frame_livo,label = "Вінетка", from_=0.1, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=lambda x: zastosuvaty_vanetku())
slider_vinet.pack(anchor=tk.W)

interface.slider_yaskravist = slider_yaskravist
interface.slider_vysota = slider_vysota
interface.slider_shyryna = slider_shyryna
interface.slider_kontrast = slider_kontrast
interface.slider_sepia = slider_sepia
interface.slider_teplyi=slider_teplyi
interface.slider_cholodnyi=slider_cholodnyi
interface.slider_shum = slider_shum
interface.slider_p=slider_p
interface.slider_vinet=slider_vinet

vikno.mainloop()