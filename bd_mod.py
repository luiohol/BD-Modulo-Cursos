import sqlite3

def getCursor(filename):
  connection = sqlite3.connect(filename)
  return connection.cursor()

def close(cursor):
  cursor.connection.close()

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
