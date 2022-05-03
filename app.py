from select import select
import tkinter
from tkinter import filedialog, ttk, messagebox
from wsgiref.validate import validator


txt = "Para empezar selecciona la cantidad de cartas"



def etiqueta(a):
    for widgets in frameIm4.winfo_children():
        widgets.destroy()
    Label1A = tkinter.Label(frameIm4, text=a)
    Label1A.config(fg="black", bg="green", font=("broadway 15 "))
    Label1A.place(x=5,y=0)


juega = False
def adivinacion():

    txt = "Ahora piensa en una carta, no la olvides y selecciona en que grupo está"    
    etiqueta(txt)
    global juega, sel
    sel = 0
    juega = True
    print("Necesitara "+str(k)+" tiros")
    print("Jugara con "+str(n)+ " cartas")


def repartidor1(val):
    for widgets in frameIm1.winfo_children():
        widgets.destroy()
    for widgets in frameIm2.winfo_children():
        widgets.destroy()
    for widgets in frameIm3.winfo_children():
        widgets.destroy()
    x1 = 5
    y1 = 5
    x2 = 5
    y2 = 5
    x3 = 5
    y3 = 5
    primera = True
    segunda = False
    tercera = False
    for a in range(val):
        #'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4'
        carta = a            
        if primera == True:    
            carta = tkinter.Frame(frameIm1)
            carta.place(x=x1, y=y1)
            carta.config(bg="OliveDrab4")
            carta.config(width=100, height=120)
            carta.config(bd=10)
            carta.config(relief="ridge")
            alb = a+1
            c1.append(alb)
            Label3A = tkinter.Label(carta, text=alb)
            Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
            Label3A.place(x=0,y=0)
            primera = False
            segunda = True
            tercera = False
            x1 += 40
        
        elif segunda == True:
            carta = tkinter.Frame(frameIm2)
            carta.place(x=x2, y=y2)
            carta.config(bg="OliveDrab4")
            carta.config(width=100, height=120)
            carta.config(bd=10)
            carta.config(relief="ridge")
            alb = a+1
            c2.append(alb)
            Label3A = tkinter.Label(carta, text=alb)
            Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
            Label3A.place(x=0,y=0)
            primera = False
            segunda = False
            tercera = True
            x2 += 40
        elif tercera == True:
            carta = tkinter.Frame(frameIm3)
            carta.place(x=x3, y=y3)
            carta.config(bg="OliveDrab4")
            carta.config(width=100, height=120)
            carta.config(bd=10)
            carta.config(relief="ridge")
            alb = a+1
            c3.append(alb)
            Label3A = tkinter.Label(carta, text=alb)
            Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
            Label3A.place(x=0,y=0)
            primera = True
            segunda = False
            tercera = False
            x3 += 40

def repartidor(val):
    c1.clear()
    c2.clear()
    c3.clear()
    for widgets in frameIm1.winfo_children():
        widgets.destroy()
    for widgets in frameIm2.winfo_children():
        widgets.destroy()
    for widgets in frameIm3.winfo_children():
        widgets.destroy()
    x1 = 5
    y1 = 5
    x2 = 5
    y2 = 5
    x3 = 5
    y3 = 5
    primera = True
    segunda = False
    tercera = False
    for a in range(len(val)):
        carta = a            
        if primera == True:    
            carta = tkinter.Frame(frameIm1)
            carta.place(x=x1, y=y1)
            carta.config(bg="OliveDrab4")
            carta.config(width=100, height=120)
            carta.config(bd=10)
            carta.config(relief="ridge")
            alb = val[a]
            c1.append(alb)
            Label3A = tkinter.Label(carta, text=alb)
            Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
            Label3A.place(x=0,y=0)
            primera = False
            segunda = True
            tercera = False
            x1 += 40
        
        elif segunda == True:
            carta = tkinter.Frame(frameIm2)
            carta.place(x=x2, y=y2)
            carta.config(bg="OliveDrab4")
            carta.config(width=100, height=120)
            carta.config(bd=10)
            carta.config(relief="ridge")
            alb = val[a]
            c2.append(alb)
            Label3A = tkinter.Label(carta, text=alb)
            Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
            Label3A.place(x=0,y=0)
            primera = False
            segunda = False
            tercera = True
            x2 += 40
        elif tercera == True:
            carta = tkinter.Frame(frameIm3)
            carta.place(x=x3, y=y3)
            carta.config(bg="OliveDrab4")
            carta.config(width=100, height=120)
            carta.config(bd=10)
            carta.config(relief="ridge")
            alb = val[a]
            c3.append(alb)
            Label3A = tkinter.Label(carta, text=alb)
            Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
            Label3A.place(x=0,y=0)
            primera = True
            segunda = False
            tercera = False
            x3 += 40

