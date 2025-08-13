from FrontEnd.VariableDeterminadas import *

#esta funcion se encarga de examinar los minutos de la sesion del usuario
def ExamineDirectoryConsoleSesion(label):
  logging.info(f' {datetime.datetime.now() }: Se esta seleccionando el directorio para la carga de la sesion en consola')
  Path = tkinter.filedialog.askdirectory()
  if(True):
    logging.info(f' {datetime.datetime.now() }: Se selecciono el directorio {Path}')
    Path = Path.replace("/", r"\ ".strip())
    Path=Path.rstrip()
    label.config(text=Path) 
    minuteSesion.set(identifyMinuteSesion(Path,logging, datetime))
    return Path

#esta funcion se encarga de modificar el tiempo de sesion de la consola
def modifyConsoleSesion():
  logging.info(f' {datetime.datetime.now() }: Se comienza a modificar la ejecucion de la consola de sesion')
  bandera=validateField(spinMinuteConsole,logging,MessageBox,"el horario de el tiempo de ejecucion de tiempo de consola","de los minutos de la sesion",datetime) 
  bandera=bandera*validateLabel(label13,logging,MessageBox,"el horario de el tiempo de ejecucion de tiempo de consola","la ruta",datetime) 
  if(bandera):
    logging.info(f' {datetime.datetime.now() }: Se comienza a modificar la ejecucion del historico integrado paso correctamente')
    configurarMinuteConsole(label13.cget("text"),spinMinuteConsole.get(),logging,datetime)
    tk.messagebox.showinfo(title="Felicidades", message="Se modifico correctamente el tiempo de sesion.")