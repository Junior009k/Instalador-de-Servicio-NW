from FrontEnd.VariableDeterminadas import *

#esta funcion se encarga de modificar  url de suite
def startingConfigSuite():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  suite')
  bandera=validateField(TextboxHostSuite,logging,MessageBox,"suite","del servidor",datetime)
  bandera=bandera*validateField(TextboxSiteSuite,logging,MessageBox,"suite","del sitio de suite",datetime)
  bandera=bandera*validateField(TextboxSiteIm,logging,MessageBox,"suite","del sitio de im",datetime)
  bandera=bandera*validateLabel(label34,logging,MessageBox,"suite","la ruta",datetime)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Validando suite')
    configurarSuite(label34.cget("text"),TextboxHostSuite.get(),TextboxSiteSuite.get(),TextboxSiteIm.get(),logging,datetime)
    
#esta funcion se encarga de modificar la bbdd
def startingConfigSuiteBBDD():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  la bbdd')
  bandera=validateField(TextboxIMDB,logging,MessageBox,"suite","de la conexion de la bbdd",datetime)
  bandera=bandera*validateLabel(label35,logging,MessageBox,"suite","la ruta",datetime)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Validando configuracion de la bbdd de suite')
    configurarBBDDSuite(label35.cget("text"),TextboxIMDB.get(),logging,datetime)

def ExamineDirectorySuiteCitas(label):
  path = tkinter.filedialog.askdirectory()
  logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {path} donde se identificaran los reportes')
  path = path.replace("/", r"\ ".strip())
  path=path.rstrip()
  label.config(text=path) 
  
  TextboxCitasIm.delete(0, tk.END)
  TextboxtenantAppointment.delete(0, tk.END)
  TextboxUserNameAdminTenant.delete(0, tk.END)
  TextboxPasswordAdminTenant.delete(0, tk.END)
  TextboxClientIdAppointment.delete(0, tk.END)
  TextboxClientSecretAppointment.delete(0, tk.END)
  
  Insert(TextboxCitasIm,Identify(f"{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config",'<identityManager>[\S|\\b|" "]+</identityManager>','<identityManager>[\S|\\b|" "]+</identityManager>',logging,datetime),logging,datetime)  
  Insert(TextboxtenantAppointment,Identify(f"{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config",'<tenantAppointment>[\S|\\b|" "]+</tenantAppointment>','<tenantAppointment>[\S|\\b|" "]+</tenantAppointment>',logging,datetime),logging,datetime)    
  Insert(TextboxUserNameAdminTenant,Identify(f"{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config",'<UserNameAdminTenant>[\S|\\b|" "]+</UserNameAdminTenant>','<UserNameAdminTenant>[\S|\\b|" "]+</UserNameAdminTenant>',logging,datetime),logging,datetime)    
  Insert(TextboxPasswordAdminTenant,Identify(f"{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config",'<PasswordAdminTenant>[\S|\\b|" "]+</PasswordAdminTenant>','<PasswordAdminTenant>[\S|\\b|" "]+</PasswordAdminTenant>',logging,datetime),logging,datetime)    
  Insert(TextboxClientIdAppointment,Identify(f"{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config",'<ClientIdAppointment>[\S|\\b|" "]+</ClientIdAppointment>','<ClientIdAppointment>[\S|\\b|" "]+</ClientIdAppointment>',logging,datetime),logging,datetime)    
  Insert(TextboxClientSecretAppointment,Identify(f"{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config",'<ClientSecretAppointment>[\S|\\b|" "]+</ClientSecretAppointment>','<ClientSecretAppointment>[\S|\\b|" "]+</ClientSecretAppointment>',logging,datetime),logging,datetime)      
  
#esta funcion se encarga de modificar la bbdd
def startingConfigSuiteAppointment():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  la bbdd')
  bandera=validateLabel(label36,logging,MessageBox,"suite","la ruta",datetime)
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Validando configuracion de la bbdd de suite')
    configurarCitasSuite(label36.cget("text"),[TextboxCitasIm.get(),TextboxtenantAppointment.get(),TextboxUserNameAdminTenant.get(),TextboxPasswordAdminTenant.get(),TextboxClientIdAppointment.get(),TextboxClientSecretAppointment.get()],logging,datetime)