def combobox_estado():
    global juega
    juega = False    
    txt = "Ahora pulsa jugar"
    etiqueta(txt)
    global v,n, k, c1,c2,c3
    v = comboReportes.get()
    n = 0
    k = 0 
    c1 = []
    c2 = []
    c3 = []
    if v == "9" :
        k = 1      
        repartidor1(int(v))
    elif v == "15":
        k = 2
        repartidor1(int(v))
    elif v == "21":
        k = 3
        repartidor1(int(v))
    elif v == "27":
        k = 4
        repartidor1(int(v))
    elif v == "33":
        k = 5
        repartidor1(int(v))
    elif v == "39":
        k = 6
        repartidor1(int(v))
    elif v == "45":
        k = 7
        repartidor1(int(v))
    elif v == "51":
        k = 8
        repartidor1(int(v))
    elif v == "57":
        k = 9
        repartidor1(int(v))
    elif v == "63":
        k = 10
        repartidor1(int(v))
    elif v == "69":
        k = 11
        repartidor1(int(v))
    elif v == "75":
        k = 12
        repartidor1(int(v))
    elif v == "81":
        k = 13
        repartidor1(int(v))
        


    n = 3*((2*k)+1)   

global sel
sel = 0

def monte1():        
    global sel,valor
    valor = []    
    if juega == True:
        
        txt = "Seleccióna de nuevo el grupo en el que se encuentra tu carta"
        etiqueta(txt)
        if v == "9" :
            if sel < 2:
                c2.extend(c1)
                c2.extend(c3)
                sel += 1  
                valor = c2.copy()
                repartidor(valor)
                if sel == 2:
                    pb = (len(valor)/2)-0.5
                    carta = valor[int(pb)]
                    txt = "Tu carta es: "+str(carta)
                    etiqueta(txt)
                    for widgets in frameIm1.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm2.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm3.winfo_children():
                        widgets.destroy()
                    x1 = 5
                    y1 = 5
                    carta = tkinter.Frame(frameIm1)
                    carta.place(x=x1, y=y1)
                    carta.config(bg="OliveDrab4")
                    carta.config(width=100, height=120)
                    carta.config(bd=10)
                    carta.config(relief="ridge")
                    alb = valor[int(pb)]
                    Label3A = tkinter.Label(carta, text=alb)
                    Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
                    Label3A.place(x=0,y=0)


                    
                else:
                    valor.clear                            

        elif v == "15" or v == "21" or v == "27":
            if sel < 3:
                c2.extend(c1)
                c2.extend(c3)
                sel += 1 
                valor = c2.copy()
                repartidor(valor)

                if sel == 3:
                    pb = (len(valor)/2)-0.5
                    carta = valor[int(pb)]
                    txt = "Tu carta es: "+str(carta)
                    etiqueta(txt)
                    for widgets in frameIm1.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm2.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm3.winfo_children():
                        widgets.destroy()
                    x1 = 5
                    y1 = 5
                    carta = tkinter.Frame(frameIm1)
                    carta.place(x=x1, y=y1)
                    carta.config(bg="OliveDrab4")
                    carta.config(width=100, height=120)
                    carta.config(bd=10)
                    carta.config(relief="ridge")
                    alb = valor[int(pb)]
                    Label3A = tkinter.Label(carta, text=alb)
                    Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
                    Label3A.place(x=0,y=0)

                else:
                    valor.clear                

        elif v == "33" or v == "39" or v == "45" or v == "51" or v == "57"or v == "63" or v == "69" or v == "75" or v == "81":
            if sel < 4:
                c2.extend(c1)
                c2.extend(c3)
                sel += 1 
                valor = c2.copy()
                repartidor(valor)              

                if sel == 4:
                    pb = (len(valor)/2)-0.5
                    carta = valor[int(pb)]
                    txt = "Tu carta es: "+str(carta)
                    etiqueta(txt)
                    for widgets in frameIm1.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm2.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm3.winfo_children():
                        widgets.destroy()
                    x1 = 5
                    y1 = 5
                    carta = tkinter.Frame(frameIm1)
                    carta.place(x=x1, y=y1)
                    carta.config(bg="OliveDrab4")
                    carta.config(width=100, height=120)
                    carta.config(bd=10)
                    carta.config(relief="ridge")
                    alb = valor[int(pb)]
                    Label3A = tkinter.Label(carta, text=alb)
                    Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
                    Label3A.place(x=0,y=0)

                else:
                    valor.clear 

        

