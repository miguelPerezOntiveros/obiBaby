#!/usr/bin/python
import grovepi
import MySQLdb
import time
import os

#Subprocess, es para correr comandos
import subprocess
#Es una función obtenida de esta liga 
#http://stackoverflow.com/questions/4760215/running-shell-command-from-python-and-capturing-the-output
#Obtiene lo que devuelve el comando.
def runProcess(exe):    
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
      retcode = p.poll() 
      line = p.stdout.readline()
      yield line
      if(retcode is not None):
        break

db = MySQLdb.connect(host="10.49.130.37",
                     user="cedittec",
                      passwd="server",
                      db="obiBaby")

sensorth = 4
gas_sensor = 1
grovepi.pinMode(gas_sensor,"INPUT")
air_sensor = 0
grovepi.pinMode(air_sensor,"INPUT")
pir_sensor = 3
grovepi.pinMode(pir_sensor,"INPUT")

cur = db.cursor()

while True:
    try:
	fecha = time.strftime('%Y-%m-%d %H:%M:%S')
	print "Leyendo Temperatura y humedad"
        [temp,humidity] = grovepi.dht(sensorth,0)
	print "temp =", temp, " humidity =", humidity
	cur.execute("INSERT INTO log_user_temperature (temperature, humidity, created_at) VALUES ('%s', '%s', %s)", (temp, humidity, fecha))
	db.commit()
	print "Temperatura y Humedad Actualizado en la BD"
	print "Leyendo sensor de Gas"
	sensor_value = grovepi.analogRead(gas_sensor)
	print "sensor_value =", sensor_value
	cur.execute("INSERT INTO log_user_gas (co, created_at) VALUES ('%s', %s)", (sensor_value, fecha))
	db.commit()
	print "Sensor de Gas Actualizado en la BD"
	print "Leyendo sensor de Aire"
	sensor_valueAir = grovepi.analogRead(air_sensor)

	#el campo pollution es enum (1-'low', 2-'medium', 3='high')
        if sensor_valueAir > 700:
            air = 3
        elif sensor_valueAir > 300:
            air = 2
        else:
            air = 1

        print "sensor_valueAir =", sensor_valueAir, " Aire =", air
	cur.execute("INSERT INTO log_user_air (value, pollution, created_at) VALUES ('%s', '%s', %s)", (sensor_valueAir, air, fecha))
	db.commit()
	print "Sensor de Aire Actualizado en la BD"
	print "Leyendo sensor de Movimiento"
	if grovepi.digitalRead(pir_sensor):		
	    	cur.execute("INSERT INTO log_user_motion (time, created_at) VALUES (%s, %s)", (fecha, fecha))
		db.commit()
		print "Sensor de Movimiento Actualizado en la BD"
        else:
            print "No hubo movimiento"


	print "--------------------------------------------------"
	

	####################################################################################################
	#Parte en la que se realiza la configuración de la Raspberry sí solo sí está conectada por Ethernet.
	
	#Se revisa si está conectado vía Ethernet...
	for line in runProcess('ifconfig eth0 | grep inet'.split()):
	#Acá se realizaría la configuración...
		print "Estoy conectado via Ethernet, y soy bien chido. Aca me configuro, ¡Ese!"
		break

	time.sleep( 2 )

    except IOError:
        print "Error"
