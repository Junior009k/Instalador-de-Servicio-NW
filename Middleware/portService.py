
from Middleware.funcionesAuxiliares import replaceCadena
#print(content)


def changePort(path,port,url,loggin,datetime):
    #puertos {path}\Middleware\bin\servicemodelConfig\{service.config} tcp middleware
    loggin.info(f' {datetime.datetime.now() }: Se inicia con el proceso de cambio de puerto')
    replaceCadena(f'{path}/Middleware/STE/bin/serviceModelConfig/services.config',
                '<endpoint name="MiddleWare" address="net.tcp://\S*:\w*/ApplicationService/" ', 
                f'<endpoint name="MiddleWare" address="net.tcp://{url}:{port}00/ApplicationService/" ',loggin,datetime)
    #puertos {path}\Middleware\bin\servicemodelConfig\{service.config} Design Time Adress middleware
    replaceCadena(f'{path}/Middleware/STE/bin/serviceModelConfig/services.config',
                'add baseAddress="http://\S*:\w*/Design_Time_Addresses/Sidesys.Services/ApplicationService/"', 
                f'add baseAddress="http://{url}:{port}2/Design_Time_Addresses/Sidesys.Services/ApplicationService/"',loggin,datetime)
    #puertos {path}\Middleware\bin\servicemodelConfig\{Cliente.config} clientNode en el middleware
    replaceCadena(f'{path}/Middleware/STE/bin/serviceModelConfig/client.config',
                'address="net.tcp://\S*:\w*/ApplicationServiceNode/"', 
                f'address="net.tcp://{url}:{port}01/ApplicationServiceNode/"',loggin,datetime)
    #puertos {path}\MiddlewareNode\bin\servicemodelConfig\{service.config} tcp middlewareNode
    replaceCadena(f'{path}/MiddlewareNode/STE/bin/serviceModelConfig/services.config',
                '<endpoint name="MiddleWareNode" address="net.tcp://\S*:\w*/ApplicationServiceNode/" ', 
                f'<endpoint name="MiddleWareNode" address="net.tcp://{url}:{port}01/ApplicationServiceNode/" ',loggin,datetime)
    #puertos {path}\MiddlewareNode\bin\servicemodelConfig\{service.config} Design Time Adress middlewareNode
    replaceCadena(f'{path}/MiddlewareNode/STE/bin/serviceModelConfig/services.config',
                'add baseAddress="http://\S*:\w*/Design_Time_Addresses/Sidesys.Services/ApplicationServiceNode/"', 
                f'add baseAddress="http://{url}:{port}3/Design_Time_Addresses/Sidesys.Services/ApplicationServiceNode/"',loggin,datetime)
    #puertos {path}\Middleware\bin\servicemodelConfig\{service.config} tcp middlewareNode
    replaceCadena(f'{path}/Middleware/STE/bin/serviceModelConfig/services.config',
                '<endpoint name="MiddleWareNode" address="net.tcp://\S*:\w*/ApplicationServiceNode/" ', 
                f'<endpoint name="MiddleWareNode" address="net.tcp://{url}:{port}01/ApplicationServiceNode/" ',loggin,datetime)
    #puertos {path}\Middleware\bin\servicemodelConfig\{service.config} Design Time Adress middlewareNode
    replaceCadena(f'{path}/Middleware/STE/bin/serviceModelConfig/services.config',
                'add baseAddress="http://\S*:\w*/Design_Time_Addresses/Sidesys.Services/ApplicationServiceNode/"', 
                f'add baseAddress="http://{url}:{port}3/Design_Time_Addresses/Sidesys.Services/ApplicationServiceNode/"',loggin,datetime)
    #puertos {path}\Middleware\bin\servicemodelConfig\{Cliente.config} clientNode en el middlewareNode
    replaceCadena(f'{path}/MiddlewareNode/STE/bin/serviceModelConfig/client.config',
                'address="net.tcp://\S*:\w*/ApplicationServiceNode/"', 
                f'address="net.tcp://{url}:{port}9/ApplicationServiceNode/"',loggin,datetime)
    #puertos {path}\Frontend\ConfigFiles\Client.config tcp middleware
    replaceCadena(f'{path}/Frontend/STE/ConfigFiles/client.config',
                '<endpoint name="MiddleWare" address="net.tcp://\S*:\w*/ApplicationService/"', 
                f'<endpoint name="MiddleWare" address="net.tcp://{url}:{port}00/ApplicationService/" ',loggin,datetime)
    #puertos {path}\Frontend\ConfigFiles\Client.config  tcp middlewareNode
    replaceCadena(f'{path}/Frontend/STE/ConfigFiles/client.config',
                '<endpoint name="MiddleWareNode" address="net.tcp://\S*:\w*/ApplicationServiceNode/"', 
                f'<endpoint name="MiddleWareNode" address="net.tcp://{url}:{port}01/ApplicationServiceNode/" ',loggin,datetime)
