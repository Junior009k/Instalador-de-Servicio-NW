from FrontEnd.VariableDeterminadas import *


#esta funcion se encarga de Seleccionar el directorio y carga las horas
def ExamineDirectoryRHI(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la carga de hora y minutos del proceso historico')
  Path = tkinter.filedialog.askdirectory()
  if(True):
    logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
    Path = Path.replace("/", r"\ ".strip())
    Path=Path.rstrip()
    label.config(text=Path) 
    hour.set(identifyHour(Path,logging, datetime))
    minute.set(identifyMinute(Path,logging, datetime))
    return Path
#esta funcion se encarga de modificar la ejecucion del reporte historico integrado
def modifyRHI():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar la ejecucion del historico integrado')
  bandera=validateField(spinHour,logging,MessageBox,"el horario de ejecucion del historico","las Horas",datetime)
  bandera=bandera*validateField(spinMinute,logging,MessageBox,"el horario de ejecucion del historico","los minutos",datetime)
  bandera=bandera*validateLabel(label10,logging,MessageBox,"el horario de ejecucion del historico","la ruta",datetime)
  if(bandera!=False):
    logging.info(f' {datetime.datetime.now() }: Se comienza a modificar la ejecucion del historico integrado paso correctamente')
    configurarHorario(label10.cget("text"),spinHour.get(),spinMinute.get(),logging,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="La hora de ejecucion del historico integrado se modifico correctamente")