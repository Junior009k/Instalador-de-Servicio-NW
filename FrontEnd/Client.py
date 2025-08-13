from FrontEnd.VariableDeterminadas import *

#Se encarga de instalar los dll de la impresora
def startingInstallDLL():
  logging.info(f' {datetime.datetime.now() }: Se comienza a ejecutar la funcion startingInstallDLL')
  bandera=validateLabel(label23,logging,MessageBox,"los dll","la ruta",datetime)
  if(bandera):
    if(installDLL(label23.cget("text"),logging,datetime)):tk.messagebox.showinfo(title="Felicidades", message="Los udls se modificaron correctamente")

#Se encarga de configurar las opciones de internet
def startingconfigureOptionInternet():
  logging.info(f' {datetime.datetime.now() }: Se comienza a ejecutar la funcion startingconfigureOptionInternet')
  bandera=validateField(TextboxsvrIO,logging,MessageBox,"los startingconfigureOptionInternet","el nombre del servidor",datetime)
  if(bandera):
    if(manageInternetOption(TextboxsvrIO.get(),logging,datetime)):tk.messagebox.showinfo(title="Felicidades", message="Los udls se modificaron correctamente")

#Se encarga de configurar los permisos de internet
def startingconfigureAutoplaylist():
  logging.info(f' {datetime.datetime.now() }: Se comienza a ejecutar la funcion startingconfigureAutoplaylist')
  bandera=validateField(TextboxUrlEflow,logging,MessageBox,"los startingconfigureAutoplaylist","el nombre de la url de e-Flow",datetime)
  if(bandera):
    if(autoplaylist(TextboxUrlEflow.get(),logging,datetime)):tk.messagebox.showinfo(title="Felicidades", message="Los udls se modificaron correctamente")

#Se encarga de configurar el ticket printing service
def startingconfigureTicketPrintingService():
  logging.info(f' {datetime.datetime.now() }: Se comienza a ejecutar la funcion startingconfigureOptionInternet')
  protocol,url,stylepath,imgpath,ticketImg=identifyTicketPrintingService(logging,datetime)
  TextboxProtocolo.delete(0, tk.END)
  TextboxUrl.delete(0, tk.END)
  Textboxstylepath.delete(0, tk.END)
  Textboximgpath.delete(0, tk.END)
  TextboxticketImg.delete(0, tk.END)
  Insert(TextboxProtocolo,protocol,logging,datetime)
  Insert(TextboxUrl,url,logging,datetime)
  Insert(Textboxstylepath,stylepath,logging,datetime)
  Insert(Textboximgpath,imgpath,logging,datetime)
  Insert(TextboxticketImg,ticketImg,logging,datetime)
  
#Se encarga de actualizar los campos del config ddel ticket printing service
def startingUpdateTicketPrintingService():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar el ticket printing service')
  updateTicketPrintingService(TextboxProtocolo.get(),TextboxUrl.get(),Textboxstylepath.get(),Textboximgpath.get(),TextboxticketImg.get(),logging,datetime)

#Se encarga de actualizar la resolucion
def startingConfigureResolution():
  logging.info(f' {datetime.datetime.now() }: Se ejecuta el metodo startingConfigureResolution')
  ajustarResolucion(TextboxSelectResolution.get(),logging,datetime)

#Se encarga de configurar el autologon
def startingConfigureAutoLogon():
  logging.info(f' {datetime.datetime.now() }: Se ejecuta el metodo startingConfigureAutoLogon')
  bandera=validateField(TextboxALName,logging,MessageBox,"El autologon","el nombre del usuario",datetime)
  bandera=bandera*validateField(TextboxALDomain,logging,MessageBox,"El autologon","El dominio del usuario",datetime)
  bandera=bandera*validateField(TextboxALPassword,logging,MessageBox,"El autologon","La contraseña del usuario",datetime)
  if(bandera):
    if(autologon(TextboxALName.get(),TextboxALDomain.get(),TextboxALPassword.get(),logging,datetime)):tk.messagebox.showinfo(title="Felicidades", message="El autologon se modifico correctamente")  

#Se encarga de generar el script de inicio
def startingCreationScript():
  logging.info(f' {datetime.datetime.now() }: Se ejecuta el metodo startingCreationScript')
  if(browser.get()=="IExplorer"):
    nombre=tkinter.filedialog.asksaveasfilename(initialdir="/",title="Guardar como",filetypes=(("vbs","*.vbs"),("all type","*.*")))
    if(re.findall(".vbs",nombre)==[]):nombre=F"{nombre}.vbs"
    print(nombre)
    scriptBotoneraExplorer(nombre,label29.cget("text"),fullscreen.get(),xBrowserVar.get(),yBrowserVar.get(),logging,datetime)
    return ''
  nombre=tkinter.filedialog.asksaveasfilename(initialdir="/",title="Guardar como",filetypes=(("bat","*.bat"),("all type","*.*")))
  if(re.findall(".bat",nombre)==[]):nombre=F"{nombre}.bat"
  scriptBotonera(nombre,label29.cget("text"),logging,datetime)  
  
#Se encarga de realizar la consulta por powershell de TNC
def startingTest():
  logging.info(f' {datetime.datetime.now() }: Se ejecuta el metodo startingTest')
  bandera=validateField(TextboxTNCPort,logging,MessageBox,"La validacion del test","el nombre del usuario",datetime)
  bandera=bandera*validateField(TextboxTNCUrl,logging,MessageBox,"La validacion del test","el nombre del usuario",datetime)
  if(bandera):
    labelResult.config(text=TNC(TextboxTNCUrl.get(),TextboxTNCPort.get(),logging,datetime))  
    
#Se encarga de desbloquear los archivos
def startingUnblockingFolder():
    logging.info(f' {datetime.datetime.now() }: Se ejecuta el metodo startingUnblockingFolder')
    bandera=validateLabel(label32,logging,MessageBox,"El desbloqueo de archivo","la ruta",datetime)
    if(bandera):
      if(unLockFolder(label32.cget("text"),logging,datetime)):tk.messagebox.showinfo(title="Felicidades", message="El autologon se modifico correctamente")  
