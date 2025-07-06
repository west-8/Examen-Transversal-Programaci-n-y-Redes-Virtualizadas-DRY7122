from netmiko import ConnectHandler

# Configura los datos de conexión
router = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
}

# Conectar al router
print("Conectando al router...")
conexion = ConnectHandler(**router)

# Comandos de configuración para EIGRP nombrado (IPv4)
configuracion = [
    "router eigrp SDN",
    "address-family ipv4 unicast autonomous-system 100",
    "network 192.168.0.0 0.0.255.255",
    "af-interface GigabitEthernet1",
    "passive-interface",
    "exit-af-interface",
    "exit-address-family",
]

print("\n🛠 Aplicando configuración EIGRP...")
salida_config = conexion.send_config_set(configuracion)
print(salida_config)

# Comandos de show
print("\n📄 show running-config | section eigrp")
print(conexion.send_command("show run | section eigrp"))

print("\n📄 show ip interface brief")
print(conexion.send_command("show ip interface brief"))

print("\n📄 show version")
print(conexion.send_command("show version"))

# Cerrar la conexión
conexion.disconnect()
print("\n✅ Conexión cerrada.")
