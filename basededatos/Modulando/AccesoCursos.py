import basedatos

#MENU PRINCIPAL
def Menu():
	print" //MENU PRINCIPAL//\n"
	print"----------------------------"
	print" ---  ELIJA UNA OPCION  --- "
	print"----------------------------\n"
	print"1) Alumnos"
	print"2) Cursos"
	print"3) Inscripciones"
	print"4) Informes"
	print"5) Salir\n "
	opcion=raw_input("OPCION: ")
	if opcion=="1":
		SubAlumnos()
	elif opcion == "2":
		SubCursos()
	elif opcion == "3":
		SubInscripciones()
	elif opcion == "4":
		SubInformes()
	elif opcion=="5":
		print
		print "saliendo..."
		basedatos.close(cur)
		exit()
	else:
		print
		raw_input("No ha elgido ninguna opcion./pulsa una tecla")
		
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
		print "5) Volver al Menu anterior\n"
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
			break
		else:
			raw_input("No ha elgido ninguna opcion./pulsa una tecla")

def AltaAlumno():
	dni = raw_input('Introduzca DNI: ')
	try:
		int(dni)
	except:
		raw_input("SOLO NUMEROS!! / Pulsa una tecla\n")
		return
	datos = basedatos.getAlumno(cur, dni)
	if datos != None:
		raw_input('ESTE DNI YA EXISTE!!!!: \n/ Pulsa una tecla'), datos[0]
		return
	apellido = raw_input('Introduzca Apellido: ')
	nombre = raw_input('Introduzca Nombre: ')
	fnacimiento = raw_input('Introduzca Fecha de Nacimiento: ')
	fingreso = raw_input('Fecha de Ingreso: ')
	basedatos.insertAlumno(cur, (dni, apellido, nombre, fnacimiento, fingreso ) )
	print'\n'
	print "Se agrego el alumno con Dni: ", dni
	raw_input("pulsa una tecla")

def VerAlumno():
	dni = raw_input('Introduzca DNI: ')
	try:
		int(dni)
	except:
		raw_input("SOLO NUMEROS!! / Pulsa ENTER para continuar\n")
		return
	datos = basedatos.getAlumno(cur, dni)
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
		raw_input("SOLO NUMEROS!! / Pulsa una tecla\n")
		return
	datos = basedatos.getAlumno(cur, dni)
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
		basedatos.updateAlumno(cur, (dni, apellido, nombre, fnacimiento, fingreso ) )
		print
		raw_input("SE MODIFICO CON EXITO!./pulsa una tecla")
	else:
		print
		raw_input("NO EXISTE EL DNI QUE INTENTA INGRESAR!/pulsa una tecla")

def BajaAlumno():
	dni = raw_input('Introduzca DNI: ')
	try:
		int(dni)
	except:
		raw_input("SOLO NUMEROS!! / Pulsa una tecla\n")
		return
	datos = basedatos.getAlumno(cur, dni)
	if datos != None:
		print'\n'
		print 'DNI: ', datos[0]
		print 'Nombre: ', datos[2]
		print 'Apellido: ', datos[1], '\n'
		print 
		borrar2=raw_input("!Esta seguro de que quiere borrar el archivo!?/ si/no")
		if borrar2.lower() == "si":
			basedatos.deleteAlumno(cur, dni)
			print
			raw_input( "-EL ALUMNO SE BORRO!-/ Pulsa una tecla\n")
		else:
			print
			raw_input("-EL ALUMNO NO SE BORRO!-/ Pulsa una tecla\n")
	else:
		print
		raw_input("NO EXISTE EL DNI QUE INGRESO!\n/ Pulsa una tecla\n")

