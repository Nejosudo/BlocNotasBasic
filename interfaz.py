from tkinter import *
from tkinter import filedialog, messagebox
import speech_recognition as sr
import os

class mainAplication():
    def __init__(self):
        self.root = Tk() 
        self.root.geometry("600x400+400+180")
        self.root.title("Bloc notas")
        self.widgets()
        self.current_file = None  # Indica que el archivo no existe
        self.changes_save = True # Para saber si un archivo tiene los datos guardados.

        self.root.protocol("WM_DELETE_WINDOW", self.onClose) # Personalizar el cierre de la ventana

    def widgets(self):
        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)

        self.archivo_menu = Menu(self.menuBar, tearoff=0)
        self.archivo_menu.add_command(label="New", command=self.newWindow, accelerator='CTRL+N')
        self.archivo_menu.add_command(label="Save", command=self.saveNote, accelerator='CTRL+S')
        #self.archivo_menu.add_command(label="Peech to text", command=self.peechToText)

        self.root.bind_all('<Control-n>', self.newWindow)
        self.root.bind_all('<Control-s>', self.saveNote)

        self.menuBar.add_cascade(label="Archivo", menu=self.archivo_menu)

        self.entrada = Text(self.root)
        self.entrada.pack()
        self.entrada.bind("<Key>", self.modify) # Cada tecla generara una modificacion cambiando el estado de no guardado

    def newWindow(self, event=None):
        app = mainAplication()
        app.run()

    def saveNote(self, event=None):
        # Verificador si el archivo ya existe o no antes de guardar los cambios.
        if self.current_file is None or not os.path.exists(self.current_file):
            # Obtener la ruta de archivo seleccionada por el usuario
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")

            # Guardar la nota en el archivo seleccionado
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(self.entrada.get("1.0", "end-1c"))
                self.current_file = file_path
                self.changes_save = True
                self.root.title(os.path.basename(file_path))
        else:
            # Actualizar el archivo existente
            with open(self.current_file, 'w') as file:
                file.write(self.entrada.get("1.0", "end-1c"))
            self.changes_save = True


    def onClose(self): # Ventana emergente personalizar cierre de ventana
        if not self.changes_save:
            message = messagebox.askyesnocancel("Guardar cambios", "¿Desea guardar los cambios antes de salir?") 
            if message is None:
                return
            elif message:
                self.saveNote()
        self.root.destroy()

    def modify(self, event=None):
        self.changes_save = False # No guardado

    def run(self):
        self.root.mainloop()
        
if __name__ == '__main__':
    app = mainAplication()
    app.run()
