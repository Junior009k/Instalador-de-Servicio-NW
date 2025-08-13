from FrontEnd.VariableDeterminadas import *

#Frame 12
# Variable de control
opcion = tk.StringVar(value="")
token=''
sucursales = ["1","2","3","4","5","6","7","8"]
labelVirtualQueue = tk.Label(frame37,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxVirtualQueue = tk.Entry(frame37)
labelUser = tk.Label(frame37,text="Introduzca el nombre del usuario",bg=colorframe5)
TextboxUser = tk.Entry(frame37)
labelPassword = tk.Label(frame37,text="Introduzca la contraseña del usuario",bg=colorframe5)
TextboxPassword = tk.Entry(frame37)
labelTypeDocument = tk.Label(frame37,text="Seleccione el tipo de documento",bg=colorframe5)
comboTypeDocument = ttk.Combobox(frame37,state="readonly",values=["Cedula", "Pasaporte", "RNC", "CED"])
labelNumberDocument = tk.Label(frame37,text="Introduzca el tipo de documento",bg=colorframe5)
TextboxNumberDocument = tk.Entry(frame37)
#place
TextboxVirtualQueue.place(x=40,y=80)
TextboxUser.place(x=40,y=120)
TextboxPassword.place(x=40,y=160)
comboTypeDocument.place(x=40,y=200)
TextboxNumberDocument.place(x=40,y=240)
labelVirtualQueue.place(x=40,y=60)
labelUser.place(x=40,y=100)
labelPassword.place(x=40,y=140)
labelTypeDocument.place(x=40,y=180)
labelNumberDocument.place(x=40,y=220)
#Config
def startingRequest():
   logging.info(f' {datetime.datetime.now() }: Se comienza a realizar la request a Virtual Queue')
   bandera=validateField(TextboxVirtualQueue,logging,MessageBox,"Virtual Queue","de la url",datetime)
   bandera=bandera*validateField(TextboxUser,logging,MessageBox,"Virtual Queue","del usuario",datetime)
   bandera=bandera*validateField(TextboxPassword,logging,MessageBox,"Virtual Queue","de la contraseña",datetime)
   bandera=bandera*validateField(comboTypeDocument,logging,MessageBox,"Virtual Queue","del tipo de documento",datetime)
   bandera=bandera*validateField(TextboxNumberDocument,logging,MessageBox,"Virtual Queue","del numero de documento",datetime)
   if(bandera):
         global token
         token=loginVirtualQueue(TextboxVirtualQueue.get(),TextboxUser.get(),TextboxPassword.get(),comboTypeDocument.get(),TextboxNumberDocument.get(),logging,datetime)
         #tk.messagebox.showinfo(title="Felicidades", message=f"{token}")
         global sucursales
         #sucursales=getAllOrganization(TextboxVirtualQueue.get(),token,logging,datetime)
         cleanRadioButton()
         #print(frame38.winfo_children())
         createSelectionOrganization(sucursales)
         #label38.config(text=sucursales) 
         show_frame(frame37,frame38)
         
def change():
   id,code=eval(opcion.get())[0],eval(opcion.get())[1]
   print(f"id sucursal:{id}, codigo sucursal:{code}")
   print(token)
   logging.info(f' {datetime.datetime.now() }:id sucursal:{id}, codigo sucursal:{code}')
   resp=getAllServiceByOrganization(TextboxVirtualQueue.get(),token,code,logging,datetime)
   print(f"respuest:{resp}")
   pass

def cleanRadioButton():
   for widget in frame38.winfo_children():
      if isinstance(widget, Radiobutton):  # Filtra solo los botones
         widget.destroy()

def createSelectionOrganization(sucursales):
   i=40
   #5,cantidad de líneas=sección.length/5,posicion=5*(inputUser-1<(cantidad de línea-1)))
   for sucursal in sucursales:
      print(sucursal)
      #Radiobutton(frame38,text=f"{sucursal['description']}", variable=opcion, value=str([f"{sucursal['id']}",f"{sucursal['code']}"]), bg=colorMenuservice, command=lambda: change()).place(x=0,y=i)
      Radiobutton(frame38,text=f"{sucursal}", variable=opcion, value=0, bg=colorMenuservice, command=lambda: change()).place(x=0,y=i)
      if(i==200):break
      i=40+i
      
        
