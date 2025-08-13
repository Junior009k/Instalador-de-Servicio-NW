from FrontEnd.VariableDeterminadas import *

#esta funcion se encarga de modificar los parametros de encuestas
def modifyPoll():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar  Encuesta')
  bandera=validateField(TextboxsvrEncuesta,logging,MessageBox,"Encuesta","del servidor",datetime)
  bandera=bandera*(TextboxsvrEncuesta,logging,MessageBox,"Encuesta","del sitio de Encuesta",datetime)
  bandera=bandera*validateField(TextboxsvrEncuesta,logging,MessageBox,"Encuesta","del sitio de e-Flow",datetime)
  bandera=bandera*validateLabel(label12,logging,MessageBox,"Encuesta","la ruta",datetime)
  if( validateDirectory(label12.cget("text"),"Middleware",logging,datetime)  or validateDirectory(label12.cget("text"),"FrontEnd",logging,datetime)):label12.config(text="") 
  bandera=bandera*validateLabel(label12,logging,MessageBox,"Encuesta","tiene que estar en la carpeta del aplicativo")
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Paso todas las pruebas, comenzando proceso de modificacion de encuesta')
    configurarEncuesta(label12.cget("text"),TextboxsvrEncuesta.get(),TextboxEncuesta.get(),TextboxEflowEncuesta.get(),logging,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="El aplicativo de Encuesta termino el proceso de configuracion de los archivos")
#esta funcion se encarga de actualizar los campos en Encuesta
def updatePoll():
  updateEncuestas(label21.cget("text"),TextboxReporteriaSTEWebConfig.get(),TextboxReporteriaReportePoll.get(),TextboxReporteriaOpinionPollIndex.get(),TextboxReporteriaSettingPoll.get(),TextboxReporteriaMiddlewareOpinionPoll.get(),TextboxReporteriaMiddlewareSTE.get(),logging,datetime)

#esta funcion se encarga de cargar los datos de encuesta
def loadDataPoll(path):
  TextboxReporteriaSTEWebConfig.delete(0, tk.END)
  TextboxReporteriaReportePoll.delete(0, tk.END)
  TextboxReporteriaOpinionPollIndex.delete(0, tk.END)
  TextboxReporteriaSettingPoll.delete(0, tk.END)
  TextboxReporteriaMiddlewareOpinionPoll.delete(0, tk.END)
  TextboxReporteriaMiddlewareSTE.delete(0, tk.END)
  Insert(TextboxReporteriaSTEWebConfig,identifyBaseURL(f"{path}/FrontEnd/STE/Web.config",'<add key="OpinionPollPath" value=[\S|\\b|" "]+','value=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaReportePoll,identifyBaseURL(f"{path}/FrontEnd/STE/Reportes/Poll/app/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaOpinionPollIndex,identifyBaseURL(f"{path}/FrontEnd/OpinionPoll/index.html",'<base href=[\S|\\b|" "]+','href=[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaSettingPoll,identifyBaseURL(f"{path}/FrontEnd/OpinionPoll/assets/settings.json",'"pollApiBaseUrl":[\S|\\b|" "]+',':[\S|\\b|" "]+',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaMiddlewareOpinionPoll,Identify(f"{path}/Middleware/OpinionPoll/ConfigFiles/OpinionPoll.config",'<eFlow>[\S|\\b|" "]+</eFlow>','<eFlow>[\S|\\b|" "]+</eFlow>',logging,datetime),logging,datetime)
  Insert(TextboxReporteriaMiddlewareSTE,Identify(f"{path}/Middleware/STE/ConfigFiles/OpinionPoll.config",'<Path>[\S|\\b|" "]+</Path>','<Path>[\S|\\b|" "]+</Path>',logging,datetime),logging,datetime)    
  