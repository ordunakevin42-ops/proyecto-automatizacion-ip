from programa import validar_ip

def test_ip_valida():
    assert validar_ip("192.168.1.1") == True

def test_ip_invalida_formato():
    assert validar_ip("192.168.1") == False

def test_ip_invalida_rango():
    assert validar_ip("999.168.1.1") == False