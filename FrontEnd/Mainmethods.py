from FrontEnd.Reports import *
from FrontEnd.Client import startingInstallDLL,startingconfigureOptionInternet,startingconfigureTicketPrintingService,startingconfigureAutoplaylist,startingconfigureTicketPrintingService,startingUpdateTicketPrintingService,startingConfigureResolution,startingConfigureAutoLogon,startingCreationScript,startingUnblockingFolder,startingTest
from FrontEnd.RHI import ExamineDirectoryRHI,modifyRHI
from FrontEnd.NME import ExamineDirectoryNME,modifyNME,modifyNMEEmissionConfig,modifyNMESite,modifyNMECitas
from FrontEnd.Consola import ExamineDirectoryConsoleSesion,modifyConsoleSesion
from FrontEnd.iis import createSite,createAplication
from FrontEnd.portService import modifyPort,modifyPortAppointment
from FrontEnd.NCache import modifyNCache
from FrontEnd.Nodo import Examine,modifyNode
from FrontEnd.udl import modifyUDL
from FrontEnd.Mail import modifyMail
from FrontEnd.Citas import modifyAppointment,updateAppointment,loadDataAppointment
from FrontEnd.Encuestas import modifyPoll,updatePoll
from FrontEnd.automateProcess import automateProcess
from FrontEnd.Service import executeScript
from FrontEnd.Api import startingRequest
from FrontEnd.Virtualqueue import updateVirtualQueue
from FrontEnd.MSMQ import validateMSMQ
from FrontEnd.Suite import startingConfigSuite,startingConfigSuiteBBDD,ExamineDirectorySuiteCitas,startingConfigSuiteAppointment
import tkinter.filedialog

#esta funcion se encarga de Seleccionar el directorio donde se creara la aplicacion
def ExamineDirectory(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la creacion de la aplicacion')
  Path = tkinter.filedialog.askdirectory()
  logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
  Path = Path.replace("/", r"\ ".strip())
  Path=Path.rstrip()
  label.config(text=Path) 
  return Path

def new_Archive(event=None):
    print("¡Has presionado para crear un nuevo archivo!")
def saveDataConfiguration():
  logging.info(f' {datetime.datetime.now() }: guardando los datos de configuracion')
  #setConfiguration([fixWord(variableColor1.get()),1],[fixWord(variableColor2.get()),2],[fixWord(variableColor3.get()),3], [fixWord(variableColor4.get()),4],[fixWord(variableColor5.get()),5],logging,datetime.datetime.now())
  loadColor([getColor(1,"codigo"),getColor(2,"codigo"),getColor(3,"codigo"),getColor(4,"codigo"),getColor(5,"codigo")])
  tk.messagebox.showinfo(title="Los cambios se guardaron satisfactoriamente", message="Los cambios se guardaron satisfactoriamente \nPara ver los cambios, dar click en volver")




menu_archivo.add_command( label="Nuevo",accelerator="Ctrl+N",command=new_Archive)
menu_opciones.add_command(label="Configurar",accelerator="Ctrl+c",command=lambda:show_Configuration(frame,frame2,frame3,frame4,frame5,frameMenuPrincipal,frameConfiguracionColoresPrincipales))
