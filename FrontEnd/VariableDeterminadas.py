from tkinter import *
from FrontEnd.Mainmethods import *
from FrontEnd.Rutas import *
from FrontEnd.appsetting import *
from FrontEnd.systeminformation import *
from Middleware.Api import loginVirtualQueue,getAllOrganization,getAllServiceByOrganization
from Middleware.Validador import validateDirectory
from Middleware.script import identifyService,manageService,installService,installDLL,manageInternetOption,autoplaylist,cargarResolucion,ajustarResolucion,autologon,scriptBotonera,scriptBotoneraExplorer,unLockFolder,TNC
from Middleware.iis import createAplicationIIS,createSiteIIS,ko,findApp,findSite,re,os
from Middleware.udl import findUdls,validateService,manageUDL,validateConnection
from Middleware.db import getColor,getIdColor,getColors,setColor,setConfiguration
from Middleware.NCache import configurarNCache
from Middleware.NME import fixWord,show_frame,show_Configuration,loadImagen,IdentifyJSON,identifyBaseURL,Insert,identifyNME,validateField,validateLabel,configurarNME,configurarEmissionConfig,configurarNMESite,configurarNMECitas,identifyTicketPrintingService,updateTicketPrintingService
from Middleware.Nodo import configurarNodo
from Middleware.portService import changePort,changePortAppointment
from Middleware.configuracionCitas import updateCitas,configurarCitas
from Middleware.RHI import configurarHorario,identifyHour,identifyMinute
from Middleware.mail import configurarMail,sendEmail
from Middleware.Reporte import identifyVersion
from Middleware.Encuesta import updateEncuestas,configurarEncuesta
from Middleware.Consola import configurarMinuteConsole,identifyMinuteSesion,Identify
from Middleware.Excel import registrarReporte
from Middleware.VirtualQueue import updatesVirtualQueue
from Middleware.MSMQ import sendMessage,receivedMessage
from Middleware.Suite import configurarSuite,configurarBBDDSuite, configurarCitasSuite
from tkinter import messagebox as MessageBox,font
import tkinter as tk
from tkinter import ttk
import logging
import datetime
import tkinter.filedialog

#===========================CONSTANTE DEL FRONTEND================================
#Loggin
#Declaracion del Loggin
logging.basicConfig(filename=f'{LOGS} {datetime.datetime.now().date()}.log ', encoding='utf-8', level=logging.DEBUG)
logging.info(f' {datetime.datetime.now() }: Inicializacion de la Aplicacion')

#Menu
menu = tk.Tk()

#Crear el primer menú.
barra_menus = tk.Menu()
menu_archivo = tk.Menu(barra_menus, tearoff=False)
menu_opciones = tk.Menu(barra_menus, tearoff=False)

#======Carga de imagen=======
icono = loadImagen(f"{IMG}\icon-16.png",PhotoImage,logging,datetime)
eflowimg= loadImagen(f"{IMG}\eflow.png",PhotoImage,logging,datetime)
client= loadImagen(f"{IMG}\client.png",PhotoImage,logging,datetime)
citas= loadImagen(f"{IMG}\citas.png",PhotoImage,logging,datetime)
encuesta= loadImagen(f"{IMG}\Encuesta.png",PhotoImage,logging,datetime)
report= loadImagen(f"{IMG}\\report.png",PhotoImage,logging,datetime)
automatizacion= loadImagen(f"{IMG}\\automatizacion.png",PhotoImage,logging,datetime)
imagen= loadImagen(f"{IMG}\sidesys.gif",PhotoImage,logging,datetime)
confImg= loadImagen(f"{IMG}\conf.png",PhotoImage,logging,datetime)
correo= loadImagen(f"{IMG}\correo.png",PhotoImage,logging,datetime)
diagnosticoimg= loadImagen(f"{IMG}\diagnostico.png",PhotoImage,logging,datetime)
excel= loadImagen(f"{IMG}\Excel-icon.png",PhotoImage,logging,datetime)
impresora= loadImagen(f"{IMG}\impresora.png",PhotoImage,logging,datetime)
imagen= loadImagen(f"{IMG}\sidesys.gif",PhotoImage,logging,datetime)
suiteimg= loadImagen(f"{IMG}\suite.png",PhotoImage,logging,datetime)
apiimg= loadImagen(f"{IMG}\\api.png",PhotoImage,logging,datetime)
confImg =loadImagen(f"{IMG}\conf.png",PhotoImage,logging,datetime)
reloadImg =loadImagen(f"{IMG}\\reload.png",PhotoImage,logging,datetime)

#FRAMES
frameMenuEflow=Frame(menu)
frameMenuPrincipal = Frame(menu)
frameMenuClient = Frame(menu)
frameMenuCitas = Frame(menu)
frameMenuEncuesta = Frame(menu)
frameMenuReport = Frame(menu)
frameMenuAuto = Frame(menu)
frameMenuDiagnosis = Frame(menu)
frameMenuML = Frame(menu)
frameMenuApi = Frame(menu)
frameMenuSuite = Frame(menu)
framesubMenuIIS = Frame(menu)
framesubMenuNME = Frame(menu)
frame = Frame(menu)
frame2 = Frame(menu)
frame3 = Frame(menu)
frame4 = Frame(menu)
frame5 = Frame(menu)
frame6 = Frame(menu)
frame7 = Frame(menu)
frame8 = Frame(menu)
frame9 = Frame(menu)
frame10 = Frame(menu)
frame11 = Frame(menu)
frame12 = Frame(menu)
frame13 = Frame(menu)
frame14 = Frame(menu)
frame15 = Frame(menu)
frame16 = Frame(menu)
frame16b = Frame(menu) 
frame17 = Frame(menu)
frame18 = Frame(menu)
frame19 = Frame(menu)
frame20 = Frame(menu)
frame20b = Frame(menu)
frame20c = Frame(menu)
frame20d = Frame(menu)
frame21 = Frame(menu)
frame21b = Frame(menu)
frame22 = Frame(menu)
frame23 = Frame(menu)
frame24 = Frame(menu)
frame25 = Frame(menu)
frame26 = Frame(menu)
frame27 = Frame(menu)
frame28 = Frame(menu)
frame29 = Frame(menu)
frame30 = Frame(menu)
frame31 = Frame(menu)
frame32 = Frame(menu)
frame33 = Frame(menu)
frame34 = Frame(menu)
frame35 = Frame(menu)
frame36 = Frame(menu)
frame37 = Frame(menu)
frame38 = Frame(menu)
frame39 = Frame(menu)
frameConfiguracionColoresPrincipales = Frame(menu) 
frameConfiguracionColoresSecundarios =Frame(menu) 
#BOTONES
#Botones Menu Principal
if(SYSTEMBUTTONEFLOW):buttonEflow = tk.Button(frameMenuPrincipal,width=100,height=41, image = eflowimg,text="e-Flow", command=lambda: show_frame(frameMenuPrincipal,frameMenuEflow)).place(x=45,y=100)
if(SYSTEMBUTTONCLIENT):buttonClient = tk.Button(frameMenuPrincipal,width=100,height=41, image = client,text="e-Flow", command=lambda: show_frame(frameMenuPrincipal,frameMenuClient)).place(x=157,y=100)
if(SYSTEMBUTTONCITAS):buttonCitas = tk.Button(frameMenuPrincipal,width=100,height=41, image = citas,text="Citas", command=lambda: show_frame(frameMenuPrincipal,frameMenuCitas)).place(x=270,y=100)
if(SYSTEMBUTTONENCUESTAS):buttonEncuesta = tk.Button(frameMenuPrincipal,width=100,height=41, image = encuesta,text="Encuesta", command=lambda: show_frame(frameMenuPrincipal,frameMenuEncuesta)).place(x=45,y=175)
if(SYSTEMBUTTONREPORT):buttonReport = tk.Button(frameMenuPrincipal,width=100,height=41, image = report,text="e-Flow", command=lambda: show_frame(frameMenuPrincipal,frameMenuReport)).place(x=157,y=175)
if(SYSTEMBUTTONAUTOMATIZACION):buttonAutomatizacion = tk.Button(frameMenuPrincipal,width=100,height=41, image = automatizacion,text="Automatizacion", command=lambda: show_frame(frameMenuPrincipal,frameMenuAuto)).place(x=270,y=175)
if(SYSTEMBUTTONAUTOMATIZACION):buttonDiagnosis = tk.Button(frameMenuPrincipal,width=100,height=41,image = diagnosticoimg,text="Diagnosisto", command=lambda: show_frame(frameMenuPrincipal,frameMenuDiagnosis)).place(x=45,y=250)
if(SYSTEMBUTTONMAIL):buttonCorreo = tk.Button(frameMenuPrincipal,width=100,height=41,image = correo,text="Modo Libre", command=lambda: show_frame(frameMenuPrincipal,frameMenuML)).place(x=45,y=250)
if(SYSTEMBUTTONSUITE):buttonSuite = tk.Button(frameMenuPrincipal,width=100,height=41,image = suiteimg,text="Suite", command=lambda: show_frame(frameMenuPrincipal,frameMenuSuite)).place(x=157,y=250)
if(SYSTEMBUTTONAPI):buttonApi = tk.Button(frameMenuPrincipal,width=100,height=41,image = apiimg,text="API", command=lambda: show_frame(frameMenuPrincipal,frameMenuApi)).place(x=270,y=250)

#Botones Menu e-Flow
if(SYSTEMBUTTONEFLOWSERVICE):buttonEflowService = tk.Button(frameMenuEflow,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuEflow,frame)).place(x=45,y=100)
if(SYSTEMBUTTONEFLOWIIS):buttonEflowIIS = tk.Button(frameMenuEflow,width=20,height=1, text="IIS", command=lambda: show_frame(frameMenuEflow,framesubMenuIIS)).place(x=230,y=100)
if(SYSTEMBUTTONEFLOWUDL):buttonEflowUDL = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador de UDLS", command=lambda: show_frame(frameMenuEflow,frame3)).place(x=230,y=130)
if(SYSTEMBUTTONEFLOWSITES):buttonEflowSites = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador del nodo", command=lambda: show_frame(frameMenuEflow,frame16)).place(x=45,y=130)
if(SYSTEMBUTTONEFLOWPORT):buttonEflowPort = tk.Button(frameMenuEflow,width=20,height=1, text="Modificador de puertos", command=lambda: show_frame(frameMenuEflow,frame4)).place(x=45,y=160)
if(SYSTEMBUTTONEFLOWNCACHE):buttonEflowNCache = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador NCache", command=lambda: show_frame(frameMenuEflow,frame7)).place(x=230,y=160)
if(SYSTEMBUTTONEFLOWNME):buttonEflowNME = tk.Button(frameMenuEflow,width=20,height=1, text="Configurador NME", command=lambda: show_frame(frameMenuEflow,framesubMenuNME)).place(x=45,y=190)
if(SYSTEMBUTTONEFLOWRHI):buttonEflowProcesoHistorico = tk.Button(frameMenuEflow,width=20,height=1, text="Procesamiento del RHI", command=lambda: show_frame(frameMenuEflow,frame10)).place(x=230,y=190)
if(SYSTEMBUTTONEFLOWMAIL):buttonEflowMail = tk.Button(frameMenuEflow,width=20,height=1, text="Configuracion de correo", command=lambda: show_frame(frameMenuEflow,frame11)).place(x=45,y=220)
if(SYSTEMBUTTONEFLOWCONSOLE):buttonEflowConsole = tk.Button(frameMenuEflow,width=20,height=1, text="tiempo de sesion consola", command=lambda: show_frame(frameMenuEflow,frame13)).place(x=230,y=220)

