from FrontEnd.VariableDeterminadas import *


#esta funcion se encarga de modificar los puertos de e-Flow 
def modifyPort():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  los puertos')
  bandera=validateField(TextboxPortURL,logging,MessageBox,"los puertos","la url",datetime)
  bandera=bandera*validateField(TextboxPort,logging,MessageBox,"los puertos","el numero del puerto",datetime)
  bandera=bandera*validateLabel(label4,logging,MessageBox,"los puertos","la ruta",datetime)
  if( validateDirectory(label4.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label9.cget("text"),"FrontEnd",logging,datetime)):label9.config(text="") 
  bandera=bandera*validateLabel(label4,logging,MessageBox,"los puertos","tiene que estar en la carpeta del aplicativo",datetime)
  if(bandera):
    if( validateDirectory(label4.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label9.cget("text"),"FrontEnd",logging,datetime)):label9.config(text="") 
    bandera=bandera*validateLabel(label4,logging,MessageBox,"los puertos","recuerda que debe tener 3 numeros",datetime)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de los puertos')
    changePort(label4.cget("text"),TextboxPort.get(),TextboxPortURL.get(),logging,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="Los Puertos se modificaron correctamente")

#esta funcion se encarga de modificar los puertos de e-Flow 
def modifyPortAppointment():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  los puertos de citas')
  print(f"{TextboxPortAppointment.get()}")
  print(label30.cget("text"))
  bandera=validateField(TextboxPortURLAppointment,logging,MessageBox,"los puertos","la url",datetime)
  bandera=bandera*validateField(TextboxPortAppointment,logging,MessageBox,"los puertos","el numero del puerto",datetime)
  bandera=bandera*validateLabel(label30,logging,MessageBox,"los puertos","la ruta",datetime)
  if( validateDirectory(label30.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label30.cget("text"),"FrontEnd",logging,datetime)):label30.config(text="") 
  bandera=bandera*validateLabel(label30,logging,MessageBox,"los puertos","tiene que estar en la carpeta del aplicativo",datetime)
  if(bandera):
    if( validateDirectory(label30.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label30.cget("text"),"FrontEnd",logging,datetime)):label30.config(text="") 
    bandera=bandera*validateLabel(label30,logging,MessageBox,"los puertos","recuerda que debe tener 3 numeros",datetime)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de los puertos')
    changePortAppointment(label30.cget("text"),TextboxPortAppointment.get(),TextboxPortURLAppointment.get(),logging,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="Los Puertos se modificaron correctamente")
