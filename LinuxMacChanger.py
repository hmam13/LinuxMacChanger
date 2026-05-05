#!/usr/bin/env python3

"""
Nombre del Script: LinuxMacChanger
Autor: Hector Arango 
Github: https://github.com/hmam13
Descripción: Herramienta para cambiar la dirección MAC de las interfaces de red en Linux por terminal.
Lenguaje: Python
Version: 1.0
"""

# ──────────────────────────────────────────────
#  Librerías
# ──────────────────────────────────────────────
import argparse
import subprocess
import re
import os

# ──────────────────────────────────────────────
#  Configuración de Colores de Terminal
# ──────────────────────────────────────────────
ROJO = "\033[1;31m"
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
AZUL = "\033[1;34m"
FIN = "\033[0m"

# ──────────────────────────────────────────────
#  Funciones Lógicas
# ──────────────────────────────────────────────
def help_panel():

    parser = argparse.ArgumentParser(description='MACChanger')
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Nombre de la interfaz de red")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help="Nueva dirección MAC")
    return parser.parse_args()

def is_valid_input(interface, mac_address):

    is_valid_interface = re.match(r'^[e][n|t][s|h]\d{1,2}$', interface) #Interpretación para nombres tipo "Predictable Network Interface"
    is_valid_mac = re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address) #Interpretación para dirección "MAC". 
    return is_valid_interface and is_valid_mac

def change_mac(interface, mac_address):

    if os.geteuid() != 0: #Comprobamos si el usuario no es root
        print(f"\n{AMARILLO}[!] Se necesitan permisos de root...{FIN}")
        print(f"\nBy: hmam")
    elif is_valid_input(interface, mac_address):
        subprocess.run(["sudo", "ifconfig", interface, "down"])
        subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
        subprocess.run(["sudo", "ifconfig", interface, "up"])
        print(f"\n{VERDE}[+] La MAC ha sido cambiada exitosamente{FIN}")
        print(f"\nBy: hmam")
    else:
        print(f"\n{ROJO}[x] Los datos introducidos no son correctos{FIN}")
        print(f"\nBy: hmam")

def main():

    args = help_panel()
    change_mac(args.interface, args.mac_address)

if __name__ == '__main__':
    main()