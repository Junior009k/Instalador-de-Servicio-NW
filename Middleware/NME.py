from Middleware.funcionesAuxiliares import fixWord,replaceCadena,replaceCadenaInSection,IdentifyJSON,show_Configuration,show_frame,loadImagen,identifyBaseURL,Insert,validateField,validateLabel
from Middleware.iis import consultaPowershell;
from os import system

def configurarNME(path,server,eflow,eflowApi,loggin,datetime): 
    #"C:\Sides\Frontend\Sidesys.eFlow.Emission.API\Web.config"
    replaceCadena(f'{path}/FrontEnd/Sidesys.eFlow.Emission.API/Web.config',
                '<add key="eFlowServiceUrl" value="http://[\S|\\b|" "]+/Services/EmissionService.svc"', 
                f'<add key="eFlowServiceUrl" value="http://{server}/{eflow}/Services/EmissionService.svc"',loggin,datetime)
    #"C:\Sides\Frontend\STE\SPA\assets\configuration\emission.config.json"
    replaceCadena(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json',
                '"emissionApiEndpoint": "[\S|\\b|" "]+",', 
                f'"emissionApiEndpoint": "http://{server}/{eflowApi}",',loggin,datetime)
def configurarNMESite(path,server,eflow,eflowApi,loggin,datetime): 
    #"C:\Sides\Frontend\Sidesys.eFlow.Emission.API\Web.config"
    replaceCadena(f'{path}/FrontEnd/Sidesys.eFlow.Emission.API/Web.config',
                '<add key="eFlowServiceUrl" value="http://[\S|\\b|" "]+/Services/EmissionService.svc"', 
                f'<add key="eFlowServiceUrl" value="http://{server}:{eflow}/Services/EmissionService.svc"',loggin,datetime)
    #"C:\Sides\Frontend\Sidesys.eFlow.Emission.API\Web.config"
    replaceCadena(f'{path}/FrontEnd/Sidesys.eFlow.Emission.API/Web.config',
                ' <add key="AllowedCrossOrigins" value="[\S|\\b|" "]+"', 
                f'<add key="AllowedCrossOrigins" value="http://{server}:{eflow}"',loggin,datetime)    
    #"C:\Sides\Frontend\STE\SPA\assets\configuration\emission.config.json"
    replaceCadena(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json',
                '"emissionApiEndpoint": "[\S|\\b|" "]+",', 
                f'"emissionApiEndpoint": "http://{server}:{eflowApi}",',loggin,datetime)
 
def configurarNMECitas(path,server,citaswebservice,loggin,datetime): 
    #"C:\Entornos\Superintendencia - 03\PRODUCCION\Frontend\Sidesys.eFlow.Emission.API\Web.config"
    replaceCadena(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json',
    '"appointmentApiEndpoint": "[\S|\\b|" "]+",', 
    f'"appointmentApiEndpoint": "http://{server}/{citaswebservice}",',loggin,datetime)