def monte2():
    global sel,valor
    valor = [] 
    if juega == True:
        txt = "Seleccióna de nuevo el grupo en el que se encuentra tu carta"
        etiqueta(txt)

        if v == "9" :
            if sel < 2:
                c1.extend(c2)
                c1.extend(c3)
                sel += 1  
                valor = c1.copy()
                repartidor(valor)
                if sel == 2:
                    pb = (len(valor)/2)-0.5
                    carta = valor[int(pb)]
                    txt = "Tu carta es: "+str(carta)
                    etiqueta(txt)
                    for widgets in frameIm1.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm2.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm3.winfo_children():
                        widgets.destroy()
                    x1 = 5
                    y1 = 5
                    carta = tkinter.Frame(frameIm1)
                    carta.place(x=x1, y=y1)
                    carta.config(bg="OliveDrab4")
                    carta.config(width=100, height=120)
                    carta.config(bd=10)
                    carta.config(relief="ridge")
                    alb = valor[int(pb)]
                    Label3A = tkinter.Label(carta, text=alb)
                    Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
                    Label3A.place(x=0,y=0)

                else:
                    valor.clear  

        elif v == "15" or v == "21" or v == "27":
            if sel < 3:
                c1.extend(c2)
                c1.extend(c3)
                sel += 1 
                valor = c1.copy()
                repartidor(valor)
                if sel == 3:
                    pb = (len(valor)/2)-0.5
                    carta = valor[int(pb)]
                    txt = "Tu carta es: "+str(carta)
                    etiqueta(txt)
                    for widgets in frameIm1.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm2.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm3.winfo_children():
                        widgets.destroy()
                    x1 = 5
                    y1 = 5
                    carta = tkinter.Frame(frameIm1)
                    carta.place(x=x1, y=y1)
                    carta.config(bg="OliveDrab4")
                    carta.config(width=100, height=120)
                    carta.config(bd=10)
                    carta.config(relief="ridge")
                    alb = valor[int(pb)]
                    Label3A = tkinter.Label(carta, text=alb)
                    Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
                    Label3A.place(x=0,y=0)

                else:
                    valor.clear

        elif v == "33" or v == "39" or v == "45" or v == "51" or v == "57"or v == "63" or v == "69" or v == "75" or v == "81":
            if sel < 4:
                c1.extend(c2)
                c1.extend(c3)
                sel += 1 
                valor = c1.copy()
                repartidor(valor)
                if sel == 4:
                    pb = (len(valor)/2)-0.5
                    carta = valor[int(pb)]
                    txt = "Tu carta es: "+str(carta)
                    etiqueta(txt)
                    for widgets in frameIm1.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm2.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm3.winfo_children():
                        widgets.destroy()
                    x1 = 5
                    y1 = 5
                    carta = tkinter.Frame(frameIm1)
                    carta.place(x=x1, y=y1)
                    carta.config(bg="OliveDrab4")
                    carta.config(width=100, height=120)
                    carta.config(bd=10)
                    carta.config(relief="ridge")
                    alb = valor[int(pb)]
                    Label3A = tkinter.Label(carta, text=alb)
                    Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
                    Label3A.place(x=0,y=0)

                else:
                    valor.clear 

