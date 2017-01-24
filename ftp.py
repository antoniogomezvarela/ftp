# -*- coding: utf-8 -*-

import sys
import os

#Crear usuario
os.system('adduser user_%s' % (sys.argv[1]))

#Crear Carpeta
os.system('mkdir -p /var/www/html/%s' % (sys.argv[1]))

#Crear index
os.system('echo "Pagina de user_%s" > /var/www/html/%s/index.html' % (sys.argv[1],sys.argv[1]))

#Cambiar propietario y grupo
os.system('chown -R user_%s:nogroup /var/www/html/%s/' % (sys.argv[1],sys.argv[1]))

#Añadir DefaultRoot a proftpd.conf
os.system('echo "DefaultRoot	/var/www/html/%s user_%s" >> /etc/proftpd/proftpd.conf' % (sys.argv[1],sys.argv[1]))

#Reiniciar servicio
os.system('systemctl restart proftpd')