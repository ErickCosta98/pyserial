import serial
#importar conexion
from conexion import miConexion
ser = serial.Serial('COM8', 9600)

while True:
    value = ser.readline().decode().strip().split(';')
    insert = "INSERT INTO data (DATO1,DATO2) VALUES (%s,%s)"
    try:
        miConexion.cursor().execute(insert, value)
        miConexion.commit()
    except:
        print("Error al insertar los datos")
    print(value)