import requests


def loginVirtualQueue(vq,user,password,typeDocument,numberDocument,logging, datetime):
    logging.info(f' {datetime.datetime.now() }: Se comienza a realizar el request')
    data = {
        "username": user,
        "password": password,
        "docType": typeDocument,
        "docNumber": numberDocument,
        "client_Id": "mobileclient.virtualqueue",
        "client_Secret": "1a4805ac784c56662cd4aad56f0b21024215de18f2da5c01918dead7ce4f1115",
        "callbackToken": "123456789qwerty",
    }   
    logging.info(f' {datetime.datetime.now() }: Data> {data}')
    try:
        response = requests.post(f'{vq}/api/services/client/Auth/Token', json=data)
   
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            print('Solicitud exitosa!')
            print('Respuesta:', response.json())  # Mostrar el contenido de la respuesta
            logging.info(f' {datetime.datetime.now() }: Solicitud exitosa!')
            logging.info(f' {datetime.datetime.now() }: Respuesta:{response.json()}')
            token=response.json()
            return token.get("result")
        else:
            logging.info(f' {datetime.datetime.now() }: Respuesta:{response.status_code}')
            return response.status_code
    except Exception as e:
        return e
    
def getAllOrganization(vq,token,logging, datetime):
    logging.info(f' {datetime.datetime.now() }: Se comienza a realizar el request')
    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
    try:
        response =  requests.get(f'{vq}/api/services/client/Organization/GetAll',headers=headers)
   
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            print('Solicitud exitosa!')
            print('Respuesta:', response.json())  # Mostrar el contenido de la respuesta
            logging.info(f' {datetime.datetime.now() }: Solicitud exitosa!')
            logging.info(f' {datetime.datetime.now() }: Respuesta:{response.json()}')
            return response.json().get("result")
        else:
            logging.info(f' {datetime.datetime.now() }: Respuesta:{response.status_code}')
            return response.status_code
    except Exception as e:
        return e
    
def getAllServiceByOrganization(vq,token,orgId,logging, datetime):
    logging.info(f' {datetime.datetime.now() }: Se comienza a realizar el request para obtener los servicios')
   
    headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
    try:
        response =  requests.get(f'{vq}/api/services/client/Service/GetAvailable?pOrgId={orgId}',headers=headers)
   
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            print('Solicitud exitosa!')
            print('Respuesta:', response.json())  # Mostrar el contenido de la respuesta
            logging.info(f' {datetime.datetime.now() }: Solicitud exitosa!')
            logging.info(f' {datetime.datetime.now() }: Respuesta:{response.json()}')
            return response.json().get("result")
        else:
            logging.info(f' {datetime.datetime.now() }: Respuesta:{response.status_code}')
            return response.status_code
    except Exception as e:
        return e
    
        