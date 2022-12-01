from tkinter import *
from tkinter import messagebox
import json
import os
FILE='sample.json'

listado = {}

try:
# Opening JSON file
    with open(FILE, 'r', encoding="utf-8") as openfile:
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

  #  nomVar.set(nomVar.get().lower())
   # apeVar.set(apeVar.get().lower())
    #matVar.set(matVar.get().lower())

    datos[(matVar.get().lower())]=notaVar.get()
    new_key= normalizar((apeVar.get()+nomVar.get()).lower())
    
    if not new_key in listado.keys():
        listado[new_key]={}
        listado[new_key]["Nombre"]=(nomVar.get().capitalize())
        listado[new_key]["Apellido"]=(apeVar.get().capitalize())
        listado[new_key]["Materias"]=[]
    listado[new_key]["Materias"].append(datos)

    print(f"Agregar {apeVar.get()}")
    print (listado)

def salir():
    print("Salir")
     
    result = json.dumps(listado, indent = 3)
    print(result)
    # Writing to sample.json
    with open(FILE, "w", encoding="utf-8") as outfile:
        outfile.write(result)
    quit()

def ventana_sec(lista, nombre, apellido):
    ventana=Tk()
    ventana.title(f"{apellido.upper()}, {nombre.upper()}")
    #ventana.title(f"{apeVar.get().upper()}, {nomVar.get().upper()}")
    
    listbox = Listbox(ventana, justify = "center",
                  width = 100,
                  bg = "grey",
                  activestyle = "dotbox",
                  font = "Arial",
                  fg = "black",
                  height = 20,
                  )                       
    
    listbox.pack(padx=10,pady=10,fill=BOTH, expand=True)

    for a in lista:
        for k, v in a.items():
            listbox.insert(END, f"{k.capitalize()}: {v}")

    listbox.pack()

# Solucionar mayúsculas y minúsculas. Como lo introduces, es como se muestra en la lista; se tienen que mostrar en mayúscula en la lista sin importar cómo se hayan agregado
# Centrar y jerarquización del nombre y apellido (ambos en mayus)
# Agregar enter
# No funciona el normalizador al consultar

def consultar():
    if apeVar.get()=="" or nomVar.get()=="":
        messagebox.showerror("ERROR", "Por favor, completar los campos obligatorios")
    
    else:
        new_key=normalizar(apeVar.get()+nomVar.get()).lower()
        if not new_key in listado.keys():
            messagebox.showerror("ERROR", "El alumno no se encuentra en el archivo")
        else:
            ventana_sec(listado[new_key]["Materias"], listado[new_key]["Nombre"], listado[new_key]["Apellido"])

def eliminar_info ():
    try:
        #os.remove(FILE)
        listado.clear()
        print("Se han eliminado exitosamente los datos")
    except:
        print("No hay datos para eliminar, se creará un nuevo listado")

Button(root, text="Agregar", width=20, command=agregar).grid(padx=10, pady=10, row=4, column=0)
Button(root, text="Salir", width=20, command=salir).grid(padx=10, pady=10, row=4, column=1)
Button(root, text="Consultar", width=45, command=consultar).grid(padx=10, pady=10, row=5, columnspan=2)
Button(root, text="Eliminar información", width=45, command=eliminar_info).grid(padx=10, pady=10, row=6, columnspan=2)

root.mainloop()