#Botones Menu Client 
buttonClientService = tk.Button(frameMenuClient,width=20,height=1, text="Instalador DLL", command=lambda: show_frame(frameMenuClient,frame23)).place(x=45,y=100)
buttonClientInternetOption = tk.Button(frameMenuClient,width=20,height=1, text="Internet option", command=lambda: show_frame(frameMenuClient,frame24)).place(x=230,y=100)
buttonClienTicketPrintingService = tk.Button(frameMenuClient,width=20,height=1, text="Ticket Printing service", command=lambda: show_frame(frameMenuClient,frame25)).place(x=45,y=130)
buttonClienAutoPlaylist = tk.Button(frameMenuClient,width=20,height=1, text="Autoplaylist", command=lambda: show_frame(frameMenuClient,frame26)).place(x=230,y=130)
buttonClienRE = tk.Button(frameMenuClient,width=20,height=1, text="Ajustar resolucion", command=lambda: show_frame(frameMenuClient,frame27)).place(x=45,y=160)
buttonClienAutoLogon = tk.Button(frameMenuClient,width=20,height=1, text="AutoLogon", command=lambda: show_frame(frameMenuClient,frame28)).place(x=230,y=160)
buttonClienScriptInicio = tk.Button(frameMenuClient,width=20,height=1, text="Script de inicio", command=lambda: show_frame(frameMenuClient,frame29)).place(x=45,y=190)
buttonClientUnblockFolder= tk.Button(frameMenuClient,width=20,height=1, text="unBlock Folder", command=lambda: show_frame(frameMenuClient,frame32)).place(x=230,y=190)

#Botones Menu Citas
if(SYSTEMBUTTONEFLOWSERVICE):buttonCitasService = tk.Button(frameMenuCitas,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuCitas,frame)).place(x=45,y=100)
if(SYSTEMBUTTONEFLOWIIS):buttonCitasIIS = tk.Button(frameMenuCitas,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(frameMenuCitas,frame2)).place(x=230,y=100)
if(SYSTEMBUTTONEFLOWUDL):buttonCitasUDL = tk.Button(frameMenuCitas,width=20,height=1, text="Configurador de UDLS", command=lambda: show_frame(frameMenuCitas,frame3)).place(x=45,y=130)
if(SYSTEMBUTTONAPPOINTMENTCONFIGURE):buttonCitasPort = tk.Button(frameMenuCitas,width=20,height=1, text="Configurador de Citas", command=lambda: show_frame(frameMenuCitas,frame5)).place(x=230,y=130)
if(SYSTEMBUTTONAPPOINTMENTNME):buttonCitasNME = tk.Button(frameMenuCitas,width=20,height=1, text="Configurador de NME", command=lambda: show_frame(frameMenuCitas,frame9)).place(x=45,y=160)
if(SYSTEMBUTTONEFLOWMAIL):buttonCitasMail = tk.Button(frameMenuCitas,width=20,height=1, text="Configuracion de correo", command=lambda: show_frame(frameMenuCitas,frame11)).place(x=230,y=160)
if(SYSTEMBUTTONAPPOINTMENTPORT):buttonCitasPort = tk.Button(frameMenuCitas,width=20,height=1, text="Modificador de puertos", command=lambda: show_frame(frameMenuCitas,frame30)).place(x=45,y=190)

#Botones Menu Encuestas
buttonEncuestaService = tk.Button(frameMenuEncuesta,width=20,height=1, text="Instalador de servicio", command=lambda: show_frame(frameMenuEncuesta,frame)).place(x=45,y=100)
buttonEncuestaIIS = tk.Button(frameMenuEncuesta,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(frameMenuEncuesta,frame2)).place(x=230,y=100)
buttonEncuestaUDL = tk.Button(frameMenuEncuesta,width=20,height=1, text="Configurador de UDLS", command=lambda: show_frame(frameMenuEncuesta,frame3)).place(x=45,y=130)
buttonEncuestaMail = tk.Button(frameMenuEncuesta,width=20,height=1, text="Configuracion de correo", command=lambda: show_frame(frameMenuEncuesta,frame11)).place(x=230,y=130)
buttonEncuestaConfig = tk.Button(frameMenuEncuesta,width=20,height=1, text="Configuracion de encuesta", command=lambda: show_frame(frameMenuEncuesta,frame12)).place(x=45,y=160)

#Botones Menu Reporteria
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte General", command=lambda: show_frame(frameMenuReport,frame18)).place(x=45,y=100)
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte e-Flow", command=lambda: show_frame(frameMenuReport,frame19)).place(x=45,y=130)
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte Citas", command=lambda: show_frame(frameMenuReport,frame20)).place(x=230,y=100)
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte Encuestas", command=lambda: show_frame(frameMenuReport,frame21)).place(x=230,y=130)
buttonReporGeneral = tk.Button(frameMenuReport,width=20,height=1, text="Reporte Virtual Queue", command=lambda: show_frame(frameMenuReport,frame22)).place(x=45,y=160)

#Botones Automatizacion
buttonReporService = tk.Button(frameMenuAuto,width=20,height=1, text="Automatizador Basico", command=lambda: show_frame(frameMenuAuto,frame17)).place(x=45,y=100)

#Botones Mail
buttonReporService = tk.Button(frameMenuML,width=20,height=1, text="Ver mis correo", command=lambda: show_frame(frameMenuML,frame)).place(x=45,y=100)

#Botones Diagnostico
buttonMSMQ = tk.Button(frameMenuDiagnosis,width=20,height=1, text="MSMQ", command=lambda: show_frame(frameMenuDiagnosis,frame31)).place(x=45,y=100)
buttonTNC = tk.Button(frameMenuDiagnosis,width=20,height=1, text="TNC", command=lambda: show_frame(frameMenuDiagnosis,frame33)).place(x=230,y=100)
buttonDiagnosticoMail = tk.Button(frameMenuDiagnosis,width=20,height=1, text="Mail Server", command=lambda: show_frame(frameMenuDiagnosis,frame11)).place(x=45,y=130)
if(SYSTEMBUTTONEFLOWUDL):buttonEflowUDL = tk.Button(frameMenuDiagnosis,width=20,height=1, text="Dianosticador SQL", command=lambda: show_frame(frameMenuDiagnosis,frame3)).place(x=230,y=130)
buttonDiagnosticorGeneral = tk.Button(frameMenuDiagnosis,width=20,height=1, text="Diagnosticador General", command=lambda: show_frame(frameMenuDiagnosis,frame39)).place(x=45,y=160)

#Botones Suite
buttonConfigSuite = tk.Button(frameMenuSuite,width=20,height=1, text="Configurador Suite", command=lambda: show_frame(frameMenuSuite,frame34)).place(x=45,y=100)
buttonReporGeneral = tk.Button(frameMenuSuite,width=20,height=1, text="Configurador BBDD", command=lambda: show_frame(frameMenuSuite,frame35)).place(x=45,y=130)
buttonReporGeneral = tk.Button(frameMenuSuite,width=20,height=1, text="Configurador Im-Citas", command=lambda: show_frame(frameMenuSuite,frame36)).place(x=230,y=100)

#Botones Api
buttonConfigVirtualQueue = tk.Button(frameMenuApi,width=20,height=1, text="Virtual Queue", command=lambda: show_frame(frameMenuApi,frame37)).place(x=45,y=100)

#Botones Sub Menu IIS
buttonAplicationIIS = tk.Button(framesubMenuIIS,width=20,height=1, text="Creador de aplicaciones", command=lambda: show_frame(framesubMenuIIS,frame2)).place(x=45,y=100)
buttonSiteIIS = tk.Button(framesubMenuIIS,width=20,height=1, text="Creador de site", command=lambda: show_frame(framesubMenuIIS,frame6)).place(x=230,y=100)
buttonEflowBack = tk.Button(framesubMenuIIS,width=20,height=1, text="Back e-Flow", command=lambda: show_frame(framesubMenuIIS,frameMenuEflow)).place(x=45,y=270)
buttonEflowBack = tk.Button(framesubMenuIIS,width=20,height=1, text="Back to Menu Principal", command=lambda: show_frame(framesubMenuIIS,frameMenuPrincipal)).place(x=230,y=270)

#Botones Sub Menu NME
buttonAplication = tk.Button(framesubMenuNME,width=20,height=1, text="NME Aplication", command=lambda: show_frame(framesubMenuNME,frame8)).place(x=45,y=100)
buttonSite = tk.Button(framesubMenuNME,width=20,height=1, text="NME Site", command=lambda: show_frame(framesubMenuNME,frame14)).place(x=230,y=100)
buttonSetting = tk.Button(framesubMenuNME,width=20,height=1, text="Emission.config", command=lambda: show_frame(framesubMenuNME,frame15)).place(x=45,y=130)
buttonEflowBack = tk.Button(framesubMenuNME,width=20,height=1, text="Back e-Flow", command=lambda: show_frame(framesubMenuNME,frameMenuEflow)).place(x=45,y=270)
buttonEflowBack = tk.Button(framesubMenuNME,width=20,height=1, text="Back to Menu Principal", command=lambda: show_frame(framesubMenuNME,frameMenuPrincipal)).place(x=230,y=270)

#Etiquetas
label1 = tk.Label(frame) #se agregan las etiquetas al frame
label2 = tk.Label(frame2) #se agregan las etiquetas al frame
label3 = tk.Label(frame3) #se agregan las etiquetas al frame
label4 = tk.Label(frame4) #se agregan las etiquetas al frame
label5 = tk.Label(frame5) #se agregan las etiquetas al frame
label6 = tk.Label(frame6) #se agregan las etiquetas al frame
label7 = tk.Label(frame7) #se agregan las etiquetas al frame
label8 = tk.Label(frame8) #se agregan las etiquetas al frame
label9 = tk.Label(frame9) #se agregan las etiquetas al frame
label10 = tk.Label(frame10) #se agregan las etiquetas al frame
label11 = tk.Label(frame11) #se agregan las etiquetas al frame
label12 = tk.Label(frame12) #se agregan las etiquetas al frame
label13 = tk.Label(frame13) #se agregan las etiquetas al frame
label14 = tk.Label(frame14) #se agregan las etiquetas al frame
label15 = tk.Label(frame15) #se agregan las etiquetas al frame
label16 = tk.Label(frame16) #se agregan las etiquetas al frame
label17 = tk.Label(frame17) #se agregan las etiquetas al frame
label18 = tk.Label(frame18) #se agregan las etiquetas al frame
label19 = tk.Label(frame19) #se agregan las etiquetas al frame
label20 = tk.Label(frame20) #se agregan las etiquetas al frame
label21 = tk.Label(frame21) #se agregan las etiquetas al frame
label22 = tk.Label(frame22) #se agregan las etiquetas al frame
label23 = tk.Label(frame23) #se agregan las etiquetas al frame
label25 = tk.Label(frame25) #se agregan las etiquetas al frame
label29 = tk.Label(frame29) #se agregan las etiquetas al frame
label30 = tk.Label(frame30) #se agregan las etiquetas al frame
label32 = tk.Label(frame32) #se agregan las etiquetas al frame
label34 = tk.Label(frame34) #se agregan las etiquetas al frame
label35 = tk.Label(frame35) #se agregan las etiquetas al frame
label36 = tk.Label(frame36) #se agregan las etiquetas al frame
label38 = tk.Label(frame38) #se agregan las etiquetas al frame
label39 = tk.Label(frame39) #se agregan las etiquetas al frame
#========Configuracion de la aplicacion=======
k = tk.Label(menu,text="0")
sizeVentana=IdentifyJSON(f'{APPSETTING}',SIZEVENTANA[0],SIZEVENTANA[1],logging,datetime).replace('"', r'')
if(IdentifyJSON(f'{APPSETTING}',RESIZABLE[0],RESIZABLE[1],logging,datetime).replace('"', r'')=="False"):resizable=False
else:resizable=True

