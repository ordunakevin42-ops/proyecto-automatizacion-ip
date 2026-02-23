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
    return 0  # Backbone para redes públicas


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
    print("=== GENERADOR INTELIGENTE DE ROUTING ===")
    protocolo = input("Elige protocolo (ospf/eigrp): ").lower()
    red_cidr = input("Ingresa la red en formato CIDR (ej. 192.168.1.0/24): ")

    try:
        if protocolo == "ospf":
            print("\nConfiguración OSPF generada automáticamente:")
            print(generar_ospf(red_cidr))

        elif protocolo == "eigrp":
            asn = input("Ingresa el número de AS (ej. 100): ")
            print("\nConfiguración EIGRP generada automáticamente:")
            print(generar_eigrp(red_cidr, asn))

        else:
            print("Protocolo no válido")

    except ValueError:
        print("Red no válida. Usa formato correcto, ejemplo: 192.168.1.0/24")


if __name__ == "__main__":
    main()