def changePortAppointment(path,port,url,loggin,datetime):
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\FrontEnd\Appointment\ConfigFiles\Client.config" 11211
    loggin.info(f' {datetime.datetime.now() }: Se inicia con el proceso de cambio de puerto en Citas')
    replaceCadena(f'{path}/FrontEnd/Appointment/ConfigFiles/Client.config',
                'address="net.tcp://\S*:\w*/ApplicationService/', 
                f'address="net.tcp://{url}:{port}11/ApplicationService/',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\FrontEnd\Appointment\ConfigFiles\Client.config" 11211
    replaceCadena(f'{path}/FrontEnd/Appointment.WebApi.Admin/ConfigFiles/Client.config',
                'address="net.tcp://\S*:\w*/ApplicationService/', 
                f'address="net.tcp://{url}:{port}11/ApplicationService/',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\FrontEnd\Appointment\ConfigFiles\Client.config" 11211
    replaceCadena(f'{path}/FrontEnd/AppointmentWebService/ConfigFiles/Client.config',
                'address="net.tcp://\S*:\w*/ApplicationService/', 
                f'address="net.tcp://{url}:{port}11/ApplicationService/',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\FrontEnd\Appointment\ConfigFiles\Client.config" 10504 schedulling
    replaceCadena(f'{path}/FrontEnd/Appointment/ConfigFiles/Client.config',
                'address="net.tcp://\S*:\w*/Scheduling/', 
                f'address="net.tcp://{url}:{port}04/Scheduling/',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\FrontEnd\Appointment\ConfigFiles\Client.config" 10504 schedullingDetail
    replaceCadena(f'{path}/FrontEnd/Appointment/ConfigFiles/Client.config',
                'address="net.tcp://\S*:\w*/SchedulingDetail/', 
                f'address="net.tcp://{url}:{port}04/SchedulingDetail/',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\FrontEnd\AppointmentWebService\ConfigFiles\Client.config" 11211
    replaceCadena(f'{path}/FrontEnd/Appointment/ConfigFiles/Client.config',
                'address="net.tcp://\S*:\w*/ApplicationService/', 
                f'address="net.tcp://{url}:{port}11/ApplicationService/',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\Middleware\Appointment\bin\ServiceModelConfig\Service.config" 11211
    replaceCadena(f'{path}/Middleware/Appointment/bin/ServiceModelConfig/Services.config',
                'address="net.tcp://\S*:\w*/ApplicationService/', 
                f'address="net.tcp://{url}:{port}11/ApplicationService/',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\Middleware\Appointment\bin\ServiceModelConfig\Service.config" 9518 
    replaceCadena(f'{path}/Middleware/Appointment/bin/ServiceModelConfig/Services.config',
                'baseAddress="http://\S*:\w*/Design_Time_Addresses/Sidesys.Services/ApplicationService/"', 
                f'baseAddress="http://{url}:{port}8/Design_Time_Addresses/Sidesys.Services/ApplicationService/"',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\Middleware\Appointment\bin\ServiceModelConfig\Service.config" 10504
    replaceCadena(f'{path}/Middleware/Appointment/bin/ServiceModelConfig/Services.config',
                'address="net.tcp://\S*:\w*/Scheduling/"', 
                f'address="net.tcp://{url}:{port}04/Scheduling/"',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\Middleware\Appointment\bin\ServiceModelConfig\Service.config" 10505
    replaceCadena(f'{path}/Middleware/Appointment/bin/ServiceModelConfig/Services.config',
                'baseAddress="http://\S*:\w*/Design_Time_Addresses/Appointment.Core.SchedulingOperation/SchedulingOperationService/', 
                f'baseAddress="http://{url}:{port}05/Design_Time_Addresses/Appointment.Core.SchedulingOperation/SchedulingOperationService/',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\Middleware\Appointment\bin\ServiceModelConfig\Service.config" 10504 Details
    replaceCadena(f'{path}/Middleware/Appointment/bin/ServiceModelConfig/Services.config',
                'address="net.tcp://\S*:\w*/SchedulingDetail/"', 
                f'address="net.tcp://{url}:{port}04/SchedulingDetail/"',loggin,datetime)
    
    #puertos "C:\APPS\006- Proyecto Instalador de servicio\Instalador Servicio Unicos V0.110\Codigo Fuente\Sidesys\Middleware\Appointment\bin\ServiceModelConfig\Service.config" 10505 Details
    replaceCadena(f'{path}/Middleware/Appointment/bin/ServiceModelConfig/Services.config',
                'baseAddress="http://\S*:\w*/Design_Time_Addresses/Appointment.Core.SchedulingOperation/SchedulingOperationDetailService/', 
                f'baseAddress="http://{url}:{port}05/Design_Time_Addresses/Appointment.Core.SchedulingOperation/SchedulingOperationDetailService/',loggin,datetime)
    
#changePort("C:\sidesysT","041") 
    
#replacePort(content,patron, service)
def validatePort(port):
    if(len(port)!=3):return True
    else:return False
