import socket
import sys
from datetime import datetime

PUERTOS_COMUNES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
}

def escanear_puerto(ip, puerto):
    """Intenta conectar a un puerto específico."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    resultado = sock.connect_ex((ip, puerto))
    sock.close()
    return resultado == 0

def escanear_rango(ip, puerto_inicio, puerto_fin):
    print(f"\nEscaneando {ip} desde el puerto {puerto_inicio} hasta {puerto_fin}")
    print(f"Inicio: {datetime.now()}\n")

    puertos_abiertos = []

    for puerto in range(puerto_inicio, puerto_fin + 1):
        if escanear_puerto(ip, puerto):
            servicio = PUERTOS_COMUNES.get(puerto, "Desconocido")
            print(f"[+] Puerto {puerto} ABIERTO ({servicio})")
            puertos_abiertos.append(puerto)

    print(f"\nEscaneo finalizado: {datetime.now()}")
    print(f"Total de puertos abiertos: {len(puertos_abiertos)}")
    return puertos_abiertos

if __name__ == "__main__":
    objetivo = input("Introduce la IP o dominio a escanear: ")
    inicio = int(input("Puerto inicial: "))
    fin = int(input("Puerto final: "))

    try:
        ip = socket.gethostbyname(objetivo)
        escanear_rango(ip, inicio, fin)
    except socket.gaierror:
        print("Error: no se pudo resolver el nombre del host.")
        sys.exit(1)