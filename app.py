import tkinter
from tkinter import filedialog, ttk, messagebox
# --------------------------------------------------------- XML --------------------------------------------------------


ventana = tkinter.Tk()
ventana.title("Adivinación de cartas")
ventana.geometry("1100x700")
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
frame.config(width=1000, height=550)
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

frameIm = tkinter.Frame(frame)
# Establece la posición del componente
frameIm.place(x=20, y=20)
# Color de fondo, background
frameIm.config(bg="green")
# Podemos establecer un tamaño
frameIm.config(width=940, height=490)
# Establece el ancho del borde
frameIm.config(bd=10)
# Establece el tipo de relieve para el borde
frameIm.config(relief="ridge")

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

def combobox_estado():
    if comboReportes.get()=="Reporte de tokens":
        "rep_token()"
    elif comboReportes.get()=="Reporte de errores":
        "rep_error()"
    elif comboReportes.get()=="Manual de Usuario":
        print("Manual de Usuario")
    elif comboReportes.get()=="Manual Técnico":
        print("Manual Técnico")

boton1 = tkinter.Button(frameAr, text="Jugar", fg="white", font=(
    "broadway 12 bold"), command=hola, borderwidth=0, bg="green")
boton1.place(x=25, y=5)
boton1.config(width=12, height=1)

boton2 = tkinter.Button(frameAr, text="Analizar", fg="white", font=(
    "broadway 12 bold"), command=hola, borderwidth=0, bg="green")
boton2.place(x=205, y=5)
boton2.config(width=12, height=1)

boton3 = tkinter.Button(ventana, text="Seleccionar", fg="black", font=(
    "broadway 12 bold"), command=combobox_estado, borderwidth=0, bg="lightgreen")
boton3.place(x=730, y=10)
boton3.config(width=12, height=1)
boton3.config(bd=10)
# Establece el tipo de relieve para el borde
boton3.config(relief="ridge")

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------ Combobox --------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

comboReportes = ttk.Combobox(frameBu,state="readonly", values=[
    "9","81"], font=("broadway 12 bold"))
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
