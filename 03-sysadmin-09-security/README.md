Домашнее задание к занятию "3.9. Элементы безопасности информационных систем"

1. Установите Bitwarden плагин для браузера. Зарегестрируйтесь и сохраните несколько паролей.
Выполнено
2. Установите Google authenticator на мобильный телефон. Настройте вход в Bitwarden акаунт через Google authenticator OTP.
Выполнено
3. Установите apache2, сгенерируйте самоподписанный сертификат, настройте тестовый сайт для работы по HTTPS.
```bash
vagrant@vagrant:~$ sudo apt-get install apache2
vagrant@vagrant:~$ sudo a2enmod ssl
vagrant@vagrant:~$ systemctl restart apache2

vagrant@vagrant:~$ sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout /etc/ssl/private/apache-selfsigned.key \
-out /etc/ssl/certs/apache-selfsigned.crt \
-subj "/C=RU/ST=Moscow/L=Moscow/O=Company Name/OU=Org/CN=www.example.com"
vagrant@vagrant:~$ sudo mcedit /etc/apache2/sites-available/192.168.0.107.conf

<VirtualHost *:443>  
   ServerName 192.168.0.107  
   DocumentRoot /var/www/192.168.0.107  
   SSLEngine on  
   SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt  
   SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key  
</VirtualHost>  

vagrant@vagrant:~$ sudo mkdir /var/www/192.168.0.107
vagrant@vagrant:~$ sudo mcedit /var/www/192.168.0.107/index.html

<h1>This is test page</h1>
<p>Homework 3.9<p>

vagrant@vagrant:/etc/apache2/sites-available$ sudo a2ensite 192.168.0.107.conf
Enabling site 192.168.0.107.
To activate the new configuration, you need to run:
  systemctl reload apache2
vagrant@vagrant:/etc/apache2/sites-available$ systemctl reload apache2
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to reload 'apache2.service'.
Authenticating as: vagrant,,, (vagrant)
Password: 
==== AUTHENTICATION COMPLETE ===

```
4. Проверьте на TLS уязвимости произвольный сайт в интернете.
```bash
vagrant@vagrant:~$ git clone --depth 1 https://github.com/drwetter/testssl.sh.gitcd testssl.sh
vagrant@vagrant:~$  ./testssl.sh -e --fast --parallel https://localhost #из предыдущего примера
vagrant@vagrant:~$ ./testssl.sh -U --sneaky https://localhost #из предыдущего примера
```
5. Установите на Ubuntu ssh сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.
```bash
# сервер (в vagrant ubuntu ssh уже установлен, команды вернули ответ что все ок). Адрес хоста 192.168.0.107
vagrant@vagrant:~$ apt install openssh-server
vagrant@vagrant:~$ systemctl start sshd.service
vagrant@vagrant:~$ systemctl enable sshd.service

# клиент
roman@Laptop-15-ec1xxx: ssh-keygen
# копируем публичный ключ на сервер
roman@Laptop-15-ec1xxx: ssh-copy-id vagrant@192.168.0.107
# подключаемся
roman@Laptop-15-ec1xxx: ssh vagrant@192.168.0.107

```
6. Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH клиента, так чтобы вход на удаленный сервер осуществлялся по имени сервера.
```bash
roman@Laptop-15-ec1xxx:~/.ssh$ touch config
roman@Laptop-15-ec1xxx:~/.ssh$ vim config 
##
Host vagrant_server
  HostName 192.168.0.107
  IdentityFile ~/.ssh/vagrant_server.key
  User vagrant
##

roman@Laptop-15-ec1xxx:~/.ssh$ mv id_rsa vagrant_server
roman@Laptop-15-ec1xxx:~/.ssh$ ssh vagrant_server
# подключение успешно
```
7. Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.
```bash
user@ubuntu-desktop:~$ sudo apt install tcpdump
Reading package lists... Done
Building dependency tree       
Reading state information... Done
tcpdump is already the newest version (4.9.3-4).
0 upgraded, 0 newly installed, 0 to remove and 54 not upgraded.

user@ubuntu-desktop:~$ tcpdump -D
1.enp0s3 [Up, Running]
2.lo [Up, Running, Loopback]
3.any (Pseudo-device that captures on all interfaces) [Up, Running]
4.bluetooth-monitor (Bluetooth Linux Monitor) [none]
5.nflog (Linux netfilter log (NFLOG) interface) [none]
6.nfqueue (Linux netfilter queue (NFQUEUE) interface) [none]

user@ubuntu-desktop:~$ sudo tcpdump -i enp0s3 -w dump.pcap -c 100
tcpdump: listening on enp0s3, link-type EN10MB (Ethernet), capture size 262144 bytes
100 packets captured
230 packets received by filter
0 packets dropped by kernel

#файл dump.pcap успешно открыл в Wireshark

```