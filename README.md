🚀 Proyecto de Automatización – Generador Inteligente de Routing
📌 Descripción

Este proyecto automatiza la generación de configuraciones básicas de routing para routers Cisco utilizando Python.

El sistema:

✅ Valida redes en formato CIDR

✅ Calcula automáticamente la máscara wildcard

✅ Detecta automáticamente el área OSPF según el tipo de red

✅ Genera configuración dinámica para OSPF o EIGRP

✅ Integra configuración básica del router desde un archivo .txt

✅ Utiliza control de versiones con Git y GitHub

🚀 Tecnologías utilizadas

Python 3.13

Pytest

Git

GitHub

Librería ipaddress

🧠 ¿Qué hace el programa?

El usuario ingresa:

Protocolo (OSPF o EIGRP)

Red en formato CIDR (ej. 192.168.1.0/24)

El programa automáticamente:

Calcula la red

Calcula la máscara wildcard

Detecta el área OSPF (si aplica)

Genera la configuración de routing

Combina la configuración básica del router desde un archivo externo

📂 Estructura del proyecto
