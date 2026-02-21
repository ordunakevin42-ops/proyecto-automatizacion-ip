def validar_ip(ip):
    partes = ip.split(".")
    
    if len(partes) != 4:
        return False
    
    for parte in partes:
        if not parte.isdigit():
            return False
        if int(parte) < 0 or int(parte) > 255:
            return False
    
    return True


if __name__ == "__main__":
    ip = input("Ingresa una dirección IP: ")
    
    if validar_ip(ip):
        print("IP válida ✅")
    else:
        print("IP inválida ❌")