#MENU CURSOS
def SubCursos():
	while True:
		print "\n"
		print"//CURSOS//\n"
		print"******ELIJA UNA OPCION******\n"
		print"1) Dar de alta un curso"
		print"2) Modificar un curso"
		print"3) Dar de baja un curso"
		print"4) Ver informacion basica de un curso"
		print"5) Volver al menu anterior\n"
		opcioncurso=raw_input("OPCION: ")
		if opcioncurso =="1":
			AltaCurso()
		elif opcioncurso =="2":
			ModCurso()
		elif opcioncurso =="3":
			BajaCurso()
		elif opcioncurso =="4":
			VerCurso()
		elif opcioncurso =="5":
			break
		else:
			raw_input("No ha elgido ninguna opcion!/.Pulsa una tecla para continuar")

def AltaCurso():
	try:
		codigo = raw_input('Introduzca Codigo: ')
		int(codigo)
	except:
		print'\n'
		raw_input("SOLO NUMEROS!! / Pulsa una tecla para continuar\n")
		return
	datos = basedatos.getCurso(cur, codigo)
	if datos != None:
		print'\n'
		raw_input("YA EXISTE EL CODIGO QUE INTENTA INGRESAR!!!\n/ Pulsa una tecla para continuar\n"), datos[0]
		return 
	titulo = raw_input('Introduzca Titulo: ')
	descripcion = raw_input('Introduzca Descripcion: ')
	fechainicio = raw_input('Introduzca Fecha de inicio: ')
	fechafin = raw_input('Fecha de finalizacion: ')
 	basedatos.insertCurso(cur, (codigo, titulo, descripcion, fechainicio, fechafin ) )
 	print'\n'
 	print "Se agrego el curso con codigo: ", codigo
			
def ModCurso():
	try:
		codigo = raw_input('Introduzca Codigo del curso: ')
		int(codigo)
	except:
		print'\n'
		raw_input("SOLO NUMEROS!! / Pulsa una tecla para continuar\n")
		return
	datos = basedatos.getCurso(cur, codigo)
	if datos != None:
		print'\n'
		print 'Codigo: ', datos[0]
		print 'Titulo: ', datos[1]
		print 'Descripcion: ', datos[2]
		print 'Fecha de inicio: ', datos[3]
		print 'Fecha de finalizacion: ', datos[4], '\n'
		print 'INGRESE NUEVOS DATOS\n'
		ntitulo = raw_input('Introduzca Titulo: ')
		ndescripcion = raw_input('Introduzca Descripcion: ')
		nfechainicio = raw_input('Introduzca Fecha de inicio: ')
		nfechafin = raw_input('Fecha de finalizacion: ')
		basedatos.updateCurso(cur, (codigo, ntitulo, ndescripcion, nfechainicio, nfechafin ) )
		print '\n'
		raw_input( "SE MODIFICO CON EXITO.../ Pulsa una tecla para continuar\n")
	else:
		print'\n'
		raw_input("NO EXISTE EL CODIGO QUE INTENTA INGRESAR!!!/ Pulsa una tecla para continuar\n")

def BajaCurso():
	try:
		codigo = raw_input('Introduzca Codigo: ')
		int(codigo)
	except:
		print'\n'
		raw_input("SOLO NUMEROS!! / Pulsa una tecla para continuar\n")
		return
	datos = basedatos.getCurso(cur, codigo)
	if datos != None:
		print 'Codigo: ', datos[0]
		print 'Titulo: ', datos[1]
		print 'Descripcion: ', datos[2], '\n'	
		borrar2=raw_input("Esta seguro de que quiere borrar el curso? si/no\n")
  		if borrar2.lower() == "si":
			basedatos.deleteCursos(cur, codigo)
			print'\n'
			raw_input( "EL CURSO SE BORRO/ Pulsa una tecla para continuar\n")
		else:
			print'\n'
			raw_input( "EL CURSO NO SE BORRO/ Pulsa una tecla para continuar\n")		
	else:
		print'\n'
		raw_input( "NO EXISTE EL CURSO!!/ Pulsa una tecla para continuar\n")

