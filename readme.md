Guía Raspberry Pi
Descargar y montar raspbian en la memoria SD
https://www.raspberrypi.org/downloads/raspbian/
https://www.raspberrypi.org/documentation/installation/installing-images/mac.md

Comando raspi-config
Asignar contraseña a la raspberry (‘obitec15.0’)
Habilitar la cámara

Comando sudo apt-get update

Instalar MySql
sudo apt-get install python-mysqldb

Clonar carpeta git para tener nuestro código
	git clone https://github.com/miguelPerezOntiveros/obiBaby.git

http://www.dexterindustries.com/GrovePi/get-started-with-the-grovepi/setting-software/

Instalar el GrovePi
	Reiniciar la Raspberry sin el Grove Pi
	Descargar archivos de GrovePi
		git clone https://github.com/DexterInd/GrovePi
	Ir al folder Script de la carpeta de GrovePi
		cd GrovePi/Script
	sudo chmod +x install.sh
	sudo ./install.sh
	
	La raspberry se reiniciará y se deberá colocar el GrovePi
	
Checar si se instaló correctamente (uno al final con las nuevas versiones de raspberry)
	sudo i2cdetect -y 1 
	Si se ve un “04” la instalación fue exitosa

Probar el GrovePi con los Sripts en Python de ejemplo
	cd GrovePi/Software/Python

							