#========Carga de colores=======
#Establece las variables a configurar
variableColor1 = StringVar(menu)
variableColor1.set(getColor(1,"c.descripcion")) # default value
variableColor2 = StringVar(menu)
variableColor2.set(getColor(2,"c.descripcion")) # default value
variableColor3 = StringVar(menu)
variableColor3.set(getColor(3,"c.descripcion")) # default value
variableColor4 = StringVar(menu)
variableColor4.set(getColor(4,"c.descripcion")) # default value
variableColor5 = StringVar(menu)
variableColor5.set(getColor(5,"c.descripcion")) # default value
colorframe1=getColor(1,"codigo")
colorframe2=getColor(2,"codigo")
colorframe3=getColor(3,"codigo")
colorframe4=getColor(4,"codigo")
colorframe5=getColor(5,"codigo")
colorframeC="#555"

#===Colores Menu principal y secundarios===
colorMenuPrincipal=IdentifyJSON(f'{APPSETTING}',COLORMENUMENUPRINCIPAL[0],COLORMENUMENUPRINCIPAL[1],logging,datetime).replace('"', r'')
colorMenuEflow=IdentifyJSON(f'{APPSETTING}',COLORMENUEFLOW[0],COLORMENUEFLOW[1],logging,datetime).replace('"', r'')
colorMenuClient=IdentifyJSON(f'{APPSETTING}',COLORMENUCLIENT[0],COLORMENUCLIENT[1],logging,datetime).replace('"', r'')
colorMenuCita=IdentifyJSON(f'{APPSETTING}',COLORMENUCITAS[0],COLORMENUCITAS[1],logging,datetime).replace('"', r'')
colorMenuEncuesta=IdentifyJSON(f'{APPSETTING}',COLORMENUENCUESTA[0],COLORMENUENCUESTA[1],logging,datetime).replace('"', r'')
colorMenuReporteria=IdentifyJSON(f'{APPSETTING}',COLORMENUREPORT[0],COLORMENUREPORT[1],logging,datetime).replace('"', r'')
colorMenuAutomatizacion=IdentifyJSON(f'{APPSETTING}',COLORMENUAUTO[0],COLORMENUAUTO[1],logging,datetime).replace('"', r'')
colorMenumail=IdentifyJSON(f'{APPSETTING}',COLORMENUMAIL[0],COLORMENUMAIL[1],logging,datetime).replace('"', r'')
colorMenuDiagnostico=IdentifyJSON(f'{APPSETTING}',COLORMENUDIAGNOSTICO[0],COLORMENUDIAGNOSTICO[1],logging,datetime).replace('"', r'')
colorMenuApi=IdentifyJSON(f'{APPSETTING}',COLORMENUAPI[0],COLORMENUAPI[1],logging,datetime).replace('"', r'')
colorMenuSuite=IdentifyJSON(f'{APPSETTING}',COLORMENUSUITE[0],COLORMENUSUITE[1],logging,datetime).replace('"', r'')
colorMenuNME=IdentifyJSON(f'{APPSETTING}',COLORMENUNME[0],COLORMENUNME[1],logging,datetime).replace('"', r'')
colorMenuNcache=IdentifyJSON(f'{APPSETTING}',COLORMENUNCACHE[0],COLORMENUNCACHE[1],logging,datetime).replace('"', r'')
colorMenuservice=IdentifyJSON(f'{APPSETTING}',COLORMENUSERVICE[0],COLORMENUSERVICE[1],logging,datetime).replace('"', r'')
colorMenuiis=IdentifyJSON(f'{APPSETTING}',COLORMENUIIS[0],COLORMENUIIS[1],logging,datetime).replace('"', r'')
colorMenuudl=IdentifyJSON(f'{APPSETTING}',COLORMENUUDL[0],COLORMENUUDL[1],logging,datetime).replace('"', r'')
colorMenuport=IdentifyJSON(f'{APPSETTING}',COLORMENUPORT[0],COLORMENUPORT[1],logging,datetime).replace('"', r'')

nameMenuPrincipal=IdentifyJSON(f'{APPSETTING}',NAMEMENUPRINCIPAL[0],NAMEMENUPRINCIPAL[1],logging,datetime).replace('"', r'')
nameMenuEflow=IdentifyJSON(f'{APPSETTING}',NAMEMENUEFLOW[0],NAMEMENUEFLOW[1],logging,datetime).replace('"', r'')
nameMenuClient=IdentifyJSON(f'{APPSETTING}',NAMEMENUCLIENT[0],NAMEMENUCLIENT[1],logging,datetime).replace('"', r'')
nameMenuCitas=IdentifyJSON(f'{APPSETTING}',NAMEMENUCITAS[0],NAMEMENUCITAS[1],logging,datetime).replace('"', r'')
nameMenuEncuesta=IdentifyJSON(f'{APPSETTING}',NAMEMENUENCUESTA[0],NAMEMENUENCUESTA[1],logging,datetime).replace('"', r'')
nameMenuReportes=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTE[0],NAMEMENUREPORTE[1],logging,datetime).replace('"', r'')
nameMenuAuto=IdentifyJSON(f'{APPSETTING}',NAMEMENUAUTOMATICO[0],NAMEMENUAUTOMATICO[1],logging,datetime).replace('"', r'')
nameMenuMail=IdentifyJSON(f'{APPSETTING}',NAMEMENUMAIL[0],NAMEMENUMAIL[1],logging,datetime).replace('"', r'')
nameMenuDiagnostico=IdentifyJSON(f'{APPSETTING}',NAMEMENUDIAGNOSTICO[0],NAMEMENUDIAGNOSTICO[1],logging,datetime).replace('"', r'')
nameMenuApi=IdentifyJSON(f'{APPSETTING}',NAMEMENUAPI[0],NAMEMENUAPI[1],logging,datetime).replace('"', r'')
nameMenuSuite=IdentifyJSON(f'{APPSETTING}',NAMEMENUSUITE[0],NAMEMENUSUITE[1],logging,datetime).replace('"', r'')
namesubMenuIIS=IdentifyJSON(f'{APPSETTING}',NAMESUBMENUIIS[0],NAMESUBMENUIIS[1],logging,datetime).replace('"', r'')
nameSubMenuNME=IdentifyJSON(f'{APPSETTING}',NAMESUBMENUNME[0],NAMESUBMENUNME[1],logging,datetime).replace('"', r'')
nameMenuService=IdentifyJSON(f'{APPSETTING}',NAMEMENUSERVICE[0],NAMEMENUSERVICE[1],logging,datetime).replace('"', r'')
nameMenuAIIS=IdentifyJSON(f'{APPSETTING}',NAMEMENUAIIS[0],NAMEMENUAIIS[1],logging,datetime).replace('"', r'')
nameMenuUDL=IdentifyJSON(f'{APPSETTING}',NAMEMENUUDL[0],NAMEMENUUDL[1],logging,datetime).replace('"', r'')
nameMenuPort=IdentifyJSON(f'{APPSETTING}',NAMEMENUPORT[0],NAMEMENUPORT[1],logging,datetime).replace('"', r'')
nameMenuConfigCitas=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGCITAS[0],NAMEMENUCONFIGCITAS[1],logging,datetime).replace('"', r'')
nameMenuSIIS=IdentifyJSON(f'{APPSETTING}',NAMEMENUSIIS[0],NAMEMENUSIIS[1],logging,datetime).replace('"', r'')
nameMenuNCache=IdentifyJSON(f'{APPSETTING}',NAMEMENUNCACHE[0],NAMEMENUNCACHE[1],logging,datetime).replace('"', r'')
nameMenuConfigNME=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGNME[0],NAMEMENUCONFIGNME[1],logging,datetime).replace('"', r'')
nameMenuRHI=IdentifyJSON(f'{APPSETTING}',NAMEMENURHI[0],NAMEMENURHI[1],logging,datetime).replace('"', r'')
nameMenuConfigCitasNME=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGCITASNME[0],NAMEMENUCONFIGCITASNME[1],logging,datetime).replace('"', r'')
nameMenuCorreo=IdentifyJSON(f'{APPSETTING}',NAMEMENUCORREO[0],NAMEMENUCORREO[1],logging,datetime).replace('"', r'')
nameMenuConfigEncuesta=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGENCUESTA[0],NAMEMENUCONFIGENCUESTA[1],logging,datetime).replace('"', r'')
nameMenuConfigTimeSesionConsole=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGTIMESESIONCONSOLE[0],NAMEMENUCONFIGTIMESESIONCONSOLE[1],logging,datetime).replace('"', r'')
nameMenuConfigNMESite=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGNMESITE[0],NAMEMENUCONFIGNMESITE[1],logging,datetime).replace('"', r'')
nameMenuEmissionConfig=IdentifyJSON(f'{APPSETTING}',NAMEMENUEMISSIONCONFIG[0],NAMEMENUEMISSIONCONFIG[1],logging,datetime).replace('"', r'')
nameMenuNodo=IdentifyJSON(f'{APPSETTING}',NAMEMENUNODO[0],NAMEMENUNODO[1],logging,datetime).replace('"', r'')
nameMenuAutomatizacion=IdentifyJSON(f'{APPSETTING}',NAMEMENUAUTO[0],NAMEMENUAUTO[1],logging,datetime).replace('"', r'')
nameMenuReport=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORT[0],NAMEMENUREPORT[1],logging,datetime).replace('"', r'')
nameMenuReportEflow=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTEFLOW[0],NAMEMENUREPORTEFLOW[1],logging,datetime).replace('"', r'')
nameMenuReportCitas=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTCITAS[0],NAMEMENUREPORTCITAS[1],logging,datetime).replace('"', r'')
nameMenuReportVirtualQueue=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTVQ[0],NAMEMENUREPORTVQ[1],logging,datetime).replace('"', r'')
nameMenuReportCitasConfig=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTCITASCONFIG[0],NAMEMENUREPORTCITASCONFIG[1],logging,datetime).replace('"', r'')
nameMenuReportCitasMSMQ=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTCITASMSMQ[0],NAMEMENUREPORTCITASMSMQ[1],logging,datetime).replace('"', r'')
nameMenuReportCitasMoreConfig=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTCITASMORECONFIG[0],NAMEMENUREPORTCITASMORECONFIG[1],logging,datetime).replace('"', r'')
nameMenuReportEncuesta=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTENCUESTA[0],NAMEMENUREPORTENCUESTA[1],logging,datetime).replace('"', r'')
nameMenuReportEncuestaConfig=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTENCUESTACONFIG[0],NAMEMENUREPORTENCUESTACONFIG[1],logging,datetime).replace('"', r'')
nameMenuReportVirtualQueue2=IdentifyJSON(f'{APPSETTING}',NAMEMENUREPORTVQ2[0],NAMEMENUREPORTVQ2[1],logging,datetime).replace('"', r'')
nameMenuDLL=IdentifyJSON(f'{APPSETTING}',NAMEMENUDLL[0],NAMEMENUDLL[1],logging,datetime).replace('"', r'')
nameMenuInternetOption=IdentifyJSON(f'{APPSETTING}',NAMEMENUINTERNETOPTION[0],NAMEMENUINTERNETOPTION[1],logging,datetime).replace('"', r'')
nameMenuTicketPrintingService=IdentifyJSON(f'{APPSETTING}',NAMEMENUTICKETPRINTINGSERVICE[0],NAMEMENUTICKETPRINTINGSERVICE[1],logging,datetime).replace('"', r'')
nameMenuAutoPlaylist=IdentifyJSON(f'{APPSETTING}',NAMEMENUAUTOPLAYLIST[0],NAMEMENUAUTOPLAYLIST[1],logging,datetime).replace('"', r'')
nameMenuResolution=IdentifyJSON(f'{APPSETTING}',NAMEMENURESOLUTION[0],NAMEMENURESOLUTION[1],logging,datetime).replace('"', r'')
nameMenuAutoLogon=IdentifyJSON(f'{APPSETTING}',NAMEMENUAUTOLOGON[0],NAMEMENUAUTOLOGON[1],logging,datetime).replace('"', r'')
nameMenuSI=IdentifyJSON(f'{APPSETTING}',NAMEMENUSCRIPTINICIO[0],NAMEMENUSCRIPTINICIO[1],logging,datetime).replace('"', r'')
nameMenuModificadorPuertoCitas=IdentifyJSON(f'{APPSETTING}',NAMEMENUPORTCITAS[0],NAMEMENUPORTCITAS[1],logging,datetime).replace('"', r'')
nameMenuDMSMQ=IdentifyJSON(f'{APPSETTING}',NAMEMENUMSMQ[0],NAMEMENUMSMQ[1],logging,datetime).replace('"', r'')
nameMenuUnblockFile=IdentifyJSON(f'{APPSETTING}',NAMEMENUUNBLOCKFILE[0],NAMEMENUUNBLOCKFILE[1],logging,datetime).replace('"', r'')
nameMenuTNC=IdentifyJSON(f'{APPSETTING}',NAMEMENUTNC[0],NAMEMENUTNC[1],logging,datetime).replace('"', r'')
nameMenuTNC=IdentifyJSON(f'{APPSETTING}',NAMEMENUTNC[0],NAMEMENUTNC[1],logging,datetime).replace('"', r'')
nameMenuConfigSuite=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGSUITE[0],NAMEMENUCONFIGSUITE[1],logging,datetime).replace('"', r'')
nameMenuConfigSuiteBBDD=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGSUITEBBDD[0],NAMEMENUCONFIGSUITEBBDD[1],logging,datetime).replace('"', r'')
nameMenuConfigSuiteIMCitas=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGSUITEIMCITAS[0],NAMEMENUCONFIGSUITEIMCITAS[1],logging,datetime).replace('"', r'')
nameMenuConfigApi=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGAPI[0],NAMEMENUCONFIGAPI[1],logging,datetime).replace('"', r'')
nameMenuSucApi=IdentifyJSON(f'{APPSETTING}',NAMEMENUSUCAPI[0],NAMEMENUSUCAPI[1],logging,datetime).replace('"', r'')
nameMenuDiagnosticoGeneral=IdentifyJSON(f'{APPSETTING}',NAMEMENUDIAGNOSTICADORDINAMICO[0],NAMEMENUDIAGNOSTICADORDINAMICO[1],logging,datetime).replace('"', r'')
nameMenuConfiguration1=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGURATION1[0],NAMEMENUCONFIGURATION1[1],logging,datetime).replace('"', r'')
nameMenuConfiguration2=IdentifyJSON(f'{APPSETTING}',NAMEMENUCONFIGURATION2[0],NAMEMENUCONFIGURATION2[1],logging,datetime).replace('"', r'')