def configurarEmissionConfig(path, preferencial,announceAppointment,loggin,datetime):
    if(preferencial==1):preferencial='true'
    else:preferencial='false'
    if(announceAppointment==1):announceAppointment='true'
    else:announceAppointment='false'
    replaceCadenaInSection(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json','"attentionPreferential": {[\S|\s]+"showIcon"','"showButton":[\S|\\b|" "]+,', f'"showButton": {preferencial},',loggin,datetime)
    replaceCadenaInSection(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json','"announceAppointment": {[\S|\s]+"showAnnounceAppointment"','"showAnnounceAppointment":[\S|\\b|" "]+,', f'"showAnnounceAppointment": {announceAppointment},',loggin,datetime)
#configurarEmissionConfig("C:\Entornos\Superintendencia - 04\PRODUCCION",1, logging, datetime)   
def identifyNME(path,patron, secondPatron,logging,datetime):
    if(IdentifyJSON(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json',patron,secondPatron,logging,datetime)=="true"):
        return True
    else:
        return False
    #def identifyTicketPrintingService(protocol,url,stylepath, imgpath, ticketImg, logging, datetime)
def identifyTicketPrintingService( logging, datetime):
    try:   
        usuario=consultaPowershell("(Get-CimInstance -ClassName Win32_ComputerSystem).Username",logging, datetime).split("\\",2)[1].strip()
        print(usuario)
        print(f'"C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json"')
    #system(f'"C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json"')
       
        protocol=IdentifyJSON(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"eFlow"[\s|\S]+},','"protocol":[\S|\\b|" "]+,',logging,datetime).replace('"', r'')
        url=IdentifyJSON(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"eFlow"[\s|\S]+},','"urlEflow":[\S|\\b|" "]+',logging,datetime).replace('"', r'')
        stylepath=IdentifyJSON(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"printServer"[\s|\S]+}','"relativeStyleFilePath":[\S|\\b|" "]+',logging,datetime).replace('"', r'')
        imgpath=IdentifyJSON(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"printServer"[\s|\S]+}','"ticketImagesDirectory":[\S|\\b|" "]+',logging,datetime).replace('"', r'')
        ticketImg=IdentifyJSON(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"printServer"[\s|\S]+}','"ticketLogoFile":[\S|\\b|" "]+',logging,datetime).replace('"', r'')
        logging.info(f' {datetime.datetime.now() }: "C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json"')
    
        return protocol,url,stylepath,imgpath,ticketImg
    except Exception as e:
        print(f"Espacio en blanco detectado: {e}")
        
    
def updateTicketPrintingService(protocol,url,stylepath, imgpath, ticketImg, loggin, datetime):
    usuario=consultaPowershell("(Get-CimInstance -ClassName Win32_ComputerSystem).Username",loggin, datetime).split("\\",2)[1].strip()
    replaceCadenaInSection(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"eFlow"[\s|\S]+},','"protocol":[\S|\\b|" "]+,', f'"protocol": "{protocol}",',loggin,datetime)
    replaceCadenaInSection(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"eFlow"[\s|\S]+},','"urlEflow":[\S|\\b|" "]+', f'"urlEflow": "{url}"',loggin,datetime)
    replaceCadenaInSection(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"printServer"[\s|\S]+}','"relativeStyleFilePath":[\S|\\b|" "]+,', f'"relativeStyleFilePath": "{stylepath}",',loggin,datetime)
    replaceCadenaInSection(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"printServer"[\s|\S]+}','"ticketImagesDirectory":[\S|\\b|" "]+,', f'"ticketImagesDirectory": "{imgpath}",',loggin,datetime)
    replaceCadenaInSection(f'C:\\Users\\{usuario}\AppData\\Local\Programs\\ticketprinttingservice\\static\config\\configuration.json','"printServer"[\s|\S]+}','"ticketLogoFile":[\S|\\b|" "]+,', f'"ticketLogoFile": "{ticketImg}",',loggin,datetime)
    pass
    
#print(identifyNME("C:\Entornos\Superintendencia - 04\PRODUCCION"))
#configurarNMESite("C:\Entornos\Superintendencia - 04\PRODUCCION","192.168.104.42","80","81",logging,datetime)
#configurarNME("C:\Entornos\Superintendencia - 04\PRODUCCION","192.168.104.42","ste","steAPI",logging,datetime)
#configurarNMECitas("C:\Entornos\Superintendencia - 04\PRODUCCION","192.168.104.42","AppointmentWebService",logging,datetime)
#steMiddleware="FS"
#replaceCadenaInSection(f'C:/Entornos/Superintendencia - 04/PRODUCCION/FrontEnd/STE/SPA/assets/configuration/emission.config.json','"appointmentApiEndpoint": [\S|\\b|" "]+"',':[\S|\\b|" "]+"',f':"{steMiddleware}"',logging,datetime)