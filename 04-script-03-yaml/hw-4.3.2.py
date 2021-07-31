#!/usr/bin/env python3

import socket
import yaml
import json

hosts_list = [{'host':'drive.google.com','old_ip':'142.250.150.194','new_ip':''},
           {'host':'mail.google.com','old_ip':'142.250.150.83','new_ip':''},
           {'host':'google.com','old_ip':'64.233.165.138','new_ip':''}]
errors_list = []
to_file = []
print('Scan result')
for index, hosts_item in enumerate(hosts_list):
    result = socket.gethostbyname(hosts_item['host'])
    hosts_list[index]['new_ip'] = result
    print(f"http://{hosts_item['host']} - {result}")

    # Форматируем ответ для выгрузки в файл
    to_file.append({hosts_item['host']:result})

    if hosts_list[index]['new_ip'] != hosts_list[index]['old_ip']:
        errors_list.append(f"[ERROR] http://{hosts_item['host']} IP mismatch: {hosts_list[index]['old_ip']} {hosts_list[index]['new_ip']}")

for errors_item in errors_list:
    print(errors_item)
#Сохраняем в yaml
with open('hosts_check.yml', 'w') as result_yaml:
    result_yaml.write(yaml.dump(to_file))
#Сохраняем в json
with open('hosts_check.json', 'w') as result_json:
    result_json.write(json.dumps(to_file))