import ipaddress


def calcular_wildcard(mascara):
    wildcard = []
    partes = mascara.split(".")
    for parte in partes:
        wildcard.append(str(255 - int(parte)))
    return ".".join(wildcard)


def detectar_area(red):
    if red.is_private:
        if str(red.network_address).startswith("192.168"):
            return 1
        elif str(red.network_address).startswith("10."):
            return 2
        elif str(red.network_address).startswith("172."):
            return 3
    return 0


def leer_config_basica(archivo):
    datos = {}
    with open(archivo, "r") as f:
        for linea in f:
            clave, valor = linea.strip().split("=")
            datos[clave] = valor
    return datos


def generar_config_basica(datos):
    configuracion = f"""
hostname {datos['hostname']}

interface {datos['interfaz']}
 ip address {datos['ip']} {datos['mascara']}
 no shutdown
 description Conexion LAN
"""
    return configuracion


def generar_ospf(red_cidr):
    red = ipaddress.ip_network(red_cidr, strict=False)
    direccion_red = red.network_address
    mascara = red.netmask
    wildcard = calcular_wildcard(str(mascara))
    area = detectar_area(red)

    configuracion = f"""
router ospf 1
 network {direccion_red} {wildcard} area {area}
"""
    return configuracion


def generar_eigrp(red_cidr, asn):
    red = ipaddress.ip_network(red_cidr, strict=False)
    direccion_red = red.network_address
    mascara = red.netmask
    wildcard = calcular_wildcard(str(mascara))

    configuracion = f"""
router eigrp {asn}
 network {direccion_red} {wildcard}
 no auto-summary
"""
    return configuracion


def main():
    print("=== GENERADOR AUTOMÁTICO DESDE ARCHIVO ===")

    datos_router = leer_config_basica("router_config.txt")

    print("\n--- CONFIGURACIÓN BÁSICA ---")
    print(generar_config_basica(datos_router))

    protocolo = input("\nElige protocolo (ospf/eigrp): ").lower()
    red_cidr = input("Ingresa la red en formato CIDR (ej. 192.168.1.0/24): ")

    try:
        if protocolo == "ospf":
            print("\n--- CONFIGURACIÓN OSPF ---")
            print(generar_ospf(red_cidr))

        elif protocolo == "eigrp":
            asn = input("Ingresa el número de AS (ej. 100): ")
            print("\n--- CONFIGURACIÓN EIGRP ---")
            print(generar_eigrp(red_cidr, asn))

        else:
            print("Protocolo no válido")

    except ValueError:
        print("Red no válida")


if __name__ == "__main__":
    main()