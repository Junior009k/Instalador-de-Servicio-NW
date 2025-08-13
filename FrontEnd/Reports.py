from FrontEnd.VariableDeterminadas import *
from FrontEnd.Citas import loadDataAppointment
from FrontEnd.Encuestas import loadDataPoll
from FrontEnd.Virtualqueue import loadDataVQ

#esta funcion se encarga de examinar el directorio.
def ExamineDirectoryReporteria(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la carga de reportes')
  path = tkinter.filedialog.askdirectory()
  logging.info(f' {datetime.datetime.now() }: Borrando los campos de la tablas')
  for child in tree.get_children():
        tree.delete(child)
  if(True):
    logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {path}')
    path = path.replace("/", r"\ ".strip())
    path=path.rstrip()
    if(validateDirectory(f'{path}\\FrontEnd',"STE",logging,datetime)==False):
      versionEflow=identifyVersion(f"{path}\\FrontEnd\STE\\bin\eflow.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime)
      se=identifyService(f"{path}\\Middleware\\STE\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
      if(se!=None):labelReporteriaEflowService.config(fg= "green", text=f"{se[0]} | {se[1]} | {se[2]}")
      else:
        se=["No hay servicio instalado","None","none","none"]
        labelReporteriaEflowService.config(fg= "red", text=f"No hay servicio instalado")
      labelReporteriaEflow.config(fg= "green", text=f"e-Flow    {versionEflow}") 
    else:
      se=["No hay servicio instalado","none","none","none"]
      versionEflow="None"
      labelReporteriaEflow.config(fg= "red", text=f"e-Flow")
    if(validateDirectory(f'{path}\\FrontEnd',"Appointment",logging,datetime)==False):
      versionCitas=identifyVersion(f"{path}\\\FrontEnd\Appointment\\bin\Application.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime)
      sa=identifyService(f"{path}\\Middleware\\Appointment\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
      if(sa!=None):labelReporteriaCitasService.config(fg= "green", text=f"{sa[0]} | {sa[1]} | {sa[2]}")
      else:
        sa=["No hay servicio instalado","none","none","none"]
        labelReporteriaCitasService.config(fg= "red", text=f"No hay servicio instalado")
      labelReporteriaCitas.config(fg= "green", text=f"Citas        {versionCitas}")     
    else:
      sa=["No hay servicio instalado","none","none","none"]
      versionCitas="None"
      labelReporteriaCitas.config(fg= "red", text=f"Citas")  
    if(validateDirectory(f'{path}\\FrontEnd',"OpinionPoll",logging,datetime)==False):      
      versionEncuesta=identifyVersion(f"{path}\\FrontEnd\OpinionPoll\\bin\OpinionPoll.config","<Version>[\S|\\b|" "]+</Version>",logging,datetime)
      sen=identifyService(f"{path}\\Middleware\\Appointment\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
      if(sen!=None):labelReporteriaEncuestaService.config(fg= "green", text=f"{sen[0]} | {sen[1]} | {sen[2]}")
      else:
        sen=["No hay servicio instalado","none","none","none"]
        labelReporteriaEncuestaService.config(fg= "red", text=f"No hay servicio instalado")
      labelReporteriaEncuesta.config(fg= "green", text=f"Encuesta v{versionEncuesta}")
    else:
      sen=["No hay servicio instalado","none","none","none"]
      versionEncuesta="None"
      labelReporteriaEncuesta.config(fg= "red", text=f"Encuesta")
    data = [
        ("Version",versionEflow, versionCitas, versionEncuesta),
        ("Nombre",se[0],sa[0],sen[0]),
        ("Estado",se[1],sa[1],sen[1]),
        ("Inicio",se[2],sa[2],sen[2]),
        ("Ruta",  se[3],sa[3],sen[3]),
    ]
    for item in data:
        tree.insert("", "end", values=item)
    label.config(text=path) 
    print(path)
    return path
#Funcion que se encarga de cargar los reportes
def loadReporte(path,service,detailService,IIS, UDL,paquete,label,frame,db):
  #limpia todos los label
  service.config(text="Service",fg="black")
  detailService.config(text="",fg="black")
  IIS.config(text="IIS")
  UDL.config(text="UDL")
  #SERVICE
  #se asigna los servicios devueltos que coinciden con la ruta
  s=identifyService(f"{path}\Middleware\{paquete}\\bin\Sidesys.Services.ApplicationService.exe",logging,datetime)
  if(s!=None): 
    service.config(text=f"{s[0]}",fg="green")
    detailService.config(text=f"{s[1]}|{s[2]}",fg="green")
    if(s[1]=="Stopped"):boton = tk.Button(frame,text="Ejecutar", command=lambda:loadOptionService(1,boton,f"{label.cget('text')}\Middleware\{paquete}\\bin\Sidesys.Services.ApplicationService.exe,labelReporteriaServiceEflow",service,frame))
    if(s[1]=="Running"):boton = tk.Button(frame,text="Detener", command=lambda:loadOptionService(2,boton,f"{label.cget('text')}\Middleware\{paquete}\\bin\Sidesys.Services.ApplicationService.exe,labelReporteriaServiceEflow",service,frame))
    boton.place(x=230,y=125)
  else:
      service.config(text=f"No existe el aplicativo e-Flow",fg="red")
      if(validateDirectory(f"{path}\\FrontEnd",paquete,logging,datetime)==False): 
        service.config(text=f"No hay servicio instalado",fg="red")
        boton = tk.Button(frame,text="Instalar Servicio", command=lambda:loadOptionService(3,boton,f"{label.cget('text')}\Middleware\{paquete}\\bin\Sidesys.Services.ApplicationService.exe,labelReporteriaServiceEflow",service,frame))
        boton.place(x=230,y=125)
  #IIS
  texto=''
  datosApp=findApp(f"{path}\\FrontEnd\\{paquete}",logging,datetime)
  datosSite=findSite(f"{path}\\FrontEnd\\{paquete}",logging,datetime)
  if(datosApp!=False):
    name,site,protocol=datosApp
    i=0
    while(i<len(name)):
      texto=f"{texto}Aplication {name[i]} {site[i]} {protocol[i]}\n"
      i=i+1
  if(datosSite!=False):
    name,site,protocol=datosSite
    i=0
    while(i<len(name)):
      texto=f"{texto}Site {name[i]} {site[i]} {protocol[i]}\n"
      i=i+1
  IIS.config(text=f"{texto}",fg="green")
  if(texto==''):
    logging.error(f' {datetime.datetime.now() }: No se encontro aplicacion o site asociado a este paquete')
    IIS.config(text="No se encontro aplicacion o site asociado a este paquete",fg="red")
  #UDL
  textoUDL=''
  datosSOF=findUdls(f"{path}\\Middleware\\{paquete}\\ConfigFiles","SOF",logging,datetime)
  datosusrSTE=findUdls(f"{path}\\Middleware\\{paquete}\\ConfigFiles",db,logging,datetime)
  if(datosSOF!=False):textoUDL=f"{textoUDL}user:{datosSOF[1]} password:{datosSOF[0]} db:{datosSOF[2]} srv:{datosSOF[3]}\n"
  if(datosusrSTE!=False):textoUDL=f"{textoUDL}user:{datosusrSTE[1]} password:{datosusrSTE[0]} db:{datosusrSTE[2]} srv:{datosusrSTE[3]}"
  UDL.config(text=f"{textoUDL}",fg="green")
  if(textoUDL==''):
    logging.error(f' {datetime.datetime.now() }: Hubo un error al identificar los udls ')
    UDL.config(text="Revisar UDLS",fg="red")
#Funcion que permite manejar los servicios cargado en reporte generales
def loadOptionService(p,boton,path,labelReporteriaService,framei):
  logging.info(f' {datetime.datetime.now() }: Se ejecuta la funcion loadOptionService')
  if(p==1):
    manageService(1,labelReporteriaService.cget("text"),path,logging)
    boton.config(text="Detener", command=lambda:loadOptionService(2,boton,path,labelReporteriaService,framei))
  if(p==2):
    manageService(2,labelReporteriaService.cget("text"),path,logging)
    boton.config(text="Ejecutar", command=lambda:loadOptionService(1,boton,path,labelReporteriaService,framei))
  if(p==3):
    label1.config(text=path)
    boton.destroy()
    show_frame(framei,frame)
#Funcion que permite exportar los datos a excel
def exportExcel():
  a=[]
  b=[]
  c=[]
  d=[]
  logging.info(f' {datetime.datetime.now() }: Se estan exportando los siguientes datos a excel')
  for child in tree.get_children():
        a.append(tree.item(child)["values"][0])
        b.append(tree.item(child)["values"][1])
        c.append(tree.item(child)["values"][2])
        d.append(tree.item(child)["values"][3])
        logging.info(f' {datetime.datetime.now() }: {tree.item(child)["values"][0]}')
        logging.info(f' {datetime.datetime.now() }: {tree.item(child)["values"][1]}')
        logging.info(f' {datetime.datetime.now() }: {tree.item(child)["values"][2]}')
        logging.info(f' {datetime.datetime.now() }: {tree.item(child)["values"][3]}')           
  nombre=tkinter.filedialog.asksaveasfilename(initialdir="/",title="Guardar como",filetypes=(("Libro de excel","*.xlsx"),("todos los archivos","*.*")))
  if(re.findall(".xlsx",nombre)==[]):nombre=F"{nombre}.xlsx"
  try:
    registrarReporte(nombre,[b[0],b[1],b[2],b[3],b[4]],[c[0],c[1],c[2],c[3],c[4]],[d[0],d[1],d[2],d[3],d[4]], datetime, logging)
  except Exception as e:
    logging.error(f' {datetime.datetime.now() }: No se pudo exportar el archivo excel')
    logging.error(f' {datetime.datetime.now() }: {e}')
#esta funcion se encarga de Seleccionar el directorio y carga las horas
def ExamineDirectoryReportesAplicativos(p,label):
  path = tkinter.filedialog.askdirectory()
  logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {path} donde se identificaran los reportes')
  path = path.replace("/", r"\ ".strip())
  path=path.rstrip()
  label.config(text=path) 
  if(p==1):    
    loadReporte(path,labelReporteriaServiceEflow,labelReporteriaServiceEflowDetail,labelReporteriaIISEflow,labelReporteriaUDLEflow,"STE",label19,frame19,"STE")
  if(p==2):
    loadReporte(path,labelReporteriaServiceCitas,labelReporteriaServiceCitasDetail,labelReporteriaIISCitas,labelReporteriaUDLCitas,"Appointment",label20,frame20,"SSP")
    loadDataAppointment(path)
  if(p==3):
    loadReporte(path,labelReporteriaServiceEncuesta,labelReporteriaServiceEncuestaDetail,labelReporteriaIISEncuesta,labelReporteriaUDLEncuesta,"OpinionPoll",label21,frame21,"OpinionPoll")
    loadDataPoll(path)  
  if(p==4):
    loadDataVQ(path)
    return path
#Funcion que permite exportar la data de e-Flow
def exportDataEflowExcel():
  print("Se esta exportando la data de eflow")
#Funcion que permite exportar la data de Appointment
def exportDatAppointmentExcel():
  print("Se esta exportando la data de Appointment")
#Funcion que permite exportar la data de Encuesta
def exportDataEncuestaExcel():
  print("Se esta exportando la data de Encuesta")
#Funcion que permite exportar la data de VirtualQueue
def exportDataVirtualQueueExcel():
  print("Se esta exportando la data de VirtualQueue")