def monte3():
    global sel,valor
    valor = [] 
    if juega == True:
        txt = "Seleccióna de nuevo el grupo en el que se encuentra tu carta"
        etiqueta(txt)    
        if v == "9" :
            if sel < 2:
                c1.extend(c3)
                c1.extend(c2)
                sel += 1  
                valor = c1.copy()
                repartidor(valor)
                if sel == 2:
                    pb = (len(valor)/2)-0.5
                    carta = valor[int(pb)]
                    txt = "Tu carta es: "+str(carta)
                    etiqueta(txt)
                    for widgets in frameIm1.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm2.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm3.winfo_children():
                        widgets.destroy()
                    x1 = 5
                    y1 = 5
                    carta = tkinter.Frame(frameIm1)
                    carta.place(x=x1, y=y1)
                    carta.config(bg="OliveDrab4")
                    carta.config(width=100, height=120)
                    carta.config(bd=10)
                    carta.config(relief="ridge")
                    alb = valor[int(pb)]
                    Label3A = tkinter.Label(carta, text=alb)
                    Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
                    Label3A.place(x=0,y=0)

                else:
                    valor.clear  

        elif v == "15" or v == "21" or v == "27":
            if sel < 3:
                c1.extend(c3)
                c1.extend(c2)
                sel += 1 
                valor = c1.copy()
                repartidor(valor)
                if sel == 3:
                    pb = (len(valor)/2)-0.5
                    carta = valor[int(pb)]
                    txt = "Tu carta es: "+str(carta)
                    etiqueta(txt)
                    for widgets in frameIm1.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm2.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm3.winfo_children():
                        widgets.destroy()
                    x1 = 5
                    y1 = 5
                    carta = tkinter.Frame(frameIm1)
                    carta.place(x=x1, y=y1)
                    carta.config(bg="OliveDrab4")
                    carta.config(width=100, height=120)
                    carta.config(bd=10)
                    carta.config(relief="ridge")
                    alb = valor[int(pb)]
                    Label3A = tkinter.Label(carta, text=alb)
                    Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
                    Label3A.place(x=0,y=0)

                else:
                    valor.clear

        elif v == "33" or v == "39" or v == "45" or v == "51" or v == "57"or v == "63" or v == "69" or v == "75" or v == "81":
            if sel < 4:
                c1.extend(c3)
                c1.extend(c2)
                sel += 1 
                valor = c1.copy()
                repartidor(valor)
                if sel == 4:
                    pb = (len(valor)/2)-0.5
                    carta = valor[int(pb)]
                    txt = "Tu carta es: "+str(carta)
                    etiqueta(txt)
                    for widgets in frameIm1.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm2.winfo_children():
                        widgets.destroy()
                    for widgets in frameIm3.winfo_children():
                        widgets.destroy()
                    x1 = 5
                    y1 = 5
                    carta = tkinter.Frame(frameIm1)
                    carta.place(x=x1, y=y1)
                    carta.config(bg="OliveDrab4")
                    carta.config(width=100, height=120)
                    carta.config(bd=10)
                    carta.config(relief="ridge")
                    alb = valor[int(pb)]
                    Label3A = tkinter.Label(carta, text=alb)
                    Label3A.config(fg="black", bg="DarkOliveGreen4", font=("broadway 12 bold"))
                    Label3A.place(x=0,y=0)

                else:
                    valor.clear 


   

ventana = tkinter.Tk()
ventana.title("Adivinación de cartas")
ventana.geometry("1500x850")
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Frames ---------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
frame = tkinter.Frame(ventana)
# Establece la posición del componente
frame.place(x=35, y=85)
# Color de fondo, background
frame.config(bg="lightgreen")
# Podemos establecer un tamaño
frame.config(width=1400, height=720)
# Establece el ancho del borde
frame.config(bd=10)
# Establece el tipo de relieve para el borde
frame.config(relief="ridge")

frameAr = tkinter.Frame(ventana)
# Establece la posición del componente
frameAr.place(x=35, y=10)
# Color de fondo, background
frameAr.config(bg="lightgreen")
# Podemos establecer un tamaño
frameAr.config(width=400, height=60)
# Establece el ancho del borde
frameAr.config(bd=10)
# Establece el tipo de relieve para el borde
frameAr.config(relief="ridge")

frameBu = tkinter.Frame(ventana)
# Establece la posición del componente
frameBu.place(x=450, y=15)
# Color de fondo, background
frameBu.config(bg="lightgreen")
# Podemos establecer un tamaño
frameBu.config(width=410, height=60)
# Establece el ancho del borde
frameBu.config(bd=10)
# Establece el tipo de relieve para el borde
frameBu.config(relief="ridge")


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Labels ---------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

frameIm1 = tkinter.Frame(frame)
# Establece la posición del componente
frameIm1.place(x=20, y=60)
# Color de fondo, background
frameIm1.config(bg="green")
# Podemos establecer un tamaño
frameIm1.config(width=1350, height=200)
# Establece el ancho del borde
frameIm1.config(bd=10)
# Establece el tipo de relieve para el borde
frameIm1.config(relief="ridge")

frameIm2 = tkinter.Frame(frame)
# Establece la posición del componente
frameIm2.place(x=20, y=270)
# Color de fondo, background
frameIm2.config(bg="green")
# Podemos establecer un tamaño
frameIm2.config(width=1350, height=200)
# Establece el ancho del borde
frameIm2.config(bd=10)
# Establece el tipo de relieve para el borde
frameIm2.config(relief="ridge")

