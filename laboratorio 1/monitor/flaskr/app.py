from flaskr import create_app
from .modelos import db, Reporte
import subprocess
import setproctitle
import time
from datetime import datetime

setproctitle.setproctitle('monitorDB')

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

#MONITOR
while (True):
    with app.app_context():
        f = open('reporte.txt','a+')
        #COMANDOS
        #COMANDOS PING - ECHO
        comandosNMAP = subprocess.getoutput(["nmap -p 5000 127.0.0.1 | grep open"])
        if comandosNMAP:
            print(comandosNMAP)
            descripcionComNMAP = "Microservicio comandos (nmap) " + str(comandosNMAP)
            f.write(descripcionComNMAP + " "+ str(datetime.today())+'\n')
            rc = Reporte(evento='1', descripcion = descripcionComNMAP, fecha=datetime.today())
            db.session.add(rc)
        else:
            descripcionComNMAP = "PROCESO INACTICO. MICROSERVICIO COMANDOS (NMAP)"
            print(descripcionComNMAP)
            f.write(descripcionComNMAP + " " + str(datetime.today())+'\n')
            rc = Reporte(evento='2', descripcion = descripcionComNMAP, fecha=datetime.today())
            db.session.add(rc)

        #COMANDOS KEEP A LIVE
        comandosPS = subprocess.getoutput(["ps -e | grep comandos"])
        if comandosPS:
            print(comandosPS)
            descripcionComPS =  "Microservicio comandos (ps) " + str(comandosNMAP)
            f.write(descripcionComPS +" " + str(datetime.today())+'\n')
            rc = Reporte(evento='3', descripcion = descripcionComPS, fecha=datetime.today())
            db.session.add(rc)
        else:
            descripcionComPS = "PROCESO INACTICO. MICROSERVICIO COMANDOS (PS)"
            print(descripcionComPS)
            f.write(descripcionComPS + " " + str(datetime.today())+'\n')
            rc = Reporte(evento='4', descripcion = descripcionComPS, fecha=datetime.today())
            db.session.add(rc)

        #CONSULTAS
        #CONSULTAS PING - ECHO
        consultasNMAP = subprocess.getoutput(["nmap -p 5001 127.0.0.1 | grep open"])
        if consultasNMAP:
            print(consultasNMAP)
            descripcionConNMAP = "Microservicio consultas (nmap) " + str(consultasNMAP)
            f.write(descripcionConNMAP + " "+ str(datetime.today())+'\n')
            rc = Reporte(evento='5', descripcion = descripcionConNMAP, fecha=datetime.today())
            db.session.add(rc)
        else:
            descripcionConNMAP = "PROCESO INACTICO. MICROSERVICIO CONSULTAS (NMAP)"
            print(descripcionConNMAP)
            f.write(descripcionConNMAP + " " + str(datetime.today())+'\n')
            rc = Reporte(evento='6', descripcion = descripcionConNMAP, fecha=datetime.today())
            db.session.add(rc)

        #CONSULTAS KEEP A LIVE
        consultasPS = subprocess.getoutput(["ps -e | grep consultas"])
        if consultasPS:
            print(consultasPS)
            descripcionConPS =  "Microservicio consultas (ps) " + str(consultasPS)
            f.write(descripcionConPS +" " + str(datetime.today())+'\n')
            rc = Reporte(evento='7', descripcion = descripcionConPS, fecha=datetime.today())
            db.session.add(rc)
        else:
            descripcionConPS = "PROCESO INACTICO. MICROSERVICIO CONSULTAS (PS)"
            print(descripcionConPS)
            f.write(descripcionConPS + " " + str(datetime.today())+'\n')
            rc = Reporte(evento='8', descripcion = descripcionConPS, fecha=datetime.today())
            db.session.add(rc)

        f.close()
        db.session.commit()
        time.sleep(10)



