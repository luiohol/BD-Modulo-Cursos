#Luis Benedetich
import sqlite3

def getCursor(BaseDatos):
  connection = sqlite3.connect(BaseDatos)
  return connection.cursor()

def close(cursor):
  cursor.connection.close()
#Alumnos
def getAlumno(cursor, dni):
  sql='SELECT * FROM Alumnos WHERE DNI='+dni
  cursor.execute(sql)
  return cursor.fetchone()

def insertAlumno(cursor, datos):
  cursor.execute('INSERT INTO Alumnos (DNI, Apellido, Nombre, Fecha_de_Nacimiento, Fecha_de_Ingreso) VALUES ( ?, ?, ?, ?, ? )',
              datos )
  cursor.connection.commit()

def updateAlumno(cursor, datos):
  sql="UPDATE Alumnos SET Apellido = '"+ datos[1] +"',Nombre = '"+ datos[2] +"',Fecha_de_Nacimiento = '"+ datos[3] +"', Fecha_de_Ingreso = '"+ datos[4] +"' WHERE DNI="+ datos[0]
  cursor.execute(sql)

def deleteAlumno(cursor, dni):
  borrar='DELETE FROM Alumnos WHERE DNI = %d' % (int(dni))
  cursor.execute(borrar)
  borrar='DELETE FROM Inscripciones WHERE DNI = %d' % (int(dni))
  cursor.execute(borrar)
  cursor.connection.commit()

def listarAlumnos(cursor):
  sql='SELECT * FROM Alumnos'
  cursor.execute(sql)
  return cursor.fetchall()

#Cursos
def getCurso(cursor, codigo):
	sql='SELECT * FROM Cursos WHERE Codigo='+codigo
	cursor.execute(sql)
	return cursor.fetchone()

def insertCurso(cursor, datos):
	cursor.execute('INSERT INTO Cursos (Codigo, Titulo, Descripcion, Fecha_de_inicio, Fecha_de_finalizacion) VALUES (?, ?, ?, ?, ?)',
 				datos )
 	cursor.connection.commit()

def updateCurso(cursor, datos):
	sql2="UPDATE Cursos SET Titulo = '"+ datos[1] +"',Descripcion = '"+ datos[2] +"',Fecha_de_inicio = '"+ datos[3] +"', Fecha_de_finalizacion = '"+ datos[4] +"' WHERE Codigo="+ datos[0]
	cursor.execute(sql2)

def deleteCursos(cursor, codigo):
  borrar='DELETE FROM Cursos WHERE Codigo = %d' % (int(codigo))
  cursor.execute(borrar)
  borrar='DELETE FROM Inscripciones WHERE Codigo = %d' % (int(codigo))
  cursor.execute(borrar)
  cursor.connection.commit()

def viewCursos(cursor): #Lista de todos los cursos
  sql='SELECT * FROM Cursos'
  cursor.execute(sql)
  return cursor.fetchall()

#INSCRIPCIONES
def Inscribir(cursor, datos):#UNIQUE constraint failed: Inscripciones.Codigo, Inscripciones.DNI
  cursor.execute('INSERT INTO Inscripciones (Codigo, DNI, Nota) VALUES ( ?, ?, ?)',
              datos )
  cursor.connection.commit()

def inscriptos(cursor, dni, codigo):
  sql2='SELECT * FROM Inscripciones WHERE DNI='+dni
  cursor.execute(sql2)
  return cursor.fetchone()

def CursosIn(cursor, codigo):
   sql='SELECT * FROM Inscripciones WHERE Codigo='+codigo
   cursor.execute(sql)
   return cursor.fetchone()

def deleteIn(cursor, dni, codigo):#DELETE FROM Inscripciones WHERE DNI = 'dni' AND Codigo = 'codigo'
	borrar='DELETE FROM Inscripciones WHERE DNI= %d AND Codigo= %d' % (int(dni), int(codigo)) 
	cursor.execute(borrar)
  	cursor.connection.commit()

def verInscripciones(cursor, codigo):#cursor.execute("SELECT %s FROM Inscripciones WHERE dni=?" % (Codigo), (dni,))
  sql2='SELECT * FROM Inscripciones Where Codigo='+codigo
  cursor.execute(sql2)
  return cursor.fetchall()

def getInscp(cursor, dni):
  sql='SELECT * FROM Inscripciones WHERE DNI=%s' %(dni)
  cursor.execute(sql)
  return cursor.fetchone()