# Домашнее задание к занятию "3.7. Компьютерные сети, лекция 2"

1. Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?
```bash
# ip
vagrant@vagrant:~$ ip -br l
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP> 
eth0             UP             08:00:27:e3:90:c5 <BROADCAST,MULTICAST,UP,LOWER_UP> 
eth1             UP             08:00:27:05:21:c6 <BROADCAST,MULTICAST,UP,LOWER_UP> 

# или
vagrant@vagrant:~$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::a00:27ff:fee3:90c5  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:e3:90:c5  txqueuelen 1000  (Ethernet)
        RX packets 30622  bytes 24223477 (24.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 17308  bytes 1597322 (1.5 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.107  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::a00:27ff:fe05:21c6  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:05:21:c6  txqueuelen 1000  (Ethernet)
        RX packets 4603  bytes 748104 (748.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 329  bytes 35802 (35.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 762  bytes 71552 (71.5 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 762  bytes 71552 (71.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

# в windows можно использовать ipconfig
```
2. Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?
```bash 
# протокол LLDP
# пакет для определения соседа lldpd
# команда lldpctl
```

3. Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? Какой пакет и команды есть в Linux для этого? Приведите пример конфига.
```bash
# технология VLAN
# пакет vlan
# проверяем текущие интерфейсы
vagrant@vagrant:~$ ip -br -c l
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP> 
eth0             UP             08:00:27:e3:90:c5 <BROADCAST,MULTICAST,UP,LOWER_UP> 
eth1             UP             08:00:27:05:21:c6 <BROADCAST,MULTICAST,UP,LOWER_UP> 

# поднимаем VLAN на интерфейсе eth1
vagrant@vagrant:~$ vi /etc/network/interfaces
    # interfaces(5) file used by ifup(8) and ifdown(8)
    # Include files from /etc/network/interfaces.d:
    source-directory /etc/network/interfaces.d
    auto vlan1400
    iface vlan1400 inet static
            address 192.168.2.1
            netmask 255.255.255.0
            vlan_raw_device eth1
# перезапускаем интерфейсы
sudo service networking restart
# проверяем результат
vagrant@vagrant:~$ ip -br -c l
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP> 
eth0             UP             08:00:27:e3:90:c5 <BROADCAST,MULTICAST,UP,LOWER_UP> 
eth1             UP             08:00:27:05:21:c6 <BROADCAST,MULTICAST,UP,LOWER_UP> 
vlan1400@eth1    UP             08:00:27:05:21:c6 <BROADCAST,MULTICAST,UP,LOWER_UP> 
# видим VLAN vlan1400@eth1 на eht1
```

4. Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.
```bash 
# в Linux используется агрегация портов (LAG)
# Объединенные интерфейсы могут работать в режиме горячего резерва (отказоустойчивости) или в режиме балансировки нагрузки.
# Виды балансировки нагрузки:
balance-rr    
balance-xor
balance-tlb
balance-alb

# Пример: конфига
 /etc/network/interfaces 
 
auto bond0

iface bond0 inet static
    address 10.31.1.5
    netmask 255.255.255.0
    network 10.31.1.0
    gateway 10.31.1.254
    slaves eth0 eth1

```

