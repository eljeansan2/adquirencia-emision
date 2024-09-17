#Pantalla principal de programa
from tkinter import messagebox
from time import sleep
from tkinter import * 
from tkinter import ttk
from tkinter import Tk
import tkinter as tk
from tkinter import scrolledtext as st
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import filedialog
from Controlador import ControlLectura
import os


#variables globales

def __init__():venta.mainloop()
def fondoObjeto(objeto,fondo,x,y):
    canvas=Canvas(objeto,width=x,height=y)
    canvas.place(x=0,y=0)
    bg=canvas.create_image(0,0,image=fondo,anchor=tk.NW)
    return objeto
def converImagen(ruta,x,y):
    return ImageTk.PhotoImage((Image.open(ruta)).resize((x,y)))
def ventMensajeError(msg):
    popup = tk.Toplevel(venta)
    popup.wm_title("Excepción")
    popup.geometry("420x90+338+538")
    popup.grid_propagate(False)
    popup.overrideredirect(True)
    popup.resizable(width=False, height=False)
    popup.lift()
    label = ttk.Label(popup, text=msg, font=SEL_FIRST)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Ok", command = popup.destroy)
    B1.pack()
    popup.grab_set()
    popup.mainloop()
def crearBoton(idBoton,contenedor,dirX,dirY,fondo,funcion):
    def enter():#evento cuando entra a un boton
        contenedor.config(cursor="hand2")
    def leave():#evento cuando sale de un boton
        contenedor.config(cursor="")
    def on_leave():
        funcionEvento(funcion)
    idBoton=contenedor.create_image(dirX,dirY,image=fondo,tag='event')  
    contenedor.tag_bind('event',"<Enter>",lambda event: enter())
    contenedor.tag_bind('event',"<Leave>",lambda event: leave())
    contenedor.tag_bind(idBoton,"<Button-1>",lambda event: on_leave())
    return idBoton

def funcionEvento(evento):
    
    if(evento=="Validar"):
        
        
        #try:
            file=open("ProgramaT\Archivos\ArchivoListaTemporalCAMPOS.txt","w",encoding="utf-8")
            file.close()
            file2=open("ProgramaT\Archivos\ArchivoListaTemporalValidacion.txt","w",encoding="utf-8")
            file2.close()
            varRuta=boxRuta.get()
            varRuta=varRuta.replace("/","\\")
            ControlLectura.validarTodo(varRuta,combTip.get())
            
            
        #except Exception as e: messagebox.showerror("Error", f"Por favor ingrese correctamente la ruta: - {str(e)} -||")
    if(evento=="Lupa"):
        boxRuta.delete("0","end")
        boxRuta.insert(0,filedialog.askopenfilename(initialdir = varRuta1,title = "Seleccione archivo",filetypes = (("all files","*.*"),("text Files","*.txt"))))
    if(evento=="Cerrar"):venta.destroy()
    if(evento=="Niguno"):print("sin evento") 
def ignore_drag(event):
    pass
#ventana principal
venta=Tk()
venta.geometry("1000x500+330+180")
venta.title("Validacion de Archivo")
venta.grid_propagate(False)
venta.overrideredirect(False)
venta.bind("<B1-Motion>", ignore_drag)
venta.resizable(width=False, height=False)
varRuta=""
#imagenes
imgVenta=converImagen("ProgramaT\Imagenes\Pantalla.png",1000,500)
Pantalla=converImagen("ProgramaT\Imagenes\Pantalla.png",1000,500)
cerrar1=converImagen("ProgramaT\Imagenes\cerrar1.png",170,40)
cerrar2=converImagen("ProgramaT\Imagenes\cerrar2.png",170,40)
expor1=converImagen("ProgramaT\Imagenes\expor1.png",220,40)
expor2=converImagen("ProgramaT\Imagenes\expor2.png",220,40)
Resultado=converImagen("ProgramaT\Imagenes\Resultado.png",1000,500)
validar1=converImagen("ProgramaT\Imagenes\lidar1.png",180,40)
validar2=converImagen("ProgramaT\Imagenes\lidar2.png",180,40)
Cons1=converImagen("ProgramaT\Imagenes\Cons1.png",180,40)
Cons2=converImagen("ProgramaT\Imagenes\Cons2.png",180,40)    
lupa=converImagen("ProgramaT\Imagenes\lupa.png",39,30)   
#contenedorPrincipal
contenedor =Canvas(venta,width=1000,height=500) #cracion de la instanci
contenedor.place(x=-1,y=-1)#posicion en la columna y fila
bg=contenedor.create_image(0,0,image=Pantalla,anchor=tk.NW)
#texBox imputs de entrada
boxRuta= Entry(contenedor,width=15,border=0,font=("Roboto Cn",12))
boxRuta.place(x=180, y=300)
#comboBox
combTip= ttk.Combobox(contenedor,width=18,font=("Roboto Cn",12),background="white")
combTip.place(x=176, y=333)
opciones=[
    #///////////////////////////////////emision
    "Contabilidad Emision",
    "Proximas a Vencer Emision",
    "Domiciliaciones Emision",
    "Estampacion Emision",
    "Operaciones diarias a Comercios Emision",
    "Notificaciones Emision",
    "Devoluciones Emision",
    "Comunicaciones Emision",
    "Posiciones contrato Emision",
    "Extractos comercios Emision",
    "Operaciones diarias Emision",
    "Vigentes canceladas y amortizadas Emision",
    "Cuentas Baja Emision",
    "Tarifario Emision",
    "Bloqueos y desbloqueos Emision",
    "Posiciones a comercios Emision",
    #///////////////////////////////////adquirencia
    "Posicion Comercio",
    "Emisor Adquirente",
    "Pago Comercio",
    "Operaciones Diarias a comercios",
    "Contabilidad",
    "Posicion Contrato",
    "Interfaz Master",
    "Interfaz Visa",
    "INC. Visa",
    "INC. MasterCard",
    "INC. UnionPay",
    "ISO 2",
    "ISO 3",
    "COMBBO",
    "CTLBBO",
    "ADLBBO",
    "ATRBBO",
    "CCOBBO",
    "CCPBBO",
    "CPOBBO",
    "MCMBBO",
    "AUTORIZA"
]
combTip['values']=opciones
combTip.set("Posicion Comercio")
combTip.config(state="readonly")
#boton Validar
btnValidar=None; btnValidar=crearBoton(btnValidar,contenedor,280,400,validar1,"Validar")
btnexportar=None; btnexportar=crearBoton(btnexportar,contenedor,640,460,expor1,"Niguno")
btnConsulta=None; btnConsulta=crearBoton(btnConsulta,contenedor,845,460,Cons1,"Niguno")
btnCerrar=None; btnCerrar=crearBoton(btnCerrar,contenedor,850,93,cerrar1,"Cerrar")
btnBuscar=None; btnBuscar=crearBoton(btnBuscar,contenedor,350,307,lupa,"Lupa")
# contenedor de Resultados
varRuta1=str("/")
barraVert=Scrollbar(venta)  #barra de desplazamiento
barraVert.place(x=917,y=130,width=14,height=272)
barraHori=Scrollbar(venta,orient="horizontal")  #barra de desplazamiento
barraHori.place(x=440,y=416,width=470,height=13)
listaPresenta=Listbox(venta,yscrollcommand=barraVert.set,xscrollcommand=barraHori.set,font=("Roboto Cn",12)) #contenedor
listaPresenta.place(x=450,y=123,width=465,height=290)
listaPresenta.insert(END, "Por favor, seleccione un archivo")