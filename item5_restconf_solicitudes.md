interface Loopback11
 ip address 11.11.11.11 255.255.255.255

interface GigabitEthernet1
 ip address dhcp

DELETE https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback11
Headers:
  Accept: application/yang-data+json
  Content-Type: application/yang-data+json

PUT https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback22
Headers:
  Accept: application/yang-data+json
  Content-Type: application/yang-data+json
Body (JSON):
{
  "ietf-interfaces:interface": {
    "name": "Loopback22",
    "description": "Loopback 22",
    "type": "iana-if-type:softwareLoopback",
    "enabled": false,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "22.22.22.22",
          "netmask": "255.255.255.255"
        }
      ]
    }
  }
}


GET https://192.168.56.101/restconf/data/ietf-interfaces:interfaces
Headers:
  Accept: application/yang-data+json
