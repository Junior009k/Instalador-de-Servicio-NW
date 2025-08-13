from FrontEnd.VariableDeterminadas import *

#esta funcion se encarga de configurar las citas
def modifyAppointment():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  Citas')
  bandera=validateField(TextboxCitas,logging,MessageBox,"cita","del servidor",datetime)
  bandera=bandera*validateField(TextboxMSMQ,logging,MessageBox,"cita","el nombre de la cola de mensajeria",datetime)
  bandera=bandera*validateField(TextboxEflow,logging,MessageBox,"cita","del sitio de e-Flow",datetime)
  bandera=bandera*validateLabel(label5,logging,MessageBox,"cita","la ruta",datetime)
  if( validateDirectory(label5.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label5.cget("text"),"FrontEnd",logging,datetime)):label5.config(text="") 
  bandera=bandera*validateLabel(label5,logging,MessageBox,"cita","tiene que estar en la carpeta del aplicativo")
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de citas')
    configurarCitas(label5.cget("text"),Textboxsvr.get(),TextboxCitas.get(),TextboxEflow.get(),TextboxMSMQ.get(),logging,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El aplicativo de cita termino el proceso de configuracion de los archivos")

#esta funcion se encarga de actualizar los campos en citas
def updateAppointment():
  TextboxReporteriaCitasAWAWebbo.delete(0, tk.END)  
  updateCitas(label20.cget("text"),TextboxReporteriaCitasAppSpa.get(),TextboxReporteriaCitasAttOpSpa.get(),TextboxReporteriaCitasApplication.get(),TextboxReporteriaCitasAppointmentWebIndex.get(),TextboxReporteriaCitasAppointmentWebSetting.get(),TextboxReporteriaCitasSTEWeb.get(),TextboxReporteriaCitasServiceSSP.get(),TextboxReporteriaCitasNME.get(),TextboxReporteriaCitasAppointmentWebConfig.get(),TextboxReporteriaCitasConfigFilesAppointment.get(),TextboxReporteriaCitasConfigFilesAppoinmentWeb.get(),TextboxReporteriaCitasSSPServiceMSMQ.get(),TextboxReporteriaCitasDataExport.get(),TextboxReporteriaCitasAWebWA.get(),TextboxReporteriaCitasAWebSuite.get(),TextboxReporteriaCitasApplicationWA.get(),TextboxReporteriaCitasAWAWebbo.get(),TextboxReporteriaCitasAboindex.get(),TextboxReporteriaCitasabosettingAWA.get(), TextboxReporteriaCitasabosettingA.get, TextboxReporteriaCitasabosettingSuite.get(),logging,datetime)

#esta funcion se encarga de actualizar los campos en citas
def loadDataAppointment(path):
  TextboxReporteriaCitasApplication.delete(0, tk.END)
  TextboxReporteriaCitasAppSpa.delete(0, tk.END)
  TextboxReporteriaCitasAttOpSpa.delete(0, tk.END)
  TextboxReporteriaCitasAppointmentWebIndex.delete(0, tk.END)
  TextboxReporteriaCitasAppointmentWebSetting.delete(0, tk.END)
  TextboxReporteriaCitasSTEWeb.delete(0, tk.END)
  TextboxReporteriaCitasServiceSSP.delete(0, tk.END)
  TextboxReporteriaCitasNME.delete(0, tk.END)
  TextboxReporteriaCitasAppointmentWebConfig.delete(0, tk.END)
  TextboxReporteriaCitasConfigFilesAppointment.delete(0, tk.END)
  TextboxReporteriaCitasConfigFilesAppoinmentWeb.delete(0, tk.END)
  TextboxReporteriaCitasSSPServiceMSMQ.delete(0, tk.END)
  TextboxReporteriaCitasDataExport.delete(0, tk.END)  
  TextboxReporteriaCitasAWebWA.delete(0, tk.END)  
  TextboxReporteriaCitasAWebSuite.delete(0, tk.END)  
  TextboxReporteriaCitasApplicationWA.delete(0, tk.END)  
  TextboxReporteriaCitasAWAWebbo.delete(0, tk.END)  
  TextboxReporteriaCitasAboindex.delete(0, tk.END)  
  TextboxReporteriaCitasabosettingAWA.delete(0, tk.END)  
  TextboxReporteriaCitasabosettingA.delete(0, tk.END)  
  TextboxReporteriaCitasabosettingSuite.delete(0, tk.END)  
  
  Insert(TextboxReporteriaCitasApplication,Identify(f"{path}/FrontEnd/Appointment/bin/Application.config",'<OperationalPath>[\S|\\b|" "]+</OperationalPath>','<OperationalPath>[\S|\\b|" "]+</OperationalPath>',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasAppSpa,identifyBaseURL(f"{path}/FrontEnd/Appointment/appSpa/index.html",'<base href=[\S|\\b|" "]+','<base href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasAttOpSpa,identifyBaseURL(f"{path}/FrontEnd/Appointment/AttOpSpa/index.html",'<base href=[\S|\\b|" "]+','<base href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasAppointmentWebIndex,identifyBaseURL(f"{path}/FrontEnd/AppointmentWeb/index.html",'<base href=[\S|\\b|" "]+','<base href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasAppointmentWebSetting,identifyBaseURL(f"{path}/FrontEnd/AppointmentWeb/assets/settings.json",'"appointmentApiUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasSTEWeb,identifyBaseURL(f"{path}/FrontEnd/STE/Web.config",'<add key="AppointmentWS" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasServiceSSP,identifyBaseURL(f"{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config",'<add key="dataExportServer" value=[\S|\\b|" "]+/>','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasNME,identifyBaseURL(f"{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json",'"appointmentApiEndpoint":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasAppointmentWebConfig,identifyBaseURL(f"{path}/FrontEnd/AppointmentWeb/Web.config",'<add key="messageQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasConfigFilesAppointment,Identify(f"{path}/Middleware/Appointment/ConfigFiles/Appointment.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasConfigFilesAppoinmentWeb,Identify(f"{path}/Middleware/Appointment/ConfigFiles/Appointment.config",'<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>','<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasSSPServiceMSMQ,identifyBaseURL(f"{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config",'<add key="virtualQueueCallBackQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasDataExport,Identify(f"{path}/Middleware/STE/ConfigFiles/DataExport.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime),logging,datetime)  
  Insert(TextboxReporteriaCitasAWebWA,identifyBaseURL(f"{path}/FrontEnd/Appointment/Web.config",'<add key="webApiAdminURL" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)  
  Insert(TextboxReporteriaCitasAWebSuite,identifyBaseURL(f"{path}/FrontEnd/Appointment/Web.config",'<add key="urlSuite" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)  
  Insert(TextboxReporteriaCitasApplicationWA,Identify(f"{path}/FrontEnd/Appointment.WebApi.Admin/bin/Application.config",'<UrlFrontend>[\S|\\b|" "]+</UrlFrontend>','<UrlFrontend>[\S|\\b|" "]+</UrlFrontend>',logging,datetime),logging,datetime)  
  Insert(TextboxReporteriaCitasAWAWebbo,identifyBaseURL(f"{path}/FrontEnd/Appointment.WebApi.Admin/Web.config",'<add key="webApiAdminURL" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)  
  Insert(TextboxReporteriaCitasAboindex,identifyBaseURL(f"{path}/FrontEnd/AppointmentBackOffice/index.html",'<base href=[\S|\\b|" "]+','<base href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasabosettingAWA,identifyBaseURL(f"{path}/FrontEnd/AppointmentBackOffice/assets/setting.json",'"apiAdminUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasabosettingA,identifyBaseURL(f"{path}/FrontEnd/AppointmentBackOffice/assets/setting.json",'"CitasUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaCitasabosettingSuite,identifyBaseURL(f"{path}/FrontEnd/AppointmentBackOffice/assets/setting.json",'"SuiteUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime),logging,datetime)
  