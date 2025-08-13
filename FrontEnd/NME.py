from FrontEnd.VariableDeterminadas import *

#esta funcion se encarga de Seleccionar el directorio y carga las horas
def ExamineDirectoryNME(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la carga de datos de NME')
  Path = tkinter.filedialog.askdirectory()
  if(True):
    logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
    Path = Path.replace("/", r"\ ".strip())
    Path=Path.rstrip()
    label.config(text=Path) 
    if(identifyNME(Path,'"attentionPreferential": {\\n\s+"showButton": [\S|\\b|" "]+,','"showButton": [\S|\\b|" "]+,')):preferencialVar.set(1)
    else:preferencialVar.set(0)
    if(identifyNME(Path,'"announceAppointment": {\\n\s+"showAnnounceAppointment": [\S|\\b|" "]+,','"showAnnounceAppointment": [\S|\\b|" "]+,')):AnnounceAppointmentVar.set(1)
    else:AnnounceAppointmentVar.set(0)
    return Path

#esta funcion se encarga de configurar NME en e-Flow
def modifyNME():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  NME')
  bandera=validateField(TextboxsvrNME,logging,MessageBox,"el Nuevo Modulo de Emision","del servidor",datetime)
  bandera=bandera*validateField(TextboxeAPI,logging,MessageBox,"el Nuevo Modulo de Emision","el nombre del Emission Api",datetime)
  bandera=bandera*validateField(TextboxeFlowNME,logging,MessageBox,"el Nuevo Modulo de Emision","del sitio de e-Flow",datetime)
  bandera=bandera*validateLabel(label8,logging,MessageBox,"el Nuevo Modulo de Emision","la ruta",datetime)
  if( validateDirectory(label8.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label8.cget("text"),"FrontEnd",logging,datetime)):label8.config(text="") 
  bandera=bandera*validateLabel(label8,logging,MessageBox,"el Nuevo Modulo de Emision","tiene que estar en la carpeta del aplicativo",datetime)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Nuevo Modulo de Emision')
    tk.messagebox.showinfo(title="Felicidades", message="NME termino el proceso de configuracion de los archivos")
    configurarNME(label8.cget("text"),TextboxsvrNME.get(),TextboxeFlowNME.get(),TextboxeAPI.get(),logging,datetime)
#esta funcion se encarga de configurar NME en e-Flow
def modifyNMEEmissionConfig():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  emission.config')
  bandera=validateLabel(label15,logging,MessageBox,"emission.config","la ruta",datetime)
  if( validateDirectory(label15.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label15.cget("text"),"FrontEnd",logging,datetime)):label15.config(text="") 
  bandera=bandera*validateLabel(label15,logging,MessageBox,"emission.config","tiene que estar en la carpeta del aplicativo",datetime)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Nuevo Modulo de Emision')
    tk.messagebox.showinfo(title="Felicidades", message="El Emission.config termino el proceso de configuracion de los archivos")
    configurarEmissionConfig(label15.cget("text"), preferencialVar.get(),AnnounceAppointmentVar.get(), logging,datetime)
#esta funcion se encarga de configurar NME en e-Flow con site
def modifyNMESite():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  NME')
  bandera=validateField(TextboxsvrNMESite,logging,MessageBox,"el Nuevo Modulo de Emision","del servidor",datetime)
  bandera=bandera*validateField(TextboxeAPISite,logging,MessageBox,"el Nuevo Modulo de Emision","el nombre del Emission Api",datetime)
  bandera=bandera*validateField(TextboxeFlowNMESite,logging,MessageBox,"el Nuevo Modulo de Emision","del sitio de e-Flow",datetime)
  bandera=bandera*validateLabel(label4,logging,MessageBox,"el Nuevo Modulo de Emision","la ruta",datetime)
  if( validateDirectory(label4.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label4.cget("text"),"FrontEnd",logging,datetime)):label4.config(text="") 
  bandera=bandera*validateLabel(label4,logging,MessageBox,"el Nuevo Modulo de Emision","tiene que estar en la carpeta del aplicativo")
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Nuevo Modulo de Emision')
    tk.messagebox.showinfo(title="Felicidades", message="El NME con site termino el proceso de configuracion de los archivos")
    configurarNMESite(label14.cget("text"),TextboxsvrNMESite.get(),TextboxeFlowNMESite.get(),TextboxeAPISite.get(),logging,datetime)
#esta funcion se encarga de configurar NME en citas
def modifyNMECitas():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  NME')
  bandera=validateField(TextboxsvrNMECitas,logging,MessageBox,"el Web sevice de citas","del servidor,datetime")
  bandera=bandera*validateField(TextboxCitasNME,logging,MessageBox,"el Web sevice de citas","del sitio de Citas",datetime)
  bandera=bandera*validateLabel(label9,logging,MessageBox,"el Web sevice de citas","la ruta",datetime)
  if( validateDirectory(label9.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label9.cget("text"),"FrontEnd",logging,datetime)):label9.config(text="") 
  bandera=bandera*validateLabel(label9,logging,MessageBox,"el Web sevice de citas","tiene que estar en la carpeta del aplicativo")
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion del Web sevice de citas',datetime)
    configurarNMECitas(label9.cget("text"),TextboxsvrNMECitas.get(),TextboxCitasNME.get(),logging,datetime)