5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.
```bash
1. С маской /29 можно получить 6 адресов.
2. Можно получить 32 подсети (используем ipcalc 10.10.10.0/24 /29)
3. Примеры подсетей ниже
roman@Laptop-15-ec1xxx:~$ ipcalc 10.10.10.0/24 /29
Address:   10.10.10.0           00001010.00001010.00001010. 00000000
Netmask:   255.255.255.0 = 24   11111111.11111111.11111111. 00000000
Wildcard:  0.0.0.255            00000000.00000000.00000000. 11111111
=>
Network:   10.10.10.0/24        00001010.00001010.00001010. 00000000
HostMin:   10.10.10.1           00001010.00001010.00001010. 00000001
HostMax:   10.10.10.254         00001010.00001010.00001010. 11111110
Broadcast: 10.10.10.255         00001010.00001010.00001010. 11111111
Hosts/Net: 254                   Class A, Private Internet

Subnets after transition from /24 to /29

Netmask:   255.255.255.248 = 29 11111111.11111111.11111111.11111 000
Wildcard:  0.0.0.7              00000000.00000000.00000000.00000 111

 1.
Network:   10.10.10.0/29        00001010.00001010.00001010.00000 000
HostMin:   10.10.10.1           00001010.00001010.00001010.00000 001
HostMax:   10.10.10.6           00001010.00001010.00001010.00000 110
Broadcast: 10.10.10.7           00001010.00001010.00001010.00000 111
Hosts/Net: 6                     Class A, Private Internet

 2.
Network:   10.10.10.8/29        00001010.00001010.00001010.00001 000
HostMin:   10.10.10.9           00001010.00001010.00001010.00001 001
HostMax:   10.10.10.14          00001010.00001010.00001010.00001 110
Broadcast: 10.10.10.15          00001010.00001010.00001010.00001 111
Hosts/Net: 6                     Class A, Private Internet

 3.
Network:   10.10.10.16/29       00001010.00001010.00001010.00010 000
HostMin:   10.10.10.17          00001010.00001010.00001010.00010 001
HostMax:   10.10.10.22          00001010.00001010.00001010.00010 110
Broadcast: 10.10.10.23          00001010.00001010.00001010.00010 111
Hosts/Net: 6                     Class A, Private Internet



```

6. Задача: вас попросили организовать стык между 2-мя организациями. Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.
```bash 
# Можем использовать диапазон: 100.64.0.0 — 100.127.255.255 (маска подсети: 255.192.0.0 или /10)
# Используем диапазон подсеть /26
roman@Laptop-15-ec1xxx:~$ ipcalc 100.64.0.0/26
Address:   100.64.0.0           01100100.01000000.00000000.00 000000
Netmask:   255.255.255.192 = 26 11111111.11111111.11111111.11 000000
Wildcard:  0.0.0.63             00000000.00000000.00000000.00 111111
=>
Network:   100.64.0.0/26        01100100.01000000.00000000.00 000000
HostMin:   100.64.0.1           01100100.01000000.00000000.00 000001
HostMax:   100.64.0.62          01100100.01000000.00000000.00 111110
Broadcast: 100.64.0.63          01100100.01000000.00000000.00 111111
Hosts/Net: 62                    Class A

```

7. Как проверить ARP таблицу в Linux, Windows? Как очистить ARP кеш полностью? Как из ARP таблицы удалить только один нужный IP?
```bash
Отобразить ARP таблицу Linux и Windows: arp -a
Очистить всю таблицу: ip neigh flush all (в Windows netsh interface ip delete arpcache)
Удалить один сегмент: arp -d *IP* (в Windows аналогично)
```


 ---
## Задание для самостоятельной отработки (необязательно к выполнению)

 8*. Установите эмулятор EVE-ng.
 
 Инструкция по установке - https://github.com/svmyasnikov/eve-ng

 Выполните задания на lldp, vlan, bonding в эмуляторе EVE-ng. 
 
 ---

### Как оформить ДЗ?

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Также вы можете выполнить задание в [Google Docs](https://docs.google.com/document/u/0/?tgif=d) и отправить в личном кабинете на проверку ссылку на ваш документ.
Название файла Google Docs должно содержать номер лекции и фамилию студента. Пример названия: "3.7. Компьютерные сети, лекция 2 — Сусанна Алиева"
Перед тем как выслать ссылку, убедитесь, что ее содержимое не является приватным (открыто на комментирование всем, у кого есть ссылка). 
Если необходимо прикрепить дополнительные ссылки, просто добавьте их в свой Google Docs.

Любые вопросы по решению задач задавайте в чате Slack.

---
