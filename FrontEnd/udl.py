from FrontEnd.VariableDeterminadas import *

#Frame 3
labeldb = tk.Label(frame3,text="Introduzca el nombre del servidor ",bg=colorMenuudl)
Textboxdb = tk.Entry(frame3)
labelsrv = tk.Label(frame3,text="Introduzca el nombre de la base de datos",bg=colorMenuudl)
Textboxsrv = tk.Entry(frame3)
button4 = tk.Button(frame3,width=16,height=1, text="Diagnosticar", command=lambda: diagnose()).place(x="215",y="150")

#place
Textboxdb.place(x=40,y=240)
Textboxsrv.place(x=40,y=200)
labeldb.place(x=40,y=180)
labelsrv.place(x=40,y=220)

#esta funcion se encarga de modificar los UDLS
def modifyUDL():
  logging.info(f'{datetime.datetime.now()}: Se comienza a modificar los UDLS')
  bandera=validateField(Textboxdb,logging,MessageBox,"los UDLS","el nombre de la base de datos",datetime)
  bandera=bandera*validateField(Textboxsrv,logging,MessageBox,"los UDLS","del servidor de la base de datos",datetime)
  bandera=bandera*validateLabel(label3,logging,MessageBox,"los UDLS","la ruta",datetime)
  if(bandera):
    if(manageUDL(Textboxsrv.get(),Textboxdb.get(),label3.cget("text"),logging,datetime)):tk.messagebox.showinfo(title="Felicidades", message="Los udls se modificaron correctamente")

def diagnose():
  logging.info(f'{datetime.datetime.now()}: Se comienza a Diagnosticar')
  bandera=validateField(Textboxdb,logging,MessageBox,"El diagnostico","el nombre de la base de datos",datetime)
  bandera=bandera*validateField(Textboxsrv,logging,MessageBox,"El diagnostico","del servidor de la base de datos",datetime)
  if(bandera):
    if(validateConnection(Textboxsrv.get(),Textboxdb.get(),logging,datetime)):tk.messagebox.showinfo(title="Felicidades", message="Conexión a SQL Server exitosa.")