def VerCurso():
	try:
		codigo = raw_input('Introduzca Codigo del curso: ')
		int(codigo)
	except:
		print'\n'
		raw_input("SOLO NUMEROS!! / Pulsa una tecla para continuar\n")
		return
	datos = basedatos.getCurso(cur, codigo)
	if datos != None:
		print'\n'
		print 'Codigo: ', datos[0]
		print 'Titulo: ', datos[1]
		print 'Descripcion: ', datos[2]
		print 'Fecha_de_inicio: ', datos[3]
		print 'Fecha_de_finalizacion: ', datos[4],"\n"
		raw_input("Pulsa una tecla para continuar")
	else:
		print'\n'
		raw_input("NO EXISTE EL CURSO QUE INTENTA INGRESAR!/Pulsa una tecla\n")

#INSCRIPCIONES
def SubInscripciones():
	while True:
		print "\n"
		print"//INSCRIPCIONES//\n"
		print"******ELIJA UNA OPCION******\n"
		print"1) Inscribir un alumno a un curso"
		print"2) Cancelar incripcion de un alumno a un curso" 
		print"3) Volver al menu anterior\n"
		opcioncurso=raw_input("OPCION: ")
		if opcioncurso =="1":
			Inscripcion()
		elif opcioncurso =="2":
			CancelarIns()
		elif opcioncurso =="3":
			break
		else:
			raw_input("No ha elgido ninguna opcion!/.Pulsa una tecla para continuar")

def Inscripcion():
	try:
		dni = raw_input('Introduzca DNI para la Inscripcion: ')
		int(dni)
	except:
		print'\n'
		raw_input("SOLO NUMEROS!! / Pulsa una tecla para continuar\n")
		return
	datos = basedatos.getAlumno(cur, dni)
	if datos != None:
		print'\n'
		print 'DNI: ', datos[0]
		print 'Apellido: ', datos[1]
		print 'Nombre: ', datos[2],"\n"
		confirm=raw_input("Este Alumno desea Inscribir a un curso? si/no : ")
		if confirm.lower() == "si":
			print confirm
		elif confirm.lower() == "no":
			return	
	else:
		print'\n'
		raw_input("NO EXISTE EL DNI QUE INTENTA INGRESAR!!!/ pulsa una tecla\n")
		return 
	try:
		codigo = raw_input('Introduzca Codigo del curso: ')
		int(codigo)
	except:
		print'\n'
		raw_input("SOLO NUMEROS!! / Pulsa una tecla para continuar\n")
		return
	datos = basedatos.getCurso(cur, codigo)
	if datos!= None:
		print'\n'
		print 'Titulo: ', datos[1]
		print 'Descripcion: ', datos[2]
		print 'Fecha_de_inicio: ', datos[3]
		print 'Fecha_de_finalizacion: ', datos[4],"\n"
		confirm=raw_input("Desea Inscribir al alumno en este Curso? si/no : ")
		if confirm.lower()=="si":
			print
		elif confirm.lower()=="no":
			return	
#	datos2=basedatos.inscriptos(cur, dni, codigo)
#	if datos2!=None:
#		raw_input("ya esta inscripto")
#		return
	else:
		print'\n'
		raw_input("NO EXISTE EL CURSO QUE INTENTA INGRESAR!/pulsa una tecla")
		return
	try:
		nota = raw_input('Introduzca la Nota: ')
		basedatos.Inscribir(cur, (codigo, dni, nota ) )
		print'\n'
		print "DNI:", dni, "Nota: ", nota, '\n'
		raw_input("pulse una tecla")
	except:
		raw_input("surgio un error, puede que el Alumno ya este inscripto")

