from FrontEnd.Component import *


#inicializa el frame principal
frameMenuPrincipal.pack()
#Carga la configuracion de los frames
for components  in component:loadComponent(components)
menu.mainloop()