#!/env/bin/python3
import pyperclip
from netmiko import ConnectHandler
import json
nx_os={
	
	'device_type':'cisco_ios',
	'host':'sbx-nxos-mgmt.cisco.com',
	'username':'admin',
	'password':'Admin_1234!',
	'port':8181

}

net_connect=ConnectHandler(**nx_os)



output=net_connect.send_command('sh ip int br | json-pretty')
convert=json.loads(output)
print(output)
#Number of Interfaces Available
int_number=len(convert['TABLE_intf']['ROW_intf'])

#Iterate all the interfaces to print interface name and IP address
for i in range (int_number):
	print('Interface Name')
	print(convert['TABLE_intf']['ROW_intf'][i]['intf-name'])
	print('IP Address')
	print(convert['TABLE_intf']['ROW_intf'][i]['prefix'])
	print('Protocol State')	
	print(convert['TABLE_intf']['ROW_intf'][i]['proto-state'])	
	print(''.center(50,'*'))

output1=net_connect.send_command('sh users')
output2=net_connect.send_command('sh vlan br')
print(output1)
print(output2)

