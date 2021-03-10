#Easy way to get notified when a script finishes running instead of interrupting my movie and checking the progress. 
#This is a package to give me Toast Notifications — win10toast

#The package has been published in Pypi and can be easly installed with pip.
#pip install win10toast


from win10toast import ToastNotifier

# Instance the module in a variable
toast = ToastNotifier()

# Passs the parameters in a variable
toast.show_toast(title="Notificacion de Finalización Script",       # titulo
                 msg="Termino el programitaaaa :D",     # mensaje
                 duration=20,                           # duracion
                 icon_path="linkedin_icon.ico")         # path de icono