#===Fuentes Menu principal y secundarios==
fontMenuPrincipal=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUPRINCIPAL[0],FONTMENUPRINCIPAL[1],logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuEflow=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUEFLOW[0],FONTMENUEFLOW[1],logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuClient=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUCLIENT[0],FONTMENUCLIENT[1],logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuCita=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUCITAS[0],FONTMENUCITAS[1],logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuEncuesta=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUENCUESTA[0],FONTMENUENCUESTA[1],logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuReporteria=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUREPORT[0],FONTMENUREPORT[1],logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuAutomatizacion=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUAUTO[0],FONTMENUAUTO[1],logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuDiagnostico=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUDIAGNOSTICO[0],FONTMENUDIAGNOSTICO[1],logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuApi=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUAPI[0],FONTMENUAPI[1],logging,datetime).replace('"', r''), size=12, weight="bold")
fontMenuSuite=font.Font(family=IdentifyJSON(f'{APPSETTING}',FONTMENUSUITE[0],FONTMENUSUITE[1],logging,datetime).replace('"', r''), size=12, weight="bold")

#===Fuentes Menu principal y secundarios==
widthMenuPrincipal=IdentifyJSON(f'{APPSETTING}',WIDTHMENUPRINCIPAL[0],WIDTHMENUPRINCIPAL[1],logging,datetime).replace('"', r'')
widthMenuEflow=IdentifyJSON(f'{APPSETTING}',WIDTHMENUEFLOW[0],WIDTHMENUEFLOW[1],logging,datetime).replace('"', r'')
widthMenuClient=IdentifyJSON(f'{APPSETTING}',WIDTHMENUCLIENT[0],WIDTHMENUCLIENT[1],logging,datetime).replace('"', r'')
widthMenuCita=IdentifyJSON(f'{APPSETTING}',WIDTHMENUCITAS[0],WIDTHMENUCITAS[1],logging,datetime).replace('"', r'')
widthMenuEncuesta=IdentifyJSON(f'{APPSETTING}',WIDTHMENUENCUESTA[0],WIDTHMENUENCUESTA[1],logging,datetime).replace('"', r'')
widthMenuReporteria=IdentifyJSON(f'{APPSETTING}',WIDTHMENUREPORT[0],WIDTHMENUREPORT[1],logging,datetime).replace('"', r'')
widthMenuAutomatizacion=IdentifyJSON(f'{APPSETTING}',WIDTHMENUAUTO[0],WIDTHMENUAUTO[1],logging,datetime).replace('"', r'')
widthMenuDiagnostico=IdentifyJSON(f'{APPSETTING}',WIDTHMENUDIAGNOSTICO[0],WIDTHMENUDIAGNOSTICO[1],logging,datetime).replace('"', r'')
widthMenuApi=IdentifyJSON(f'{APPSETTING}',WIDTHMENUAPI[0],WIDTHMENUAPI[1],logging,datetime).replace('"', r'')
widthMenuSuite=IdentifyJSON(f'{APPSETTING}',WIDTHMENUSUITE[0],WIDTHMENUSUITE[1],logging,datetime).replace('"', r'')

#===Fuentes Menu principal y secundarios==
heightMenuPrincipal=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUPRINCIPAL[0],HEIGHTMENUPRINCIPAL[1],logging,datetime).replace('"', r'')
heightMenuEflow=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUEFLOW[0],HEIGHTMENUEFLOW[1],logging,datetime).replace('"', r'')
heightMenuClient=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUCLIENT[0],HEIGHTMENUCLIENT[1],logging,datetime).replace('"', r'')
heightMenuCita=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUCITAS[0],HEIGHTMENUCITAS[1],logging,datetime).replace('"', r'')
heightMenuEncuesta=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUENCUESTA[0],HEIGHTMENUENCUESTA[1],logging,datetime).replace('"', r'')
heightMenuReporteria=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUREPORT[0],HEIGHTMENUREPORT[1],logging,datetime).replace('"', r'')
heightMenuAutomatizacion=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUAUTO[0],HEIGHTMENUAUTO[1],logging,datetime).replace('"', r'')
heightMenuDiagnostico=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUDIAGNOSTICO[0],HEIGHTMENUDIAGNOSTICO[1],logging,datetime).replace('"', r'')
heightMenuApi=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUAPI[0],HEIGHTMENUAPI[1],logging,datetime).replace('"', r'')
heightMenuSuite=IdentifyJSON(f'{APPSETTING}',HEIGHTMENUSUITE[0],HEIGHTMENUSUITE[1],logging,datetime).replace('"', r'')


#=======VARIABLES DETERMINADAS PARA FRAMES 

#Frame 1
var = IntVar()
R1 = Radiobutton(frame,text="Manual", variable=var, value=1, bg=colorMenuservice)
R2 = Radiobutton(frame, text="Automatico", variable=var, value=2,bg=colorMenuservice)
R1.place(x=0,y=40)
R2.place(x=0,y=60)
Textbox = tk.Entry(frame,width=60)
#place
Textbox.place(x=40,y=100)
#Config
Textbox.insert(1,"e-Flow MiddleWare Service")

#Frame 2
TextboxNameApplication = tk.Entry(frame2,width=60)
#place
TextboxNameApplication.place(x=40,y=100)
#Config
TextboxNameApplication.insert(1,"")

#Frame 4
#Se encarga de validar la entrada del textPort, donde el limite es tres caracter
def validate_entry(text):
    # Validar la entrada del usuario
    if len(text) <= 3:
        return True
    else:
        return False
TextboxPort = tk.Entry(frame4,width=5,validate="key", validatecommand=(frame4.register(validate_entry), '%P'))
TextboxPort.place(x=85,y=180)
TextboxPortURL = tk.Entry(frame4)
TextboxPortURL.place(x=85,y=200)
TextboxPortURL.insert(1,"localhost")
labelPortURL = tk.Label(frame4,text="url:",bg=colorMenuport)
labelPortURL.place(x=40,y=200)
labelPort = tk.Label(frame4,text="Puerto:",bg=colorMenuport)
#place
labelPort.place(x=40,y=180)

#Frame 5
#Declaracion de los label al frame5
labelsvr = tk.Label(frame5,text="Introduzca el nombre del servidor ",bg=colorframe5)
Textboxsvr = tk.Entry(frame5)
labelCitas = tk.Label(frame5,text="Introduzca el nombre del sitio de citas",bg=colorframe5)
TextboxCitas = tk.Entry(frame5)
labelEflow = tk.Label(frame5,text="Introduzca el nombre del sitio de e-Flow",bg=colorframe5)
TextboxEflow = tk.Entry(frame5)
labelMSMQ = tk.Label(frame5,text="Introduzca el nombre de la cola de mensajeria",bg=colorframe5)
TextboxMSMQ = tk.Entry(frame5)
labelSuiteConfig = tk.Label(frame5,text="Introduzca el nombre del sitio de suite",bg=colorframe5)
TextboxSuiteConfig = tk.Entry(frame5)
#place
Textboxsvr.place(x=40,y=80)
TextboxCitas.place(x=40,y=120)
TextboxEflow.place(x=40,y=160)
TextboxMSMQ.place(x=40,y=200)
TextboxSuiteConfig.place(x=40,y=240)
labelsvr.place(x=40,y=60)
labelCitas.place(x=40,y=100)
labelEflow.place(x=40,y=140)
labelMSMQ .place(x=40,y=180)
labelSuiteConfig .place(x=40,y=220)