frameIm3 = tkinter.Frame(frame)
# Establece la posición del componente
frameIm3.place(x=20, y=480)
# Color de fondo, background
frameIm3.config(bg="green")
# Podemos establecer un tamaño
frameIm3.config(width=1350, height=200)
# Establece el ancho del borde
frameIm3.config(bd=10)
# Establece el tipo de relieve para el borde
frameIm3.config(relief="ridge")

frameIm4 = tkinter.Frame(frame)
# Establece la posición del componente
frameIm4.place(x=20, y=5)
# Color de fondo, background
frameIm4.config(bg="green")
# Podemos establecer un tamaño
frameIm4.config(width=1350, height=50)
# Establece el ancho del borde
frameIm4.config(bd=10)
# Establece el tipo de relieve para el borde
frameIm4.config(relief="ridge")


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Labels ---------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------




"""Label1 = tkinter.Label(frameInfo, text="Canción")
    Label1.config(fg="white", bg="grey", font=("broadway 18 bold"))
    Label1.place(x=10,y=40)

    CANCION = "VALOR"

    Label1A = tkinter.Label(frameInfo, text=CANCION)
    Label1A.config(fg="white", bg="grey", font=("broadway 15 "))
    Label1A.place(x=150,y=45)

    Label2 = tkinter.Label(frameInfo, text="Artista")
    Label2.config(fg="white", bg="grey", font=("broadway 18 bold"))
    Label2.place(x=10,y=90)

    ARTISTA = "VALOR2"

    Label2A = tkinter.Label(frameInfo, text=ARTISTA)
    Label2A.config(fg="white", bg="grey", font=("broadway 15"))
    Label2A.place(x=150,y=95)

    Label3 = tkinter.Label(frameInfo, text="Album")
    Label3.config(fg="white", bg="grey", font=("broadway 18 bold"))
    Label3.place(x=10,y=140)

    ALBUM = "VALOR3"

    Label3A = tkinter.Label(frameInfo, text=ALBUM)
    Label3A.config(fg="white", bg="grey", font=("broadway 15"))
    Label3A.place(x=150,y=145)"""

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Buttons --------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


def hola():
    print("Hola Mundo")

boton1 = tkinter.Button(frameAr, text="Jugar", fg="white", font=(
    "broadway 12 bold"), command=adivinacion, borderwidth=0, bg="green")
boton1.place(x=40, y=5)
boton1.config(width=25, height=1)

Label1A = tkinter.Label(frameIm4, text=txt)
Label1A.config(fg="black", bg="green", font=("broadway 15 "))
Label1A.place(x=5,y=0)

boton3 = tkinter.Button(ventana, text="Seleccionar", fg="black", font=(
    "broadway 12 bold"), command=combobox_estado, borderwidth=0, bg="lightgreen")
boton3.place(x=730, y=10)
boton3.config(width=12, height=1)
boton3.config(bd=10)
# Establece el tipo de relieve para el borde
boton3.config(relief="ridge")


boton4 = tkinter.Button(frame, text="Seleccionar", fg="black", font=(
    "broadway 12 bold"), command=monte1, borderwidth=0, bg="lightgreen")
boton4.place(x=1210, y=180)
boton4.config(width=10, height=1)
boton4.config(bd=10)
# Establece el tipo de relieve para el borde
boton4.config(relief="ridge")

boton5 = tkinter.Button(frame, text="Seleccionar", fg="black", font=(
    "broadway 12 bold"), command=monte2, borderwidth=0, bg="lightgreen")
boton5.place(x=1210, y=390)
boton5.config(width=10, height=1)
boton5.config(bd=10)
# Establece el tipo de relieve para el borde
boton5.config(relief="ridge")

boton6 = tkinter.Button(frame, text="Seleccionar", fg="black", font=(
    "broadway 12 bold"), command=monte3, borderwidth=0, bg="lightgreen")
boton6.place(x=1210, y=600)
boton6.config(width=10, height=1)
boton6.config(bd=10)
# Establece el tipo de relieve para el borde
boton6.config(relief="ridge")
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Combobox --------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


comboReportes = ttk.Combobox(frameBu,state="readonly", values=[
    "9","15","21","27","33","39","45","51","57","63","69","75","81"], font=("broadway 12 bold"))
comboReportes.grid(column=0, row=1)
comboReportes.current(0)
comboReportes.config(width=20, height=10)



# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------- Entry ---------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

ventana.config(cursor="arrow")
ventana.config(bg="green")
ventana.config(bd=15)
ventana.config(relief="ridge")
ventana.mainloop()


