from ncclient import manager

# Datos de conexión del CSR1000v
router = {
    "host": "192.168.56.101",  # Cambia por la IP real de tu CSR1000v
    "port": 830,
    "username": "cisco",    # Cambia si usas otros datos
    "password": "cisco123!",
    "hostkey_verify": False
}

# Configuración para cambiar el hostname
config_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Arancibia-Ruminot</hostname>
  </native>
</config>
"""

# Configuración para crear la Loopback11
config_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

# Conexión y configuración
with manager.connect(**router) as m:
    # Cambiar hostname
    print("🔹 Cambiando hostname...")
    m.edit_config(target="running", config=config_hostname)
    
    # Crear loopback
    print("🔹 Creando Loopback11...")
    m.edit_config(target="running", config=config_loopback)

print("✅ Configuración completada.")
