import bd_mod

#MENU PRINCIPAL
def Menu():
	print "\n"
	print"                                ********************"
	print"                                * FICHEROS ALUMNOS *"
	print"                                ********************\n"
	print"----------------------------"
	print" ---  ELIJA UNA OPCION  --- "
	print"----------------------------\n"
	print"1) Alumnos"
	print"X) Salir\n "
	opcion=raw_input("OPCION: ")
	if opcion=="1":
		SubAlumnos()
	elif opcion.lower()=="x":
		print'\n'
		print "saliendo..."
		bd_mod.close(cur)
		exit()
	else:
		print'\n'
		print"No ha elgido ninguna opcion..."
		raw_input("pulsa ENTER para continuar")

#MENU ALUMNOS
def SubAlumnos():
	while True:
		print "\n"
		print" //ALUMNOS//\n"
		print"******ELIJA UNA OPCION******\n"
		print "1) Dar de alta un alumno"
		print "2) Modificar un alumno"
		print "3) Dar de baja un alumno"
		print "4) Ver datos de un alumno"
		print "5) Listar todos los alumnos"
		print "X) Volver al Menu anterior\n"
		opcion=raw_input("OPCION: ")
		if opcion=="1":
			AltaAlumno()
		elif opcion=="2":
			ModificarAlumno()
		elif opcion=="3":
			BajaAlumno()
		elif opcion=="4":
			VerAlumno()
		elif opcion=="5":
			ListaAlumnos()
		elif opcion.lower()=="x":
			break
		else:
			print"No ha elgido ninguna opcion..."
			raw_input("pulsa ENTER para continuar")

def AltaAlumno():
	dni = raw_input('Introduzca DNI: ')
	try:
		int(dni)
	except:
		raw_input("SOLO NUMEROS!! / Pulsa ENTER para continuar\n")
		return
	datos = bd_mod.getAlumno(cur, dni)
	if datos != None:
		raw_input('ESTE DNI YA EXISTE!!!!: \n/ Pulsa ENTER para continuar'), datos[0]
		return
	apellido = raw_input('Introduzca Apellido: ')
	nombre = raw_input('Introduzca Nombre: ')
	fnacimiento = raw_input('Introduzca Fecha de Nacimiento: ')
	fingreso = raw_input('Fecha de Ingreso: ')
	bd_mod.insertAlumno(cur, (dni, apellido, nombre, fnacimiento, fingreso ) )
	print'\n'
	print "Se agrego el alumno con Dni: ", dni
	raw_input("pulsa ENTER para continuar")

def VerAlumno():
	dni = raw_input('Introduzca DNI: ')
	try:
		int(dni)
	except:
		raw_input("SOLO NUMEROS!! / Pulsa ENTER para continuar\n")
		return
	datos = bd_mod.getAlumno(cur, dni)
	if datos != None:
		print '\n'
		print 'DNI: ', datos[0]
		print 'Apellido: ', datos[1]
		print 'Nombre: ', datos[2]
		print 'Fecha de Nacimiento: ', datos[3]
		print 'Fecha de ingreso: ', datos[4],"\n"
	else:
		print '\n'
		print "NO EXISTE EL DNI QUE INTENTA INGRESAR!!!\n"
	raw_input("pulsa ENTER para continuar")

def ModificarAlumno():
	dni = raw_input('Introduzca DNI: ')
	try:
		int(dni)
	except:
		raw_input("SOLO NUMEROS!! / Pulsa ENTER para continuar\n")
		return
	datos = bd_mod.getAlumno(cur, dni)
	if datos != None:
		print 'DNI: ', datos[0]
		print 'Apellido: ', datos[1]
		print 'Nombre: ', datos[2]
		print 'Fecha de Nacimiento: ', datos[3]
		print 'Fecha de ingreso: ', datos[4], '\n'
		print 'INGRESE NUEVOS DATOS \n'
		apellido = raw_input('Introduzca Apellido: ')
		nombre = raw_input('Introduzca Nombre: ')
		fnacimiento = raw_input('Introduzca Fecha de Nacimiento: ')
		fingreso = raw_input('Fecha de Ingreso: ')
		bd_mod.updateAlumno(cur, (dni, apellido, nombre, fnacimiento, fingreso ) )
		print'\n'
		print "SE MODIFICO CON EXITO!..."
	else:
		print'\n'
		print "NO EXISTE EL DNI QUE INTENTA INGRESAR!!!\n"
	raw_input("pulsa ENTER para continuar")

def BajaAlumno():
	dni = raw_input('Introduzca DNI: ')
	try:
		int(dni)
	except:
		raw_input("SOLO NUMEROS!! / Pulsa ENTER para continuar\n")
		return
	datos = bd_mod.getAlumno(cur, dni)
	if datos != None:
		print'\n'
		print 'DNI: ', datos[0]
		print 'Nombre: ', datos[2]
		print 'Apellido: ', datos[1], '\n'
		print "!!!Esta seguro de que quiere borrar el archivo!!!? si/no\n"
		borrar2=raw_input("\\")
		if borrar2.lower() == "si":
			bd_mod.deleteAlumno(cur, dni)
			print'\n'
			raw_input( "----EL FICHERO SE BORRO!----/ Pulsa ENTER para continuar\n")
		else:
			print'\n'
			raw_input( "EL FICHERO NO SE BORRO!/ Pulsa ENTER para continuar\n")
	else:
		print'\n'
		raw_input("NO EXISTE EL DNI QUE INGRESO!\n/ Pulsa ENTER para continuar\n")

def ListaAlumnos():
	lista_alumnos = bd_mod.listarAlumnos(cur)
	print "======= Listado de Alumnos ======="
	count = 0
	for datos in lista_alumnos:
		print "DNI: %s, Apellido: %s" % (datos[0], datos[1])
		count+=1
	print "Total: %d alumnos" % (count)
	print "===============ooo================"
	print
	raw_input("pulsa ENTER para continuar")

cur = bd_mod.getCursor('database.sqlite')

while True:
	Menu()