#Frame 6
TextboxNameSite = tk.Entry(frame6,width=60)
labelPortHttp  = tk.Label(frame6,text="Introduzca el puerto del site",bg=colorframe5)
TextboxPortHttp = tk.Entry(frame6,width=5)
#place
labelPortHttp.place(x=40,y=180)
TextboxPortHttp.place(x=40,y=200)
TextboxNameSite.place(x=40,y=100)
#Config
TextboxPortHttp.insert(1,"")
TextboxNameSite.insert(1,"")

#Frame 7
#Declaracion de los label y textbox
labelsvr = tk.Label(frame7,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxsvrC = tk.Entry(frame7)
labelCache = tk.Label(frame7,text="Introduzca el nombre del Cache",bg=colorframe5)
TextboxCache = tk.Entry(frame7)
#place
TextboxsvrC.place(x=40,y=200)
TextboxCache.place(x=40,y=240)
labelsvr.place(x=40,y=180)
labelCache.place(x=40,y=220)

#Frame 8
labelsvr = tk.Label(frame8,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxsvrNME = tk.Entry(frame8)
labeleFlowNME = tk.Label(frame8,text="Introduzca el nombre de la aplicacion de e-Flow",bg=colorframe5)
TextboxeFlowNME = tk.Entry(frame8)
labelAPI = tk.Label(frame8,text="Introduzca el nombre de la API",bg=colorframe5)
TextboxeAPI = tk.Entry(frame8)
#place
TextboxsvrNME.place(x=40,y=160)
TextboxeFlowNME.place(x=40,y=200)
TextboxeAPI.place(x=40,y=240)
labelsvr.place(x=40,y=140)
labeleFlowNME.place(x=40,y=180)
labelAPI.place(x=40,y=220)

#Frame 9
labelsvrNMECitas = tk.Label(frame9,text="Introduzca el nombre del servidor del web service de citas ",bg=colorframe5)
TextboxsvrNMECitas = tk.Entry(frame9)
labelCitasNME = tk.Label(frame9,text="Introduzca el nombre de la aplicacion del web service de citas",bg=colorframe5)
TextboxCitasNME = tk.Entry(frame9)
#place
TextboxsvrNMECitas.place(x=40,y=160)
TextboxCitasNME.place(x=40,y=200)
labelsvrNMECitas.place(x=40,y=140)
labelCitasNME.place(x=40,y=180)

#Frame 10 RHI
hour=IntVar()
minute=IntVar()
labelHour = tk.Label(frame10,text="Introduzca la hora",bg=colorframe5)
spinHour = tk.Spinbox(frame10,from_=0, to=23, increment=1,width=2, textvariable=hour)
labelMinute = tk.Label(frame10,text="Introduzca el minuto",bg=colorframe5)
spinMinute = tk.Spinbox(frame10,from_=0, to=59, increment=1,width=2, textvariable=minute)
#place
spinHour.place(x=40,y=160)
spinMinute.place(x=40,y=200)
labelHour.place(x=40,y=140)
labelMinute.place(x=40,y=180)


#Frame 12
labelsvrEncuesta = tk.Label(frame12,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxsvrEncuesta = tk.Entry(frame12)
labelEncuesta = tk.Label(frame12,text="Introduzca el nombre de sitio de Encuesta",bg=colorframe5)
TextboxEncuesta = tk.Entry(frame12)
labelEflowEncuesta = tk.Label(frame12,text="Introduzca el nombre de sitio de e-Flow",bg=colorframe5)
TextboxEflowEncuesta = tk.Entry(frame12)
#place
TextboxsvrEncuesta.place(x=40,y=80)
TextboxEncuesta.place(x=40,y=120)
TextboxEflowEncuesta.place(x=40,y=160)
labelsvrEncuesta.place(x=40,y=60)
labelEncuesta.place(x=40,y=100)
labelEflowEncuesta.place(x=40,y=140)
#Config

#Frame 13 Console 
minuteSesion=IntVar()
labelMinuteConsole = tk.Label(frame13,text="Introduzca los minuto",bg=colorframe5)
spinMinuteConsole = tk.Spinbox(frame13,from_=0, to=1000, increment=1,width=5, textvariable=minuteSesion)
#place
spinMinuteConsole.place(x=40,y=200)
labelMinuteConsole.place(x=40,y=180)

#Frame 14
labelsvrSite = tk.Label(frame14,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxsvrNMESite = tk.Entry(frame14)
labeleFlowNMESite = tk.Label(frame14,text="Introduzca el puerto del site de e-Flow",bg=colorframe5)
TextboxeFlowNMESite = tk.Entry(frame14)
labelAPISite = tk.Label(frame14,text="Introduzca el puerto del site de API",bg=colorframe5)
TextboxeAPISite = tk.Entry(frame14)
#place
TextboxsvrNMESite.place(x=40,y=160)
TextboxeFlowNMESite.place(x=40,y=200)
TextboxeAPISite.place(x=40,y=240)
labelsvrSite.place(x=40,y=140)
labeleFlowNMESite.place(x=40,y=180)
labelAPISite.place(x=40,y=220)


#Frame 15 Emission.config 
preferencialVar=IntVar()
AnnounceAppointmentVar=IntVar()
preferencialTrue = Radiobutton(frame15,text="Si", variable=preferencialVar, value=1, bg=colorframe1,width=2)
preferencialFalse = Radiobutton(frame15, text="No", variable=preferencialVar, value=0,bg=colorframe1,width=2)
labelAppointment = tk.Label(frame15,text="Mostrar el boton de anunciar citas",bg=colorframe5).place(x=2,y=150)
AppointmentTrue = Radiobutton(frame15,text="Si", variable=AnnounceAppointmentVar, value=1, bg=colorframe1,width=2)
AppointmentFalse = Radiobutton(frame15, text="No", variable=AnnounceAppointmentVar, value=0,bg=colorframe1,width=2)
#place
preferencialTrue.place(x=2,y=100)
preferencialFalse.place(x=2,y=120)
AppointmentTrue.place(x=2,y=170)
AppointmentFalse.place(x=2,y=190)
#Config
preferencialVar.set(0)
AnnounceAppointmentVar.set(0)


#Frame 16
labelNodeFont= tk.Label(frame16,text="GENERAL: Font-Family",bg=colorframe5)
TextboxNodeFont = tk.Entry(frame16)
labelNodeVoice= tk.Label(frame16,text="GENERAL: Voz",bg=colorframe5)
TextboxNodeVoice = tk.Entry(frame16)
labelNodeLang= tk.Label(frame16,text="GENERAL: Idioma",bg=colorframe5)
TextboxNodeLang = tk.Entry(frame16)
labelNodeHeaderColor= tk.Label(frame16,text="HEADER: Color",bg=colorframe5)
TextboxNodeHeaderColor = tk.Entry(frame16)
labelNodeFooterColor= tk.Label(frame16,text="FOOTER: Color",bg=colorframe5)
TextboxNodeFooterColor = tk.Entry(frame16)
labelNodeNumberSize= tk.Label(frame16,text="NumberTableBodyandNewNumber: Size",bg=colorframe5)
TextboxNodeNumberSize = tk.Entry(frame16)
labelNodeW= tk.Label(frame16,text="HEADER: Width",bg=colorframe5)
TextboxNodeW = tk.Entry(frame16)
labelNodeUW= tk.Label(frame16,text="HEADER: Unit Width",bg=colorframe5)
TextboxNodeUW = tk.Entry(frame16)
labelNodeNumberTableHeaderColor= tk.Label(frame16b,text="NumberTableHeader: Color",bg=colorframe5)
TextboxNodeNumberTableHeaderColor = tk.Entry(frame16b)
labelNodeNumberTableHeaderSize= tk.Label(frame16b,text="NumberTableHeader: Size",bg=colorframe5)
TextboxNodeNumberTableHeaderSize = tk.Entry(frame16b)
labelNodeNumberTableHeaderfontColor= tk.Label(frame16b,text="NumberTableHeader: font Color",bg=colorframe5)
TextboxNodeNumberTableHeaderfontColor = tk.Entry(frame16b)
labelNodeBannerBackgroundColor= tk.Label(frame16b,text="BANNER: Background Color",bg=colorframe5)
TextboxNodeBannerBackgroundColor = tk.Entry(frame16b)
labelNodeBannerFontColor= tk.Label(frame16b,text="BANNER: font Color",bg=colorframe5)
botonNext = tk.Button(frame16,text="==>", command=lambda: show_frame(frame16,frame16b)).place(x=375,y=150)
botonBack = tk.Button(frame16b,text="<==", command=lambda: show_frame(frame16b,frame16)).place(x=2,y=150)
#place
labelNodeFont.place(x=40,y=80)
TextboxNodeFont.place(x=40,y=100)
labelNodeVoice.place(x=40,y=120)
TextboxNodeVoice.place(x=40,y=140)
labelNodeLang.place(x=40,y=160)
TextboxNodeLang.place(x=40,y=180)
labelNodeFooterColor.place(x=40,y=200)
TextboxNodeFooterColor.place(x=40,y=220)
labelNodeNumberSize.place(x=200,y=80)
TextboxNodeNumberSize.place(x=200,y=100)
labelNodeHeaderColor.place(x=200,y=120)
TextboxNodeHeaderColor.place(x=200,y=140)
labelNodeW.place(x=200,y=160)
TextboxNodeW.place(x=200,y=180)
labelNodeUW.place(x=200,y=200)
TextboxNodeUW.place(x=200,y=220)
TextboxNodeBannerFontColor = tk.Entry(frame16b)
labelNodeNumberTableHeaderColor.place(x=40,y=80)
TextboxNodeNumberTableHeaderColor.place(x=40,y=100)
labelNodeNumberTableHeaderSize.place(x=40,y=120)
TextboxNodeNumberTableHeaderSize.place(x=40,y=140)
labelNodeBannerBackgroundColor.place(x=200,y=80)
TextboxNodeBannerBackgroundColor.place(x=200,y=100)
labelNodeBannerFontColor.place(x=200,y=120)
TextboxNodeBannerFontColor.place(x=200,y=140)
#Config

#Frame 17
labelAutomatizadorSRVBD= tk.Label(frame17,text="Servidor de base de datos",bg=colorframe5)
TextboxAutomatizadorSRVBD = tk.Entry(frame17)
labelAutomatizadorSRVAPP= tk.Label(frame17,text="Servidor de APP",bg=colorframe5)
TextboxAutomatizadorSRVAPP = tk.Entry(frame17)
labelAutomatizadorName= tk.Label(frame17,text="Nombre del aplicativo",bg=colorframe5)
TextboxAutomatizadorName = tk.Entry(frame17)
eFlowvar = BooleanVar()
eFlow4var = BooleanVar()
citasvar = BooleanVar()
encuestavar = BooleanVar()
eFlow = Checkbutton(frame17, text = "e-Flow", variable = eFlowvar, onvalue = True, offvalue = False,height = 1, width = 7,justify='left',bg=colorframe5)
eFlow4 = Checkbutton(frame17, text = "e-Flow 4.X", variable = eFlow4var, onvalue = True, offvalue = False,height = 1, width = 7,justify='left',bg=colorframe5)
Citas = Checkbutton(frame17, text = "Citas", variable = citasvar, onvalue = True, offvalue = False,height = 1, width = 7,justify='left',bg=colorframe5)
Encuesta = Checkbutton(frame17, text = "Encuesta", variable = encuestavar, onvalue = True, offvalue = False,height = 1, width = 7,justify='left',bg=colorframe5)

#place
labelAutomatizadorSRVBD.place(x=40,y=80)
TextboxAutomatizadorSRVBD.place(x=40,y=100)
labelAutomatizadorSRVAPP.place(x=40,y=120)
TextboxAutomatizadorSRVAPP.place(x=40,y=140)
labelAutomatizadorName.place(x=40,y=160)
TextboxAutomatizadorName.place(x=40,y=180)
eFlow.place(x=290,y=80)
eFlow4.place(x=290,y=100)
Citas.place(x=290,y=120)
Encuesta.place(x=290,y=140)
#Frame 18
labelReporteriaEflow= tk.Label(frame18,text="e-Flow",bg=colorframe5)
labelReporteriaEflowService= tk.Label(frame18,text="",bg=colorframe5)
labelReporteriaCitas= tk.Label(frame18,text="Citas",bg=colorframe5)
labelReporteriaCitasService= tk.Label(frame18,text="",bg=colorframe5)
labelReporteriaEncuesta= tk.Label(frame18,text="Encuestas",bg=colorframe5)
labelReporteriaEncuestaService= tk.Label(frame18,text="",bg=colorframe5)
button2 = tk.Button(frame18,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame18,frameMenuReport)).place(x=280,y=270)
tree = ttk.Treeview(frame18, columns=("","e-Flow", "Citas", "Encuestas"),height=5, show="headings")
#place
tree.place(x=10,y=100)
#Config
tree.heading("", text="")
tree.heading("e-Flow", text="e-Flow")
tree.heading("Citas", text="Citas")
tree.heading("Encuestas", text="Encuestas")
tree.column("",width=60)
tree.column("e-Flow",width=100)
tree.column("Citas",width=100)
tree.column("Encuestas", width=100)

#Frame 19
#Declaracion de los label
labelReporteriaServiceEflow= tk.Label(frame19,text="Service",bg=colorframe5)
labelReporteriaServiceEflowDetail= tk.Label(frame19,text="",bg=colorframe5)
labelReporteriaIISEflow= tk.Label(frame19,text="IIS",bg=colorframe5,justify=tk.LEFT)
labelReporteriaUDLEflow= tk.Label(frame19,text="UDL",bg=colorframe5,justify=tk.LEFT)
button2 = tk.Button(frame19,width=16,height=1, text="Back to Reportes", command=lambda:show_frame(frame19,frameMenuReport)).place(x=275,y=270)
#place
labelReporteriaServiceEflow.place(x=40,y=106) 
labelReporteriaServiceEflowDetail.place(x=40,y=126) 
labelReporteriaUDLEflow.place(x=40,y=150) 
labelReporteriaIISEflow.place(x=40,y=180)
#Config

#Frame 20
labelReporteriaServiceCitas= tk.Label(frame20,text="Service",bg=colorframe5)
labelReporteriaServiceCitasDetail= tk.Label(frame20,text="",bg=colorframe5)
labelReporteriaIISCitas= tk.Label(frame20,text="IIS",bg=colorframe5,justify=tk.LEFT)
labelReporteriaUDLCitas= tk.Label(frame20,text="UDL",bg=colorframe5,justify=tk.LEFT)
button2 = tk.Button(frame20,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame20,frameMenuReport)).place(x=275,y=270)
button8 = tk.Button(frame20,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame20,frameMenuPrincipal)).place(x=275,y=240)
buttonRC1 = Button(frame20,bg="#000",fg="#FFF",width=15,height=1,text="Datos Basicos").place(x=0,y=100)
buttonRC2 = Button(frame20,width=15,height=1,text="Configuracion Citas", command=lambda:show_frame(frame20,frame20b)).place(x=0,y=130)
buttonRC3 = Button(frame20,width=15,height=1,text="MSMQ", command=lambda:show_frame(frame20,frame20c)).place(x=0,y=160)
buttonRC4 = Button(frame20,width=15,height=1,text="More Config",command=lambda:show_frame(frame20,frame20d)).place(x=0,y=190)
labelReporteriaCitasApplication= tk.Label(frame20b,text="Application.config",bg=colorframe5)
TextboxReporteriaCitasApplication = tk.Entry(frame20b)
labelReporteriaCitasAppSpa= tk.Label(frame20b,text="appSpa/index.html",bg=colorframe5)
TextboxReporteriaCitasAppSpa = tk.Entry(frame20b)
labelReporteriaCitasAttOpSpa= tk.Label(frame20b,text="AttOpSpa/index.html",bg=colorframe5)
TextboxReporteriaCitasAttOpSpa = tk.Entry(frame20b)
labelReporteriaCitasAppointmentWebIndex= tk.Label(frame20b,text="A.Web/index.html",bg=colorframe5)
TextboxReporteriaCitasAppointmentWebIndex = tk.Entry(frame20b)
labelReporteriaCitasAppointmentWebSetting= tk.Label(frame20b,text="settings.json",bg=colorframe5)
TextboxReporteriaCitasAppointmentWebSetting = tk.Entry(frame20b)
labelReporteriaCitasServiceSSP= tk.Label(frame20b,text="A.Service.exe.config",bg=colorframe5)
TextboxReporteriaCitasServiceSSP = tk.Entry(frame20b)
labelReporteriaCitasSTEWeb= tk.Label(frame20b,text="STE/Web.config'",bg=colorframe5)
TextboxReporteriaCitasSTEWeb = tk.Entry(frame20b)
labelReporteriaCitasNME= tk.Label(frame20b,text="emission.config.json",bg=colorframe5)
TextboxReporteriaCitasNME = tk.Entry(frame20b)
buttonRC1 = Button(frame20b,width=15,height=1,text="Datos Basicos",command=lambda:show_frame(frame20b,frame20)).place(x=0,y=100)
buttonRC2 = Button(frame20b,width=15,height=1,text="Configuracion Citas",bg="#000",fg="#FFF").place(x=0,y=130)
buttonRC3 = Button(frame20b,width=15,height=1,text="MSMQ", command=lambda:show_frame(frame20b,frame20c)).place(x=0,y=160)
buttonRC4 = Button(frame20b,width=15,height=1,text="More Config",command=lambda:show_frame(frame20b,frame20d)).place(x=0,y=190)
labelReporteriaCitasAppointmentWebConfig= tk.Label(frame20c,text="A.Web/Web.config",bg=colorframe5)
TextboxReporteriaCitasAppointmentWebConfig = tk.Entry(frame20c)
labelReporteriaCitasConfigFilesAppointment= tk.Label(frame20c,text="Appointment.config out",bg=colorframe5)
TextboxReporteriaCitasConfigFilesAppointment = tk.Entry(frame20c)
labelReporteriaCitasConfigFilesAppoinmentWeb= tk.Label(frame20c,text="Appointment.config web",bg=colorframe5)
TextboxReporteriaCitasConfigFilesAppoinmentWeb = tk.Entry(frame20c)
labelReporteriaCitasSSPServiceMSMQ= tk.Label(frame20c,text="A.Service.exe.config",bg=colorframe5)
TextboxReporteriaCitasSSPServiceMSMQ = tk.Entry(frame20c)
labelReporteriaCitasDataExport= tk.Label(frame20c,text="DataExport.config",bg=colorframe5)
TextboxReporteriaCitasDataExport = tk.Entry(frame20c)
buttonRC1 = Button(frame20c,width=15,height=1,text="Datos Basicos",command=lambda:show_frame(frame20c,frame20)).place(x=0,y=100)
buttonRC2 = Button(frame20c,width=15,height=1,text="Configuracion Citas", command=lambda:show_frame(frame20c,frame20b)).place(x=0,y=130)
buttonRC3 = Button(frame20c,width=15,height=1,text="MSMQ",bg="#000",fg="#FFF").place(x=0,y=160)
buttonRC4 = Button(frame20c,width=15,height=1,text="More Config",command=lambda:show_frame(frame20c,frame20d)).place(x=0,y=190)
labelReporteriaCitasAWebWA= tk.Label(frame20d,text="A/Web.configWA",bg=colorframe5)
TextboxReporteriaCitasAWebWA = tk.Entry(frame20d)
labelReporteriaCitasAWebSuite= tk.Label(frame20d,text="A/Web.configSuite",bg=colorframe5)
TextboxReporteriaCitasAWebSuite = tk.Entry(frame20d)
labelReporteriaCitasApplicationWA= tk.Label(frame20d,text="ApplicationWA",bg=colorframe5)
TextboxReporteriaCitasApplicationWA = tk.Entry(frame20d)
labelReporteriaCitasAWAWebbo= tk.Label(frame20d,text="AWA/Web.configbo",bg=colorframe5)
TextboxReporteriaCitasAWAWebbo = tk.Entry(frame20d)
labelReporteriaCitasAboindex= tk.Label(frame20d,text="Abo/index.html",bg=colorframe5)
TextboxReporteriaCitasAboindex = tk.Entry(frame20d)
labelReporteriaCitasabosettingAWA= tk.Label(frame20d,text="abosettingAWA",bg=colorframe5)
TextboxReporteriaCitasabosettingAWA = tk.Entry(frame20d)
labelReporteriaCitasabosettingA= tk.Label(frame20d,text="abosettingA",bg=colorframe5)
TextboxReporteriaCitasabosettingA = tk.Entry(frame20d)
labelReporteriaCitasabosettingSuite= tk.Label(frame20d,text="abosettingSuite",bg=colorframe5)
TextboxReporteriaCitasabosettingSuite = tk.Entry(frame20d)

buttonRC1 = Button(frame20d,width=15,height=1,text="Datos Basicos",command=lambda:show_frame(frame20d,frame20)).place(x=0,y=100)
buttonRC2 = Button(frame20d,width=15,height=1,text="Configuracion Citas", command=lambda:show_frame(frame20d,frame20b)).place(x=0,y=130)
buttonRC3 = Button(frame20d,width=15,height=1,text="MSMQ",command=lambda:show_frame(frame20d,frame20c)).place(x=0,y=160)
buttonRC4 = Button(frame20d,width=15,height=1,text="More Config",bg="#000",fg="#FFF").place(x=0,y=190)

#place
labelReporteriaCitasApplication.place(x=120,y=90)
TextboxReporteriaCitasApplication.place(x=120,y=110)
labelReporteriaCitasAppSpa.place(x=120,y=130)
TextboxReporteriaCitasAppSpa.place(x=120,y=150)
labelReporteriaCitasAttOpSpa.place(x=280,y=90)
TextboxReporteriaCitasAttOpSpa.place(x=280,y=110)
labelReporteriaCitasAppointmentWebIndex.place(x=280,y=130)
TextboxReporteriaCitasAppointmentWebIndex.place(x=280,y=150)
labelReporteriaCitasAppointmentWebSetting.place(x=120,y=170)
TextboxReporteriaCitasAppointmentWebSetting.place(x=120,y=190)
labelReporteriaCitasServiceSSP.place(x=120,y=210)
TextboxReporteriaCitasServiceSSP.place(x=120,y=230)
labelReporteriaCitasSTEWeb.place(x=280,y=170)
TextboxReporteriaCitasSTEWeb.place(x=280,y=190)
labelReporteriaCitasNME.place(x=280,y=210)
TextboxReporteriaCitasNME.place(x=280,y=230)
labelReporteriaServiceCitas.place(x=120,y=106) #se agregan las etiquetas al frame20
labelReporteriaServiceCitasDetail.place(x=120,y=126) #se agregan las etiquetas al frame20
labelReporteriaUDLCitas.place(x=120,y=150) #se agregan las etiquetas al frame20
labelReporteriaIISCitas.place(x=120,y=180) #se agregan las etiquetas al frame20
labelReporteriaCitasAppointmentWebConfig.place(x=120,y=90)
TextboxReporteriaCitasAppointmentWebConfig.place(x=120,y=110)
labelReporteriaCitasConfigFilesAppointment.place(x=120,y=130)
TextboxReporteriaCitasConfigFilesAppointment.place(x=120,y=150)
labelReporteriaCitasConfigFilesAppoinmentWeb.place(x=280,y=90)
TextboxReporteriaCitasConfigFilesAppoinmentWeb.place(x=280,y=110)
labelReporteriaCitasSSPServiceMSMQ.place(x=280,y=130)
TextboxReporteriaCitasSSPServiceMSMQ.place(x=280,y=150)
labelReporteriaCitasDataExport.place(x=120,y=170)
TextboxReporteriaCitasDataExport.place(x=120,y=190)
labelReporteriaCitasAWebWA.place(x=120,y=90)
TextboxReporteriaCitasAWebWA.place(x=120,y=110)
labelReporteriaCitasAWebSuite.place(x=120,y=130)
TextboxReporteriaCitasAWebSuite.place(x=120,y=150)
labelReporteriaCitasApplicationWA.place(x=280,y=90)
TextboxReporteriaCitasApplicationWA.place(x=280,y=110)
labelReporteriaCitasAWAWebbo.place(x=280,y=130)
TextboxReporteriaCitasAWAWebbo.place(x=280,y=150)
labelReporteriaCitasAboindex.place(x=120,y=170)
TextboxReporteriaCitasAboindex.place(x=120,y=190)
labelReporteriaCitasabosettingAWA.place(x=120,y=210)
TextboxReporteriaCitasabosettingAWA.place(x=120,y=230)
labelReporteriaCitasabosettingA.place(x=280,y=170)
TextboxReporteriaCitasabosettingA.place(x=280,y=190)
labelReporteriaCitasabosettingSuite.place(x=280,y=210)
TextboxReporteriaCitasabosettingSuite.place(x=280,y=230)
#Frame 21
labelReporteriaServiceEncuesta= tk.Label(frame21,text="Service",bg=colorframe5)
labelReporteriaServiceEncuestaDetail= tk.Label(frame21,text="",bg=colorframe5)
labelReporteriaIISEncuesta= tk.Label(frame21,text="IIS",bg=colorframe5,justify=tk.LEFT)
labelReporteriaUDLEncuesta= tk.Label(frame21,text="UDL",bg=colorframe5,justify=tk.LEFT)
button2 = tk.Button(frame21,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame21,frameMenuReport)).place(x=275,y=270)
button8 = tk.Button(frame21,width=16,height=1, text="Back to Inicio", command=lambda: show_frame(frame21,frameMenuPrincipal)).place(x=275,y=240)
buttonRE1 = Button(frame21,width=15,height=1,text="Datos Basicos",bg="#000",fg="#FFF").place(x=0,y=100)
buttonRE2 = Button(frame21,width=15,height=1,text="Configuracion",command=lambda:show_frame(frame21,frame21b)).place(x=0,y=150)
buttonImpresora = tk.Button(frame21, text="",image=impresora ,command=lambda: show_frame(frame21,frameConfiguracionColoresPrincipales)).place(x=305,y=55)

