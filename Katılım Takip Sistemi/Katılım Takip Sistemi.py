import cv2
import numpy as np
import face_recognition
import os
import datetime
from datetime import datetime
from PIL import ImageFont
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

button_width = 300
button_height = 45

fontsize = 20
font = ImageFont.truetype("arial.ttf", fontsize)

window = tk.Tk()
window.title("Bilgisayarlı Görme Kullanan Katılım Takip Sistemi")

window.geometry('1920x1080')
window.state('zoomed')
window.configure(background="#515151")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

def Resize_Image(image, maxsize):
    r1 = image.size[0] / maxsize[0]
    r2 = image.size[1] / maxsize[1]
    ratio = max(r1, r2)
    newsize = (int(image.size[0] / ratio), int(image.size[1] / ratio))
    image = image.resize(newsize, Image.ANTIALIAS)
    return image

kullaniciadi = Image.open("ikonlar/KullaniciAdi.png")
kullaniciadi = Resize_Image(kullaniciadi, [button_width, 100])
kullaniciadi = ImageTk.PhotoImage(kullaniciadi)

sifre = Image.open("ikonlar/Sifre.png")
sifre = Resize_Image(sifre, [button_width, 100])
sifre = ImageTk.PhotoImage(sifre)

yoklamalistesi = Image.open("ikonlar/Yoklamalistesi.png")
yoklamalistesi = Resize_Image(yoklamalistesi, [button_width, 100])
yoklamalistesi = ImageTk.PhotoImage(yoklamalistesi)

xlabels = 300

title = Image.open("ikonlar/title.png")
title = ImageTk.PhotoImage(title)

title_img = tk.Label(window, border=0, image=title, bg="#515151", activebackground="#515151")
title_img.place(x=-160, y=40)

lbl = tk.Label(window, border=0, image=kullaniciadi, bg="#515151", activebackground="#515151")
lbl.place(x=xlabels, y=200)

txt = tk.Entry(window, width=15, bg="#F1F0F0", fg="#5B5B5B", font=('Cambria', 20, ' bold '), justify=CENTER)
txt.place(x=700, y=205)

lbl2 = tk.Label(window, border=0, image=sifre, bg="#515151", activebackground="#515151")
lbl2.place(x=xlabels, y=300)

txt2 = tk.Entry(window, width=15, bg="#F1F0F0", fg="#5B5B5B", font=('Cambria', 20, ' bold '), justify=CENTER,show='*')
txt2.place(x=700, y=305)

lbl4 = tk.Label(window, border=0, image=yoklamalistesi, bg="#515151", activebackground="#515151")
lbl4.place(x=300, y=650)

def temizle1():
    txt.delete(0, 'end')

def temizle2():
    txt2.delete(0, 'end')

AsilIsim="mertcan"
AsilSifre="123"
def YoklamaAlma():
    Kullanici = txt.get()
    Sifre = txt2.get()
    num = 1

    if (Kullanici == AsilIsim and Sifre == AsilSifre):
        path = 'sinif'
        sinif = []
        personNames = []
        myList = os.listdir(path)
        for cu_img in myList:
            current_Img = cv2.imread(f'{path}/{cu_img}')
            sinif.append(current_Img)
            personNames.append(os.path.splitext(cu_img)[0])

        def faceEncodings(sinif):
            encodeList = []
            for img in sinif:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList

        encodeListKnown = faceEncodings(sinif)


        def attendance(name):
            with open('YoklamaListesi.csv', 'r+') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                if name not in nameList:
                    time_now = datetime.now()
                    tStr = time_now.strftime('%H:%M:%S')
                    dStr = time_now.strftime('%d/%m/%Y')
                    f.writelines(f'\n{name},{tStr},{dStr}')

            T.insert(tk.INSERT, myDataList)



        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)



        while True:

            ret, frame = cap.read()
            faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

            facesCurrentFrame = face_recognition.face_locations(faces)
            encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

            for encodeFace, facesLoc in zip(encodesCurrentFrame, facesCurrentFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    name = personNames[matchIndex].upper()
                    y1, x2, y2, x1 = facesLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    attendance(name)
                else:
                    y1, x2, y2, x1 = facesLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, 'ListedeYok', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            cv2.imshow('Webcam', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break
            cv2.imwrite('goruntuler\ ' + str(num) +'.'+'.jpg', frame)
            num = num + 1

        cap.release()
        cv2.destroyAllWindows()




    else:
        T.insert(tk.INSERT, "KULLANICI BULUNAMADI !")

yoklama = Image.open("ikonlar/Yoklama.png")
yoklama = Resize_Image(yoklama, [button_width, button_height])
yoklama = ImageTk.PhotoImage(yoklama)

temizle = Image.open("ikonlar/Temizle.png")
temizle = Resize_Image(temizle, [button_width, button_height])
temizle = ImageTk.PhotoImage(temizle)

xtemizle = 1100
temizleButton = tk.Button(window, command=temizle1, border=0, image=temizle, bg="#515151", activebackground="#515151")
temizleButton.place(x=xtemizle, y=200)
temizleButton2 = tk.Button(window, command=temizle2, border=0, image=temizle, bg="#515151", activebackground="#515151")
temizleButton2.place(x=xtemizle, y=300)

center_x = (window.winfo_screenwidth() - button_width) / 2
yoklamaImg = tk.Button(window, command=YoklamaAlma, border=0, image=yoklama, bg="#515151", activebackground="#515151")
yoklamaImg.place(x=center_x - 315, y=420)

frame1 = tk.Frame(window, width=300, height=20, bg='#ffffff',
                  borderwidth=1, relief="sunken")
s = tk.Scrollbar(frame1)
s.pack(side=RIGHT, fill=Y)
T = tk.Text(frame1, width=65, height=14, wrap="word",
            yscrollcommand=s.set,
            borderwidth=0, highlightthickness=0)
s.config(command=T.yview)
s.pack(side="right", fill="y")
T.pack(side="left", fill="both", expand=True)
frame1.place(x=650, y=550)

window.mainloop()