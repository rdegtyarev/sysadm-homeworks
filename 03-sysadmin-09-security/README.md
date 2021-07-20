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

5. Установите на Ubuntu ssh сервер, сгенерируйте новый приватный ключ. Скопируйте свой публичный ключ на другой сервер. Подключитесь к серверу по SSH-ключу.

6. Переименуйте файлы ключей из задания 5. Настройте файл конфигурации SSH клиента, так чтобы вход на удаленный сервер осуществлялся по имени сервера.

7. Соберите дамп трафика утилитой tcpdump в формате pcap, 100 пакетов. Откройте файл pcap в Wireshark.
