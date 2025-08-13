from Middleware.funcionesAuxiliares import replaceCadena

def configurarSuite(path,server,suite,im,loggin,datetime): 
    #"..\FrontEnd\Suite\index.html"
    replaceCadena(f'{path}/FrontEnd/Suite/index.html',
                '<base href="[\S|\\b|" "]+"', 
                f'<base href="http://{server}/{suite}/"',loggin,datetime)
    
     #"..\FrontEnd\Suite\Web.config"
    replaceCadena(f'{path}/FrontEnd/Suite/Web.config',
                '<action type="Rewrite" url=[\S|\\b|" "]+/" />', 
                f'<action type="Rewrite" url="/{suite}/" />',loggin,datetime)
    
     #"..\FrontEnd\Suite\assets\appsettings.json"
    replaceCadena(f'{path}/FrontEnd/Suite/assets/appsettings.json',
                '"baseUrl":[\S|\\b|" "]+",', 
                f'"baseUrl": "http://{server}/{suite}/",',loggin,datetime)
    
    #"..\FrontEnd\Suite\assets\appsettings.json"
    replaceCadena(f'{path}/FrontEnd/Suite/assets/appsettings.json',
                '"identityManager":[\S|\\b|" "]+"', 
                f'"identityManager": "http://{server}/{im}/"',loggin,datetime)
    
    #"..\Middleware\IM\appsettings.json"
    replaceCadena(f'{path}/Middleware/IM/appsettings.json',
                '"SelfUrl": "[\S|\\b|" "]+",', 
                f'"SelfUrl": "http://{server}/{im}/",',loggin,datetime)
    
    #"..\Middleware\IM\appsettings.json"
    replaceCadena(f'{path}/Middleware/IM/appsettings.json',
                '"ClientUrl": "[\S|\\b|" "]+",', 
                f'"ClientUrl": "http://{server}/{suite}/",',loggin,datetime)
    
    #"..\Middleware\IM\appsettings.json"
    replaceCadena(f'{path}/Middleware/IM/appsettings.json',
                '"CorsOrigins": "[\S|\\b|" "]+",', 
                f'"CorsOrigins": "http://{server}",',loggin,datetime)
    
    #"..\Middleware\IM\appsettings.json"
    replaceCadena(f'{path}/Middleware/IM/appsettings.json',
                '"Authority": "[\S|\\b|" "]+",', 
                f'"Authority": "http://{server}/{im}/",',loggin,datetime)
    
def configurarBBDDSuite(path,bbdd,loggin,datetime): 
    print(bbdd)
    #"..\Middleware\IM\appsettings.json"
    replaceCadena(f'{path}/Middleware/IM/appsettings.json',
                '"Default":[\S|\\b|" "]+"', 
                f'"Default": "{bbdd}"',loggin,datetime)
    
def configurarCitasSuite(path,citasim,loggin,datetime): 
    print(citasim)
    
    
    #"C:\Sidesys\Middleware\Appointment\ConfigFiles\IMIntegration.config"
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config',
                '<identityManager>[\S|\\b|" "]+</identityManager>', 
                f'<identityManager>{citasim[0]}</identityManager>',loggin,datetime)
    
    #"C:\Sidesys\Middleware\Appointment\ConfigFiles\IMIntegration.config"
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config',
                '<tenantAppointment>[\S|\\b|" "]+</tenantAppointment>', 
                f'<tenantAppointment>{citasim[1]}</tenantAppointment>',loggin,datetime)
    
     #"C:\Sidesys\Middleware\Appointment\ConfigFiles\IMIntegration.config"
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config',
                '<UserNameAdminTenant>[\S|\\b|" "]+</UserNameAdminTenant>', 
                f'<UserNameAdminTenant>{citasim[2]}</UserNameAdminTenant>',loggin,datetime)
    
    #"C:\Sidesys\Middleware\Appointment\ConfigFiles\IMIntegration.config"
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config',
                '<PasswordAdminTenant>[\S|\\b|" "]+</PasswordAdminTenant>', 
                f'<PasswordAdminTenant>{citasim[3]}</PasswordAdminTenant>',loggin,datetime)
    
     #"C:\Sidesys\Middleware\Appointment\ConfigFiles\IMIntegration.config"
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config',
                '<ClientIdAppointment>[\S|\\b|" "]+</ClientIdAppointment>', 
                f'<ClientIdAppointment>{citasim[4]}</ClientIdAppointment>',loggin,datetime)
    
    #"C:\Sidesys\Middleware\Appointment\ConfigFiles\IMIntegration.config"
    replaceCadena(f'{path}/Middleware/Appointment/ConfigFiles/IMIntegration.config',
                '<ClientSecretAppointment>[\S|\\b|" "]+</ClientSecretAppointment>', 
                f'<ClientSecretAppointment>{citasim[5]}</ClientSecretAppointment>',loggin,datetime)

    #"..\Middleware\IM\appsettings.json"
    
    
    
    
    
    
 