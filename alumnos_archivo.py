from tkinter import *
from tkinter import messagebox
import json

listado = {}

try:
# Opening JSON file
    with open('sample.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    #print(json_object)
    #print(type(json_object))
    listado = json_object
    print (listado)
except:
    print ("No se encuentra el archivo")


root = Tk()
root.title("ALUMNOS")

Label(root, text="Nombre:").grid( pady=5, row=0, column=0)
Label(root, text="Apellido:").grid(pady=5, row=1, column=0)
Label(root, text="Materia:").grid(pady=5, row=2, column=0)
Label(root, text="Nota:").grid( pady=5, row=3, column=0)

# Entry Nombre
nomVar = StringVar()
Entry(root, width=20, textvariable=nomVar).grid(padx=5, row=0, column=1)

# Entry Apellido
apeVar = StringVar()
Entry(root, width=20, textvariable=apeVar).grid(padx=5, row=1, column=1)

# Entry Materias
matVar = StringVar()
Entry(root, width=20, textvariable=matVar).grid(padx=5, row=2, column=1)

# Entry Notas
notaVar = StringVar()
Entry(root, width=20, textvariable=notaVar).grid(padx=5, row=3, column=1)


def normalizar(s):
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
    return s.translate(trans)

def agregar():
    global listado
    datos = {}

    nomVar.set(nomVar.get().lower())
    apeVar.set(apeVar.get().lower())
    matVar.set(matVar.get().lower())

    datos[normalizar(matVar.get())]=notaVar.get()
    
    if not apeVar.get()+nomVar.get() in listado.keys():
        listado[apeVar.get()+nomVar.get()]={}
        listado[apeVar.get()+nomVar.get()]["Nombre"]=normalizar(nomVar.get())
        listado[apeVar.get()+nomVar.get()]["Apellido"]=normalizar(apeVar.get())
        listado[apeVar.get()+nomVar.get()]["Materias"]=[]
    listado[apeVar.get()+nomVar.get()]["Materias"].append(datos)
    
    print(f"Agregar {apeVar.get()}")
    print (listado)

def salir():
    print("Salir")
     
    result = json.dumps(listado, indent = 3)
    print(result)
    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(result)
    quit()

def ventana_sec(lista):
    ventana=Tk()
    ventana.title(f"{apeVar.get().upper()}, {nomVar.get().upper()}")
    
    listbox = Listbox(ventana, justify = "center",
                  width = 100,
                  bg = "grey",
                  activestyle = "dotbox",
                  font = "Arial",
                  fg = "black"
                  height = 20,
                  upper = "listbox"
                  )                       

    for a in lista:
        for k, v in a.items():
            listbox.insert(END, f"{k}: {v}")

    listbox.pack()

# Solucionar mayúsculas y minúsculas. Como lo introduces, es como se muestra en la lista; se tienen que mostrar en mayúscula en la lista sin importar cómo se hayan agregado
# Centrar y jerarquización del nombre y apellido (ambos en mayus)
# Agregar enter

def consultar():
    if apeVar.get()=="" or nomVar.get()=="":
        messagebox.showerror("ERROR", "Por favor, completar los campos obligatorios")
    
    else:
        if not apeVar.get()+nomVar.get() in listado.keys():
            messagebox.showerror("ERROR", "El alumno no se encuentra en el archivo")
        else:
            ventana_sec(listado[apeVar.get()+nomVar.get()]["Materias"])

Button(root, text="Agregar", width=20, command=agregar).grid(padx=10, pady=10, row=4, column=0)
Button(root, text="Salir", width=20, command=salir).grid(padx=10, pady=10, row=4, column=1)
Button(root, text="Consultar", width=45, command=consultar).grid(padx=10, pady=10, row=5, columnspan=2)

root.mainloop()
