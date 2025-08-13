from FrontEnd.VariableDeterminadas import *

#esta funcion se encarga de modificar el tiempo de sesion de la consola
def validateMSMQ():
  print(TextboxMSMQEntry.get())
  bandera=validateField(TextboxMSMQEntry,logging,MessageBox,"MSMQ","del servidor",datetime)
  logging.info(f' {datetime.datetime.now() }: Se comienza la ejecucion deL diagnostico de las colas de mensajerias')
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Validando la cola de mensajerias')
    diagnostico=sendMessage(TextboxMSMQEntry.get(),logging,datetime)
    if diagnostico[0] : labelMSMQSend.config(text=diagnostico[1], fg='#0F0',justify='left')
    else:labelMSMQSend.config(text="Ha ocurrido un error, vease los log" , fg='#F00',justify='left')
    diagnostico=receivedMessage(TextboxMSMQEntry.get(),logging,datetime)
    if diagnostico[0] : labelMSMQReceived.config(text=diagnostico[1], fg='#0F0',justify='left')
    else:labelMSMQReceived.config(text="Ha ocurrido un error, vease los log", fg='#F00',justify='left')
    
    #configurarMinuteConsole(spinMinuteConsole.get(),logging,datetime)