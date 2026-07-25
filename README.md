# Escáner de Puertos

Proyecto final para **Code in Place**. Escanea un rango de puertos TCP en una IP o dominio dado y muestra cuáles están abiertos, identificando el servicio común asociado (HTTP, FTP, SSH, etc.).

## ⚠️ Uso ético

Este proyecto es solo para fines educativos. Úsalo únicamente contra sistemas de tu propiedad o con autorización explícita — por ejemplo `localhost` o `scanme.nmap.org` (host público destinado a pruebas de escaneo).

**No lo uses contra sistemas de terceros sin permiso.**

## Cómo funciona

El script intenta abrir una conexión TCP a cada puerto dentro del rango indicado. Si la conexión se establece con éxito, el puerto se considera abierto. Además, compara el número de puerto contra una lista de puertos comunes para indicar qué servicio suele correr ahí.

## Requisitos

- Python 3.x
- No requiere librerías externas, solo módulos de la librería estándar (`socket`, `sys`, `datetime`)

## Cómo ejecutarlo

`python Scanner.py`

El programa te pedirá:
- **IP o dominio** a escanear
- **Puerto inicial**
- **Puerto final**

## Ejemplo de uso

```
Introduce la IP o dominio a escanear: scanme.nmap.org
Puerto inicial: 20
Puerto final: 100

Escaneando 45.33.32.156 desde el puerto 20 hasta 100
Inicio: 2026-07-24 10:00:00

[+] Puerto 22 ABIERTO (SSH)
[+] Puerto 80 ABIERTO (HTTP)

Escaneo finalizado: 2026-07-24 10:00:03
Total de puertos abiertos: 2
```

## Estructura del proyecto

```
scanner-de-puertos/
├── Scanner.py
└── README.md
```

## Posibles mejoras futuras

- Escaneo multihilo para acelerar el proceso en rangos grandes
- Exportar resultados a un archivo (CSV o TXT)
- Interfaz gráfica simple
- Agregar una barra de carga

## Autor

Proyecto desarrollado como parte del curso **Code in Place**.
