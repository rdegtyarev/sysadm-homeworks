# Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"

## Обязательные задания

1. Мы выгрузили JSON, который получили через API запрос к нашему сервису:
	```json
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            },
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
	```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

```json
{ "info" : "Sample JSON output from our service\t", 
  "elements" :[
    { "name" : "first", "type" : "server", "ip" : "192.168.0.1"}, 
    { "name" : "second", "type" : "proxy", "ip" : "71.78.22.43"}
  ]
}
```
Корректный файл json лежит рядом с READMY.md  

2. В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.  

```python
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
# Рабочий скрипт рядом с READMY.md
```

## Дополнительное задание (со звездочкой*) - необязательно к выполнению

Так как команды в нашей компании никак не могут прийти к единому мнению о том, какой формат разметки данных использовать: JSON или YAML, нам нужно реализовать парсер из одного формата в другой. Он должен уметь:
   * Принимать на вход имя файла
   * Проверять формат исходного файла. Если файл не json или yml - скрипт должен остановить свою работу
   * Распознавать какой формат данных в файле. Считается, что файлы *.json и *.yml могут быть перепутаны
   * Перекодировать данные из исходного формата во второй доступный (из JSON в YAML, из YAML в JSON)
   * При обнаружении ошибки в исходном файле - указать в стандартном выводе строку с ошибкой синтаксиса и её номер
   * Полученный файл должен иметь имя исходного файла, разница в наименовании обеспечивается разницей расширения файлов

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
