from FrontEnd.VariableDeterminadas import *


def updateVirtualQueue():  
  updatesVirtualQueue(label21.cget("text"),TextboxReporteriaVQDB.get(),TextboxReporteriaVQMSMQWebConfig.get(),TextboxReporteriaVQMSMQMiddlewareSTE.get(),logging,datetime)  

#esta funcion se encarga de cargar los datos de Virtual Queue
def loadDataVQ(path):
  TextboxReporteriaVQDB.delete(0, tk.END)
  TextboxReporteriaVQMSMQWebConfig.delete(0, tk.END)
  TextboxReporteriaVQMSMQMiddlewareSTE.delete(0, tk.END)
  Insert(TextboxReporteriaVQDB,identifyBaseURL(f"{path}/FrontEnd/VirtualQueue/web.config",'<add name="Default" connectionString="[\S|\\b|" "]+"','connectionString=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaVQMSMQWebConfig,identifyBaseURL(f"{path}/FrontEnd/VirtualQueue/web.config",'<add key="IncomingEventsReceiveQueuePath" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaVQMSMQMiddlewareSTE,Identify(f"{path}/Middleware/STE/ConfigFiles/VirtualQueue.config",'<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>','<OutgoingEventsSendQueuePath>[\S|\\b|" "]+</OutgoingEventsSendQueuePath>',logging,datetime),logging,datetime)
  