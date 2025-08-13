from Middleware.funcionesAuxiliares import replaceCadena, replaceCadenaInSection

def configurarCitas(path,server,citas,eflow,msmq,loggin,datetime): 
    #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\appSpa\index.html"
    replaceCadena(f'{path}/FrontEnd/Appointment/appSpa/index.html',
                '<base href="[\S|\\b|" "]+">', 
                f'<base href="http://{server}/{citas}/appSpa/"> ',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\AttOpSpa\index.html"
    replaceCadena(f'{path}/FrontEnd/Appointment/AttOpSpa/index.html',
               '<base href="[\S|\\b|" "]+">', 
                f'<base href="http://{server}/{citas}/AttOpSpa/">" ',loggin,datetime)
     
    #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\bin\Application.config"
    replaceCadena(f'{path}/FrontEnd/Appointment/bin/Application.config',
                '<OperationalPath>[\S|\\b|" "]+</OperationalPath>', 
                f'<OperationalPath>http://{server}/{citas}/POC/POCView.aspx</OperationalPath>',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\FrontEnd\STE\Web.config"
    replaceCadena(f'{path}/FrontEnd/STE/Web.config',
                '<add key="AppointmentWS" value="[\S|\\b|" "]+/Appointment.asmx"', 
                f'<add key="AppointmentWS" value="http://{server}/{citas}/Appointment.asmx"',loggin,datetime)
     
    #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\index.html"
    replaceCadena(f'{path}/FrontEnd/AppointmentWeb/index.html',
                '<base href="[\S|\\b|" "]+" />', 
                f'<base href="http://{server}/{citas}web/" />',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\Web.config" cola de mensajeria web 
    replaceCadena(f'{path}/FrontEnd/AppointmentWeb/Web.config',
                '<add key="messageQueuePath" value="[\S|\\b|" "]+" />', 
                   f'<add key="messageQueuePath" value="FormatName:DIRECT=TCP:{server}\private$\{msmq}" />',loggin,datetime)
    

    #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\assets\settings.json"
    replaceCadena(f'{path}/FrontEnd/AppointmentWeb/assets/settings.json',
                '"appointmentApiUrl":[\S|\\b|" "]+",', 
                f'"appointmentApiUrl": "http://{server}/{citas}webservice",',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config" OutgoingEventsSendQueuePath>
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/Appointment.config',
                '<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>', 
                f'<OutgoingEventsSendQueuePath>FormatName:DIRECT=TCP:{server}\private$\{msmq}</OutgoingEventsSendQueuePath>',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config" cola de mensajeria web 
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/Appointment.config',
                '<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>', 
             f'<MSMQWebChannel>FormatName:DIRECT=TCP:{server}\private$\{msmq}</MSMQWebChannel>',loggin,datetime)
    
    
    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\bin\Sidesys.Services.ApplicationService.exe.config" e-Flow 
    replaceCadena(f'{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config',
                '<add key="dataExportServer" value="[\S|\\b|" "]+"/>', 
                f'<add key="dataExportServer" value="http://{server}/{eflow}"/>',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\bin\Sidesys.Services.ApplicationService.exe.config" cola de mensajeria
    replaceCadena(f'{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config',
                '<add key="virtualQueueCallBackQueuePath" value="[\S|\\b|" "]+" />', 
                f'<add key="virtualQueueCallBackQueuePath" value="FormatName:DIRECT=TCP:{server}\private$\{msmq}" />',loggin,datetime)
    
    #"C:\Entorno\Seguros Reservas\Middleware\STE\ConfigFiles\DataExport.config"
    replaceCadena(f'{path}/Middleware/STE/ConfigFiles/DataExport.config',
                '<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>', 
                f'<OutgoingEventsSendQueuePath>FormatName:DIRECT=TCP:{server}\private$\{msmq}</OutgoingEventsSendQueuePath>',loggin,datetime)
    
    #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\Appointment\Web.config" AppointmentWA
    replaceCadena(f'{path}/FrontEnd/Appointment/Web.config',
                 '<add key="webApiAdminURL" value="[\S|\\b|" "]+"', 
                f'<add key="webApiAdminURL" value="http://{server}/{citas}WA/"',loggin,datetime)
    
    #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\Appointment\Web.config" Suite
    replaceCadena(f'{path}/FrontEnd/Appointment/Web.config',
                 '<add key="urlSuite" value="[\S|\\b|" "]+"', 
                f'<add key="urlSuite" value="http://{server}/suite/"',loggin,datetime)
    
    #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\Appointment.WebApi.Admin\bin\Application.config"
    replaceCadena(f'{path}/FrontEnd/Appointment.WebApi.Admin/bin/Application.config',
                '<UrlFrontend>[\S|\\b|" "]+</UrlFrontend>', 
                f'<UrlFrontend>http://{server}/{citas}bo</UrlFrontend>',loggin,datetime)
    
    #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\Appointment.WebApi.Admin\Web.config"
    replaceCadena(f'{path}/FrontEnd/Appointment.WebApi.Admin/Web.config',
                 '<add key="webApiAdminURL" value="[\S|\\b|" "]+"', 
                f'<add key="webApiAdminURL" value="http://{server}/{citas}WA/"',loggin,datetime)
    
    #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\AppointmentBackOffice\index.html"
    replaceCadena(f'{path}/FrontEnd/AppointmentBackOffice/index.html',
                '<base href="[\S|\\b|" "]+" />', 
                f'<base href="http://{server}/{citas}bo/" />',loggin,datetime)
    
    #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\AppointmentBackOffice\assets\setting.json"
    replaceCadena(f'{path}/FrontEnd/AppointmentBackOffice/assets/setting.json',
                '"apiAdminUrl":[\S|\\b|" "]+",', 
                f'"apiAdminUrl": "http://{server}/{citas}WA",',loggin,datetime)
    
    #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\AppointmentBackOffice\assets\setting.json"
    replaceCadena(f'{path}/FrontEnd/AppointmentBackOffice/assets/setting.json',
                '"CitasUrl":[\S|\\b|" "]+",', 
                f'"CitasUrl": "http://{server}/{citas}",',loggin,datetime)
    
    #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\AppointmentBackOffice\assets\setting.json"
    replaceCadena(f'{path}/FrontEnd/AppointmentBackOffice/assets/setting.json',
                '"SuiteUrl":[\S|\\b|" "]+",', 
                f'"SuiteUrl": "http://{server}/suite",',loggin,datetime)

def updateCitas(path,appSpa,AttOpSpa,app,awi,setting,steweb,steMiddleware,nmecitas,MSMQawi,MSMQMAout,MSMQMAweb,MSMQMService, MSMQMDataExport,aWwA,suiteWConfig,abo,AWWWA,ibo,aWASetting,aSetting,suiteSetting,loggin,datetime): 
   print("configurar Citas")
   #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\appSpa\index.html"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment/appSpa/index.html','<base href=[\S|\\b|" "|[<,>]]+','href=[\S|\\b|" "]+"',f'href="{appSpa}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\AttOpSpa\index.html"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment/AttOpSpa/index.html','<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+"',f'href="{AttOpSpa}"',loggin,datetime)
    
   #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\bin\Application.config"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment/bin/Application.config','<OperationalPath>[\S|\\b|" "]+</OperationalPath>','<OperationalPath>[\S|\\b|" "]+</OperationalPath>',f'<OperationalPath>{app}</OperationalPath>',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\index.html"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentWeb/index.html','<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+"',f'href="{awi}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\assets\settings.json"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentWeb/assets/settings.json','"appointmentApiUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+"',f':"{setting}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\STE\Web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/STE/Web.config','<add key="AppointmentWS" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+"',f'value="{steweb}"',loggin,datetime)

   #""C:\Entorno\Seguros Reservas\Middleware\Appointment\bin\Sidesys.Services.ApplicationService.exe.config" e-Flow 
   replaceCadenaInSection(f'{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config','<add key="dataExportServer" value=[\S|\\b|" "]+/>','value=[\S|\\b|" "]+"',f'value="{steMiddleware}"',loggin,datetime)

   #C:\Sides\Frontend\STE\SPA\assets\configuration\emission.config.json
   replaceCadenaInSection(f'{path}/FrontEnd/STE/SPA/assets/configuration/emission.config.json','"appointmentApiEndpoint":[\S|\\b|" "]+"',':[\S|\\b|" "]+"',f':"{nmecitas}"',loggin,datetime)

   #C:\Entorno\Seguros Reservas\FrontEnd\AppointmentWeb\Web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentWeb/Web.config','<add key="messageQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+"',f'value="{MSMQawi}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config"
   replaceCadenaInSection(f'{path}/Middleware/Appointment/ConfigFiles/Appointment.config','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',f'<OutgoingEventsSendQueuePath>{MSMQMAout}</OutgoingEventsSendQueuePath>',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config"
   replaceCadenaInSection(f'{path}/Middleware/Appointment/ConfigFiles/Appointment.config','<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>','<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>',f'<MSMQWebChannel>{MSMQMAweb}</MSMQWebChannel>',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config"
   replaceCadenaInSection(f'{path}/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config','<add key="virtualQueueCallBackQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+"',f'value="{MSMQMService}"',loggin,datetime)

    #"C:\Entorno\Seguros Reservas\Middleware\Appointment\ConfigFiles\Appointment.config"
   replaceCadenaInSection(f'{path}/Middleware/STE/ConfigFiles/DataExport.config','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',f'<OutgoingEventsSendQueuePath>{MSMQMDataExport}</OutgoingEventsSendQueuePath>',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\Web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment/Web.config','<add key="webApiAdminURL" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+"',f'value="{aWwA}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\Appointment\Web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment/Web.config','<add key="urlSuite" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+"',f'value="{suiteWConfig}"',loggin,datetime)
   
   #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\Appointment.WebApi.Admin\bin\Application.config"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment.WebApi.Admin/bin/Application.config','<UrlFrontend>[\S|\\b|" "]+</UrlFrontend>','<UrlFrontend>[\S|\\b|" "]+</UrlFrontend>',f'<UrlFrontend>{abo}</UrlFrontend>',loggin,datetime)

   #"E:\ENTORNOS\AMBEV - 043\PRODUCCION\FrontEnd\Appointment.WebApi.Admin\Web.config"
   replaceCadenaInSection(f'{path}/FrontEnd/Appointment.WebApi.Admin/Web.config','<add key="webApiAdminURL" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+"',f'value="{AWWWA}"',loggin,datetime)

   #"C:\Entorno\Seguros Reservas\FrontEnd\AppointmentBackOffice\index.html"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentBackOffice/index.html','<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+"',f'href="{ibo}"',loggin,datetime)

    #..\FrontEnd\AppointmentBackOffice\assets\settings.json"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentBackOffice/assets/setting.json','"apiAdminUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+"',f':"{aWASetting}"',loggin,datetime)

    #..\FrontEnd\AppointmentBackOffice\assets\settings.json"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentBackOffice/assets/setting.json','"CitasUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+"',f':"{aSetting}"',loggin,datetime)

    #..\FrontEnd\AppointmentBackOffice\assets\settings.json"
   replaceCadenaInSection(f'{path}/FrontEnd/AppointmentBackOffice/assets/setting.json','"SuiteUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+"',f':"{suiteSetting}"',loggin,datetime)



#updateCitas(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/","http://rdstac001/Citas","http://rdstac001/Citas","http://rdstac001/ CitasApp","http://rdstac001/ CitasIndex","http://rdstac001/ CitaswebService","http:RDSTAC001/Citas/Appointment","http://RDSTAC002/STE","http://rdstac001/ CitaswebService",".\Appointment",".\Appointmentout",".\AppointmentWeb",".\Appointmentout",".\AppointmentWeb",logging,datetime)
#configurarCitas("C:\SidesysCitas","192.168.104.92","SegurosReservasCitas","STE","SegurosReservas", logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/Appointment/appSpa/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/Appointment/AttOpSpa/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/AppointmentWeb/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/AppointmentWeb/assets/settings.json",'"appointmentApiUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/STE/Web.config",'<add key="AppointmentWS" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config",'<add key="dataExportServer" value=[\S|\\b|" "]+/>','value=[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:\Entornos\Superintendencia - 04\PRODUCCION/FrontEnd/STE/SPA/assets/configuration/emission.config.json",'"appointmentApiEndpoint":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/FrontEnd/AppointmentWeb/Web.config",'<add key="messageQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+',logging,datetime)
#Identify(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/Middleware/Appointment/ConfigFiles/Appointment.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime)
#Identify(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/Middleware/Appointment/ConfigFiles/Appointment.config",'<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>','<MSMQWebChannel>[\S|\\b|" "]+</MSMQWebChannel>',logging,datetime)
#identifyBaseURL(f"C:/Entornos/Banco Promerica - 01/PRODUCCION//Middleware/Appointment/bin/Sidesys.Services.ApplicationService.exe.config",'<add key="virtualQueueCallBackQueuePath" value="[\S|\\b|" "]+" />','value=[\S|\\b|" "]+',logging,datetime)
#Identify(f"C:/Entornos/Banco Promerica - 01/PRODUCCION/Middleware/STE/ConfigFiles/DataExport.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime)