def CancelarIns():
	try:
		dni = raw_input('Introduzca DNI: ')
		int(dni)
	except:
		print'\n'
		raw_input("SOLO NUMEROS!! / Pulsa una tecla para continuar\n")
		return
	datos= basedatos.getInscp(cur, dni)
	if datos != None:
		print 'Codigo:', datos[0],'DNI:', datos[1], 'Nota:', datos[2], '\n'
		confirm=raw_input("Desea continuar? si/no : ")
		if confirm.lower()=="si": 
			next 
		if confirm.lower()=="no":
			return	
	else:
		print'\n'
		raw_input("EL DNI QUE INTENTA INGRESAR NO ESTA INSCRIPTO EN NINGUN CURSO!!!/ pulse una tecla\n")
		return 
	try:
		codigo = raw_input('Introduzca Codigo del curso: ')
		int(codigo)
	except:
		print'\n'
		raw_input("SOLO NUMEROS!! / Pulsa una tecla para continuar\n")
		return
	datos= basedatos.CursosIn(cur,codigo)
	if datos != None:
		borrar2=raw_input("Esta seguro de que quiere cancelar la Inscripcion? si/no\n")
  		if borrar2.lower() == "si":
			basedatos.deleteIn(cur, dni, codigo)
			print'\n'
			raw_input( "-LA INSCRIPCION SE BORRO!-/ Pulsa una tecla\n")
		else:
			print'\n'
			raw_input( "LA INSCRIPCION NO SE BORRO!/ Pulsa una tecla\n")
	else:
		print'\n'
		raw_input("NO EXISTE EL CODIGO EN TABLA DE INSCRIPCIONES!/pulsa una tecla")

#MENU INFORMES
def SubInformes():
	while True:
		print "\n"
		print"//INFORMES//\n"
		print"******ELIJA UNA OPCION******\n"
		print"1) Lista de Alumnos"
		print"2) Lista de Cursos"
		print"3) Lista de Alumnos imcriptos en cursos"
		print"4) Volver al menu anterior\n"
		opcioninfo=raw_input("OPCION: ")
		if opcioninfo =="1":
			ListaAlumnos()
		elif opcioninfo =="2":
			ListaCursos()
		elif opcioninfo =="3":
			ListaInscripciones()
		elif opcioninfo =="4":
			break
		else:
			raw_input("No ha elgido ninguna opcion./pulsa una tecla")

def ListaAlumnos():
	lista_alumnos = basedatos.listarAlumnos(cur)
	print "------- Listado de Alumnos --------"
	count = 0
	for datos in lista_alumnos:
		print "DNI: %s, Apellido: %s" % (datos[0], datos[1])
		count+=1
	print "Total: %d alumnos" % (count)
	print "-----------------------------------"
	print
	raw_input("pulsa una tecla")

def ListaCursos():
	lista_cursos = basedatos.viewCursos(cur)
	print "-------- Listado de Cursos --------"
	count = 0
	for datos in lista_cursos:
		print "Codigo: %s, Titulo: %s, Descripcion: %s" % (datos[0], datos[1], datos[2])
		count+=1
	print "Total: %d Cursos" % (count)
	print "-----------------------------------"
	print
	raw_input("pulsa una tecla para continuar")

def ListaInscripciones():
	try:
		codigo = raw_input('Introduzca Codigo del curso: ')
		int(codigo)
	except:
		print'\n'
		raw_input("SOLO NUMEROS!! / Pulsa una tecla para continuar\n")
		return
	datos = basedatos.getCurso(cur, codigo)
	if datos != None:
		inscriptos=basedatos.verInscripciones(cur, codigo)
		print "-------- Listado de Cursos --------"
		for datos in inscriptos:
			print "Curso: %s, DNI: %s, Nota: %s" % (datos[0],datos[1], datos[2])
		print "-----------------------------------"
		raw_input("Pulsa una tecla para continuar")
	else:
		print'\n'
		raw_input( "NO EXISTE EL CURSO QUE INTENTA INGRESAR!!! /pulse una tecla/\n"	)

cur = basedatos.getCursor('BaseDatos.sqlite')

while True:
	Menu()