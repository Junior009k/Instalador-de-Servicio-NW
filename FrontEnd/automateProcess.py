from FrontEnd.VariableDeterminadas import *



#Este metodo se encarga de automatizar el proceso
def automateProcess():
  logging.info(f' {datetime.datetime.now() }: Se comienza a automatizar el aplicativo')
  
  bandera=validateField(TextboxAutomatizadorSRVBD,logging,MessageBox,"el aplicativo","el nombre del servidor de base de datos",datetime)
  bandera=validateField(TextboxAutomatizadorSRVAPP,logging,MessageBox,"el aplicativo","el nombre del servidor de la aplicaciones",datetime)
  bandera=validateField(TextboxAutomatizadorName,logging,MessageBox,"el aplicativo","el nombre del aplicativo",datetime)
  bandera=validateLabel(label17,logging,MessageBox,"el aplicativo","la ruta",datetime)
  if( validateDirectory(label17.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label17.cget("text"),"FrontEnd",logging,datetime)):
    logging.error(f' {datetime.datetime.now() }: No se puede automatizar el aplicativo ,tiene que estar en la carpeta del aplicativo')
    MessageBox.showerror("Error","Para automatizar el aplicativo, tiene que estar en la carpeta del aplicativo")
    bandera=False
  
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso automatizacion ')
    print("Paso todas las pruebas, comenzando proceso de automatizacion")
    #Instala el servicio de e-Flow
    if(eFlowvar.get()):installService(f'e-Flow {TextboxAutomatizadorName.get()} Middleware Service',f'{label17.cget("text")}\MiddleWare\STE\\bin\Sidesys.Services.ApplicationService.exe',1,logging,datetime)
    #Instala el servicio de e-Flow Nodo
    if(eFlowvar.get() & eFlow4var.get()):installService(f'e-Flow {TextboxAutomatizadorName.get()} MiddlewareNode Service',f'{label17.cget("text")}\MiddleWareNode\STE\\bin\Sidesys.Services.ApplicationService.exe',1,logging,datetime)
    #Instala el servicio de Citas
    if(citasvar.get()):installService(f'e-Flow {TextboxAutomatizadorName.get()} Citas Middleware Service',f'{label17.cget("text")}\MiddleWare\Appointment\\bin\Sidesys.Services.ApplicationService.exe',1,logging,datetime)
    #Instala el servicio de Encuesta
    if(encuestavar.get()):installService(f'e-Flow {TextboxAutomatizadorName.get()} Encuesta Middleware Service',f'{label17.cget("text")}\MiddleWare\OpinionPoll\\bin\Sidesys.Services.ApplicationService.exe',1,logging,datetime)
  if(TextboxAutomatizadorName.get()=="STE"):
    if(eFlowvar.get()):createAplicationIIS("STE",f'{label17.cget("text")}\FrontEnd\STE',logging)
    if(citasvar.get()):createAplicationIIS("Appointment",f'{label17.cget("text")}\FrontEnd\Appointment',logging)
    if(citasvar.get()):createAplicationIIS("AppointmentWeb",f'{label17.cget("text")}\FrontEnd\AppointmentWeb',logging)
    if(citasvar.get()):createAplicationIIS("AppointmentWebService",f'{label17.cget("text")}\FrontEnd\AppointmentWebService',logging)
    if(encuestavar.get()):createAplicationIIS("OpinionPoll",f'{label17.cget("text")}\FrontEnd\OpinionPoll',logging)
  else:
    if(eFlowvar.get()):createAplicationIIS(f"{TextboxAutomatizadorName.get()}-STE",f'{label17.cget("text")}\FrontEnd\STE',logging)
    if(citasvar.get()):createAplicationIIS(f"{TextboxAutomatizadorName.get()}-Appointment",f'{label17.cget("text")}\FrontEnd\Appointment',logging)
    if(citasvar.get()):createAplicationIIS(f"{TextboxAutomatizadorName.get()}-AppointmentWeb",f'{label17.cget("text")}\FrontEnd\AppointmentWeb',logging)
    if(citasvar.get()):createAplicationIIS(f"{TextboxAutomatizadorName.get()}-AppointmentWebService",f'{label17.cget("text")}\FrontEnd\AppointmentWebService',logging)
    if(encuestavar.get()):createAplicationIIS(f"{TextboxAutomatizadorName.get()}-OpinionPoll",f'{label17.cget("text")}\FrontEnd\OpinionPoll',logging)

  if(TextboxAutomatizadorName.get()=="STE"):
    if(eFlowvar.get()):manageUDL(TextboxAutomatizadorSRVBD.get(),"STE",f'{label17.cget("text")}\MiddleWare\STE\\ConfigFiles',logging,datetime)
    if(eFlowvar.get() & eFlow4var.get()):manageUDL(TextboxAutomatizadorSRVBD.get(),"STE",f'{label17.cget("text")}\MiddleWareNode\STE\\ConfigFiles',logging,datetime)
    if(citasvar.get()):manageUDL(TextboxAutomatizadorSRVBD.get(),"Appointment",f'{label17.cget("text")}\MiddleWare\Appointment\\ConfigFiles',logging,datetime)
    if(encuestavar.get()):manageUDL(TextboxAutomatizadorSRVBD.get(),"STE",f'{label17.cget("text")}\MiddleWare\OpinionPoll\\ConfigFiles',logging,datetime)  
  else:
    if(eFlowvar.get()):manageUDL(TextboxAutomatizadorSRVBD.get(),f"{TextboxAutomatizadorName.get()}-STE",f'{label17.cget("text")}\MiddleWare\STE\\ConfigFiles',logging,datetime)
    if(eFlowvar.get() & eFlow4var.get()):manageUDL(TextboxAutomatizadorSRVBD.get(),f"{TextboxAutomatizadorName.get()}-STE",f'{label17.cget("text")}\MiddleWareNode\STE\\ConfigFiles',logging,datetime)
    if(citasvar.get()):manageUDL(TextboxAutomatizadorSRVBD.get(),f"{TextboxAutomatizadorName.get()}-Appointment",f'{label17.cget("text")}\MiddleWare\Appointment\\ConfigFiles',logging,datetime)
    if(encuestavar.get()):manageUDL(TextboxAutomatizadorSRVBD.get(),f"{TextboxAutomatizadorName.get()}-STE",f'{label17.cget("text")}\MiddleWare\OpinionPoll\\ConfigFiles',logging,datetime)
    
    
  
