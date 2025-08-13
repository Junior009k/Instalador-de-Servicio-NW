import subprocess


def sendMessage(MSMQ,loggin,datetime):
    loggin.info(f' {datetime.datetime.now() }:Empezando el proceso de envio de mensajes')
    msj=consultaPowershell("""
                          # Nombre de la cola MSMQ a la que deseas enviar el mensaje
                          $colaMSMQ = '"""+MSMQ+"""'
                          # Crea una instancia del objeto Message y establece el cuerpo del mensaje
                          $mensaje = New-Object System.Messaging.Message
                          $mensaje.Body = "Este es un mensaje de prueba."

                         
                          $cola = New-Object System.Messaging.MessageQueue $colaMSMQ

                          # Envía el mensaje a la cola
                          $cola.Send($mensaje)
                          
                          Write-Host "Mensaje enviado correctamente a la cola MSMQ."
                          """,loggin,datetime)
    
    loggin.info(f' {datetime.datetime.now() }: {msj[1]}')
    print(f' {datetime.datetime.now() }: {msj[1]}')
    return msj


def receivedMessage(MSMQ,loggin,datetime):
    loggin.info(f' {datetime.datetime.now() }:Empezando el proceso de recepcion de mensajes')
    msj=consultaPowershell("""
                          # Nombre de la cola MSMQ a la que deseas enviar el mensaje
                          $queuePath= '"""+MSMQ+"""'
                          # Conectar a la cola
                            $queue = New-Object System.Messaging.MessageQueue $queuePath

                            # Establecer el formato del mensaje para poder leer el cuerpo del mensaje como un string
                            $queue.Formatter = New-Object System.Messaging.XmlMessageFormatter([String[]]@("System.String"))

                           
                            $message = $queue.Receive([System.TimeSpan]::FromSeconds(70))
                            Write-Host "Mensaje recibido: $($message.Body)"
                            
                            


                            # Cerrar la conexión con la cola
                            $queue.Close()
                            """,loggin,datetime)
    
    loggin.info(f' {datetime.datetime.now() }: {msj[1]}')
    print(f' {datetime.datetime.now() }: {msj[1]}')
    return msj


#Consulta Powershell 
def consultaPowershell(consulta,loggin,datetime):
    loggin.info(f' {datetime.datetime.now() }:empezando la consulta en poweshell')
    loggin.info(f' {datetime.datetime.now() }:{consulta}')
    comando_ps =f'''Add-Type -AssemblyName System.Messaging
                 {consulta}'''
    resultado = subprocess.run(["powershell", "-Command", comando_ps], capture_output=True, text=True)
    if(len(resultado.stderr)>0):
        loggin.error(f' {datetime.datetime.now() }:error al realizar la consulta en powershell {resultado.stderr}')
        return False,resultado.stderr
    return True,resultado.stdout


 # Abre la cola de MSMQ (creándola si no existe)
  #                        if (-not (Test-Path $colaMSMQ)) {
  #                           [System.Messaging.MessageQueue]::Create($colaMSMQ) > $null
   #                       }
                          