labelReporteriaSTEWebConfig= tk.Label(frame21b,text="STE/Web.config",bg=colorframe5)
TextboxReporteriaSTEWebConfig = tk.Entry(frame21b)
labelReporteriaReportePoll= tk.Label(frame21b,text="Reporte/index.html",bg=colorframe5)
TextboxReporteriaReportePoll = tk.Entry(frame21b)
labelReporteriaOpinionPollIndex= tk.Label(frame21b,text="O./index.html",bg=colorframe5)
TextboxReporteriaOpinionPollIndex = tk.Entry(frame21b)
labelReporteriaSettingPoll= tk.Label(frame21b,text="Setting.json",bg=colorframe5)
TextboxReporteriaSettingPoll = tk.Entry(frame21b)
labelReporteriaMiddlewareOpinionPoll= tk.Label(frame21b,text="M/O/OpinionPoll.config",bg=colorframe5)
TextboxReporteriaMiddlewareOpinionPoll = tk.Entry(frame21b)
labelReporteriaMiddlewareSTE= tk.Label(frame21b,text="M/S/OpinionPoll.config",bg=colorframe5)
TextboxReporteriaMiddlewareSTE = tk.Entry(frame21b)
button2 = tk.Button(frame21b,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame21b,frameMenuReport)).place(x=275,y=270)
buttonRE1 = Button(frame21b,width=15,height=1,text="Datos Basicos",command=lambda:show_frame(frame21b,frame21)).place(x=0,y=100)
buttonRE2 = Button(frame21b,width=15,height=1,text="Configuracion",bg="#000",fg="#FFF").place(x=0,y=150)
buttonImpresora = tk.Button(frame21b, text="",image=impresora ,command=lambda: show_frame(frame21b,frameConfiguracionColoresPrincipales)).place(x=305,y=55)
#place
labelReporteriaServiceEncuesta.place(x=120,y=106) #se agregan las etiquetas al frame21
labelReporteriaServiceEncuestaDetail.place(x=120,y=126) #se agregan las etiquetas al frame21
labelReporteriaUDLEncuesta.place(x=120,y=150) #se agregan las etiquetas al frame21
labelReporteriaIISEncuesta.place(x=120,y=180) #se agregan las etiquetas al frame21
labelReporteriaSTEWebConfig.place(x=120,y=90)
TextboxReporteriaSTEWebConfig.place(x=120,y=110)
labelReporteriaReportePoll.place(x=120,y=130)
TextboxReporteriaReportePoll.place(x=120,y=150)
labelReporteriaOpinionPollIndex.place(x=280,y=90)
TextboxReporteriaOpinionPollIndex.place(x=280,y=110)
labelReporteriaSettingPoll.place(x=280,y=130)
TextboxReporteriaSettingPoll.place(x=280,y=150)
labelReporteriaMiddlewareOpinionPoll.place(x=120,y=170)
TextboxReporteriaMiddlewareOpinionPoll.place(x=120,y=190)
labelReporteriaMiddlewareSTE.place(x=280,y=170)
TextboxReporteriaMiddlewareSTE.place(x=280,y=190)
#Frame 22
labelReporteriaVQDB= tk.Label(frame22,text="DB Conection",bg=colorframe5)
TextboxReporteriaVQDB = tk.Entry(frame22,width=50)
labelReporteriaVQMSMQWebConfig= tk.Label(frame22,text="MSMQ/Web.config",bg=colorframe5)
TextboxReporteriaVQMSMQWebConfig = tk.Entry(frame22,width=50)
labelReporteriaVQMSMQMiddlewareSTE= tk.Label(frame22,text="MSMQ/MiddlewareSTE",bg=colorframe5)
TextboxReporteriaVQMSMQMiddlewareSTE = tk.Entry(frame22,width=50)
#place
labelReporteriaVQDB.place(x=40,y=90)
TextboxReporteriaVQDB.place(x=40,y=110)
labelReporteriaVQMSMQWebConfig.place(x=40,y=130)
TextboxReporteriaVQMSMQWebConfig.place(x=40,y=150)
labelReporteriaVQMSMQMiddlewareSTE.place(x=40,y=170)
TextboxReporteriaVQMSMQMiddlewareSTE.place(x=40,y=190)
button2 = tk.Button(frame22,width=16,height=1, text="Back to Reportes", command=lambda: show_frame(frame22,frameMenuReport)).place(x=275,y=270)

