# LinuxMacChanger

-----------------------------------------------------------
AUTOR:
-----------------------------------------------------------
Nombre: Hector Arango
Github: https://github.com/hmam13
Versión: 1.0

-----------------------------------------------------------
DESCRIPCION:
-----------------------------------------------------------
LinuxMacChanger es una herramienta sencilla y eficaz escrita en Python para cambiar la dirección MAC de las interfaces de red en sistemas operativos Linux directamente desde la terminal.

-----------------------------------------------------------
REQUISITOS:
-----------------------------------------------------------
* Python 3.x
* Permisos de superusuario (root/sudo).
* Herramientas de red tradicionales (`ifconfig`).

-----------------------------------------------------------
INSTALACION:
-----------------------------------------------------------
Descarga o clona el script.

-----------------------------------------------------------
MODO DE USO:
-----------------------------------------------------------
El script requiere dos argumentos obligatorios: la interfaz de red y la nueva dirección MAC.

-----------------------------------------------------------
SINTAXIS:
-----------------------------------------------------------
python3 LinuxMacChanger.py -i (interfaz) -m (nueva_mac)

-----------------------------------------------------------
ARGUMENTOS:
-----------------------------------------------------------
* `-i, --interface`: Nombre de la interfaz de red (ej. eth0, ens33, wlan0).
* `-m, --mac`: La nueva dirección MAC que deseas asignar (ej. 00:11:22:33:44:55).

-----------------------------------------------------------
EJEMPLO DE USO:
-----------------------------------------------------------
sudo python3 LinuxMacChanger.py -i eth0 -m 00:aa:bb:cc:dd:ee

-----------------------------------------------------------
Notas de Seguridad y Validación:
-----------------------------------------------------------
* El script valida que el formato de la dirección MAC sea correcto (XX:XX:XX:XX:XX:XX).
* Valida nombres de interfaz comunes en distribuciones Linux modernas (nombres predecibles como ethX o ensX).
* Requiere privilegios de root para poder bajar la interfaz, aplicar los cambios y volver a subirla.

---
**Disclaimer:** Esta herramienta es para fines educativos y de administración de sistemas. Asegúrate de tener permiso antes de cambiar direcciones MAC en redes que no te pertenecen.