#Frame 24
labelsvrIO = tk.Label(frame24,text="Introduzca el nombre del servidor ",bg=colorframe5)
TextboxsvrIO = tk.Entry(frame24)
#place
TextboxsvrIO.place(x=40,y=160)
labelsvrIO.place(x=40,y=140)

#Frame 25
labelProtocolo= tk.Label(frame25,text="Protocolo",bg=colorframe5)
TextboxProtocolo = tk.Entry(frame25)
labelUrl= tk.Label(frame25,text="Url",bg=colorframe5)
TextboxUrl = tk.Entry(frame25)
labelstylepath= tk.Label(frame25,text="stylepath",bg=colorframe5)
Textboxstylepath = tk.Entry(frame25)
labelimgpath= tk.Label(frame25,text="imgpath",bg=colorframe5)
Textboximgpath = tk.Entry(frame25)
labelticketImg= tk.Label(frame25,text="ticketImg",bg=colorframe5)
TextboxticketImg = tk.Entry(frame25)
#place
labelProtocolo.place(x=40,y=80)
TextboxProtocolo.place(x=40,y=100)
labelUrl.place(x=180,y=80)
TextboxUrl.place(x=180,y=100)
labelstylepath.place(x=40,y=120)
Textboxstylepath.place(x=40,y=140)
labelimgpath.place(x=40,y=160)
Textboximgpath.place(x=40,y=180)
labelticketImg.place(x=40,y=200)
TextboxticketImg.place(x=40,y=220)

#Frame 26
labelUrlEflow = tk.Label(frame26,text="Introduzca el nombre de la url de e-Flow ",bg=colorframe5)
TextboxUrlEflow = tk.Entry(frame26)
#place
TextboxUrlEflow.place(x=40,y=160)
labelUrlEflow.place(x=40,y=140)

#Frame 27
labelSelectResolution = tk.Label(frame27,text="Seleccione la resolucion indicada",bg=colorframe5)
TextboxSelectResolution = ttk.Combobox(frame27,state="readonly",values=cargarResolucion(logging,datetime))
#place
TextboxSelectResolution.place(x=40,y=160)
labelSelectResolution.place(x=40,y=140)

#Frame 28
labelALName= tk.Label(frame28,text="Name",bg=colorframe5)
TextboxALName = tk.Entry(frame28)
labelALDomain= tk.Label(frame28,text="Dominio",bg=colorframe5)
TextboxALDomain = tk.Entry(frame28)
labelALPassword= tk.Label(frame28,text="Password",bg=colorframe5)
TextboxALPassword = tk.Entry(frame28)
#place
labelALName.place(x=40,y=80)
TextboxALName.place(x=40,y=100)
labelALDomain.place(x=180,y=80)
TextboxALDomain.place(x=180,y=100)
labelALPassword.place(x=40,y=120)
TextboxALPassword.place(x=40,y=140)

#Frame 29
def setScript():
  try:label29.config(text=f'start {browser.get()} {fullscreen.get().split(",",3)[0]} --new-window "{url.get()}" --window-position="{xBrowserVar.get()},{yBrowserVar.get()}" {fullscreen.get().split(",",3)[1]}')
  except: label29.config(text=f'start {browser.get()}  --new-window "{url.get()}" --window-position="{xBrowserVar.get()},{yBrowserVar.get()}"')
  
  label29.place(x=0,y=180)
browser=StringVar()
fullscreen=StringVar()
url=StringVar()

browser.set("chrome.exe")

chkbtn1 = Checkbutton(frame29, text = "Fullscreen", variable = fullscreen, onvalue = "--kiosk,--edge-kiosk-type=fullscreen", offvalue = "", command=setScript,height = 1, width = 7)  

xBrowserVar=IntVar()
xBrowserLabel = tk.Label(frame29,text="X",bg=colorframe5)
xBrowser = tk.Spinbox(frame29,from_=0, to=5000, increment=1,width=5, textvariable=xBrowserVar,command=setScript)
xBrowserLabel.place(x=5,y=130)
xBrowser.place(x=20,y=130)
yBrowserVar=IntVar()
yBrowserLabel = tk.Label(frame29,text="Y",bg=colorframe5)
yBrowser = tk.Spinbox(frame29,from_=0, to=5000, increment=1,width=5, textvariable=yBrowserVar,command=setScript)
yBrowserLabel.place(x=5,y=150)
yBrowser.place(x=20,y=150)
def callback(url): setScript()
url.trace("w", lambda name, index, mode, url=url:callback(url))
url.set("http://localhost/ste")
browserChrome = Radiobutton(frame29,text="chrome", variable=browser, value="chrome.exe",command=setScript, bg=colorframe1,width=6).place(x=5,y=70)
browserEdge = Radiobutton(frame29, text="msedge", variable=browser, value="msedge.exe",command=setScript,bg=colorframe1,width=6).place(x=85,y=70)
browserExplrer = Radiobutton(frame29, text="IExplorer", variable=browser, value="IExplorer",command=setScript,bg=colorframe1,width=6).place(x=160,y=70)

chkbtn1.place(x=5,y=100)
browserURLLabel= tk.Label(frame29,text="URL",bg=colorframe5)
browserURL = tk.Entry(frame29,textvariable=url,validatecommand=setScript)
browserURLLabel.place(x=130,y=100)
browserURL.place(x=160,y=100)



labelSelectResolution = tk.Label(frame27,text="Seleccione la resolucion indicada",bg=colorframe5)
TextboxSelectResolution = ttk.Combobox(frame27,state="readonly",values=cargarResolucion(logging,datetime))
#place
TextboxSelectResolution.place(x=40,y=160)
labelSelectResolution.place(x=40,y=140)

#Frame 33
labelTNCUrl  = tk.Label(frame33,text="ip o hostname",bg=colorMenuport)
TextboxTNCUrl= tk.Entry(frame33,width=20)
labelTNCPort  = tk.Label(frame33,text="puerto",bg=colorMenuport)
TextboxTNCPort = tk.Entry(frame33,width=6)
labelResult  = tk.Label(frame33,text="",bg=colorMenuport,justify="left")
#place
labelTNCUrl.place(x=10,y=100)
labelTNCPort.place(x=10,y=140)
TextboxTNCPort.place(x=10,y=160)
TextboxTNCUrl.place(x=10,y=120)
labelResult.place(x=140,y=80)
#Config
TextboxTNCPort.insert(1,"")
TextboxTNCUrl.insert(1,"")

#Frame 34
labelHostSuite  = tk.Label(frame34,text="ip o hostname",bg=colorMenuport)
TextboxHostSuite= tk.Entry(frame34,width=20)
labelSiteSuite  = tk.Label(frame34,text="Site de Suite",bg=colorMenuport)
TextboxSiteSuite= tk.Entry(frame34,width=20)
labelSiteIm  = tk.Label(frame34,text="Site de IM",bg=colorMenuport)
TextboxSiteIm = tk.Entry(frame34,width=20)
#place
labelHostSuite.place(x=10,y=100)
labelSiteSuite.place(x=10,y=140)
labelSiteIm.place(x=10,y=180)
TextboxHostSuite.place(x=10,y=120)
TextboxSiteSuite.place(x=10,y=160)
TextboxSiteIm.place(x=10,y=200)
#Config
TextboxHostSuite.insert(1,"")
TextboxSiteSuite.insert(1,"")
TextboxSiteIm.insert(1,"")


#Frame configuraciones
buttonC1 = Button(frameConfiguracionColoresPrincipales,bg="#000",fg="#FFF",width=15,height=1,text="Colores principales").place(x=0,y=100)
buttonC2 = Button(frameConfiguracionColoresPrincipales,width=15,height=1,text="Colores Secundarios", command=lambda:show_frame(frameConfiguracionColoresPrincipales,frameConfiguracionColoresSecundarios)).place(x=0,y=150)
OPTIONS = getColors() #etc
labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="Instalador Servicio",bg=colorframeC)
labelColor1.place(x=120,y=70)
labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="Creador de aplicaciones",bg=colorframeC)
labelColor1.place(x=120,y=110)
labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="modificador de udl",bg=colorframeC)
labelColor1.place(x=120,y=150)
labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="modificador de puertos",bg=colorframeC)
labelColor1.place(x=120,y=190)
labelColor1 = tk.Label(frameConfiguracionColoresPrincipales,text="configurador de citas",bg=colorframeC)
labelColor1.place(x=120,y=230)
comboBoxColo1 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor1, *OPTIONS)
comboBoxColo1.place(x=270,y=65,width=100)
comboBoxColo2 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor2, *OPTIONS)
comboBoxColo2.place(x=270,y=105,width=100)
comboBoxColo3 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor3, *OPTIONS)
comboBoxColo3.place(x=270,y=145,width=100)
comboBoxColo4 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor4, *OPTIONS)
comboBoxColo4.place(x=270,y=185,width=100)
comboBoxColo5 = OptionMenu(frameConfiguracionColoresPrincipales, variableColor5, *OPTIONS)
comboBoxColo5.place(x=270,y=225,width=100)
buttonC1 = Button(frameConfiguracionColoresSecundarios,width=15,height=1,text="Colores principales", command=lambda:show_frame(frameConfiguracionColoresSecundarios,frameConfiguracionColoresPrincipales)).place(x=0,y=100)
buttonC2 = Button(frameConfiguracionColoresSecundarios,bg="#000",fg="#FFF",width=15,height=1,text="Colores Secundarios").place(x=0,y=150)
#place

#Frame 30
#Declaracion de los label
TextboxPortAppointment = tk.Entry(frame30,width=5,validate="key", validatecommand=(frame4.register(validate_entry), '%P'))
TextboxPortAppointment.place(x=85,y=180)
labelPortAppointment = tk.Label(frame30,text="Puerto:",bg=colorMenuport)
#place
labelPortAppointment.place(x=40,y=180)
TextboxPortURLAppointment = tk.Entry(frame30)
TextboxPortURLAppointment.place(x=85,y=200)
TextboxPortURLAppointment.insert(1,"localhost")
labelPortURLAppointment = tk.Label(frame30,text="url:",bg=colorMenuport)
labelPortURLAppointment.place(x=40,y=200)

#Frame31
labelMSMQ = tk.Label(frame31,justify='left',text="""Formato de la MSMQ:\n.\private$\[colademensajeria]\nFormatName:DIRECT=TCP:[IP]\private$\[colademensajeria]\nFormatName:DIRECT=TCP:[HOSTNAME]\private$\[colademensajeria]""",bg=colorMenuport)
labelMSMQ.place(x=0,y=50)
labelMSMQEntry = tk.Label(frame31,text="MSMQ:",bg=colorMenuport)
labelMSMQEntry.place(x=0,y=120)
TextboxMSMQEntry = tk.Entry(frame31,width='48')
TextboxMSMQEntry.place(x=45,y=120)
labelMSMQSend = tk.Label(frame31,text="mensaje enviados",bg=colorMenuport,foreground='#0F0')
labelMSMQSend.place(x=0,y=180)
labelMSMQReceived = tk.Label(frame31,text="mensaje recibidos",bg=colorMenuport,foreground='#0F0')
labelMSMQReceived.place(x=0,y=200)

#Frame 35
labelIMDB= tk.Label(frame35,text="DB Conection",bg=colorframe5)
TextboxIMDB = tk.Entry(frame35,width=50)
#place
labelIMDB.place(x=40,y=110)
TextboxIMDB.place(x=40,y=130)
TextboxIMDB.insert(1,"Server=.;Database=******;Integrated Security=False;User Id=***********;Password=*******; TrustServerCertificate=true;")

#Frame 36 "..\MiddleWare\Appointment\ConfigFiles\IMIntegration.config"
labelCitasIm= tk.Label(frame36,text="identityManager",bg=colorframe5)
TextboxCitasIm = tk.Entry(frame36,width=30)
labeltenantAppointment= tk.Label(frame36,text="tenantAppointment",bg=colorframe5)
TextboxtenantAppointment = tk.Entry(frame36,width=30)
labelUserNameAdminTenant= tk.Label(frame36,text="UserNameAdminTenant",bg=colorframe5)
TextboxUserNameAdminTenant = tk.Entry(frame36,width=30)
labelPasswordAdminTenant= tk.Label(frame36,text="PasswordAdminTenant",bg=colorframe5)
TextboxPasswordAdminTenant = tk.Entry(frame36,width=30)
labelClientIdAppointment= tk.Label(frame36,text="ClientIdAppointment",bg=colorframe5)
TextboxClientIdAppointment = tk.Entry(frame36,width=30)
labelClientSecretAppointment= tk.Label(frame36,text="ClientSecretAppointment",bg=colorframe5)
TextboxClientSecretAppointment = tk.Entry(frame36,width=30)
#place
labelCitasIm.place(x=4,y=90)
TextboxCitasIm.place(x=4,y=110)
labeltenantAppointment.place(x=4,y=130)
TextboxtenantAppointment.place(x=4,y=150)
labelUserNameAdminTenant.place(x=4,y=170)
TextboxUserNameAdminTenant.place(x=4,y=190)
labelPasswordAdminTenant.place(x=200,y=90)
TextboxPasswordAdminTenant.place(x=200,y=110)
labelClientIdAppointment.place(x=200,y=130)
TextboxClientIdAppointment.place(x=200,y=150)
labelClientSecretAppointment.place(x=200,y=170)
TextboxClientSecretAppointment.place(x=200,y=190)

#Configuracion del Menu
menu.title("Instalador de servicios Unicos V0.800")
menu.geometry(sizeVentana)
menu.config(relief="sunken") 
menu.config(bg="blue")          # color de fondo, background
menu.config(bd=25)  
menu.resizable(resizable, resizable)
menu.iconphoto(True, icono)

# Agregarlo a la barra.
barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
barra_menus.add_cascade(menu=menu_opciones, label="Configuracion")
menu.config(menu=barra_menus)

#Esta funcion se encarga de cargar directamente desde la base de datos los colores de los 5 frame
def loadColor(color,component):
  for components  in component:
    components[0].config(bg= color)
    components[8].config(bg= color)
  pass