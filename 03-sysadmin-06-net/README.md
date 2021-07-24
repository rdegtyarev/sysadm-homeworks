# Домашнее задание к занятию "3.6. Компьютерные сети, лекция 1"

1. Работа c HTTP через телнет.
- Подключитесь утилитой телнет к сайту stackoverflow.com
`telnet stackoverflow.com 80`
- отправьте HTTP запрос
```bash
GET /questions HTTP/1.0
HOST: stackoverflow.com
[press enter]
[press enter]
```
- В ответе укажите полученный HTTP код, что он означает?
```bash
# получили ответ
HTTP/1.1 301 Moved Permanently
# это означает что запрошенный ресурс на постоянной основе был перенесен. Мы запрашиваем по HTTP (80 порт), страница редиректит на HTTPS (443).

```
2. Повторите задание 1 в браузере, используя консоль разработчика F12.
- откройте вкладку `Network`
- отправьте запрос http://stackoverflow.com
- найдите первый ответ HTTP сервера, откройте вкладку `Headers`
- укажите в ответе полученный HTTP код.
- проверьте время загрузки страницы, какой запрос обрабатывался дольше всего?
- приложите скриншот консоли браузера в ответ.

```bash
Status Code: 301 Moved Permanently
# Аналогично, редиректит на https
# Время загрузки 1.73s
# Самый длинный запрос вто, на который проходит редирект:
Request URL: https://stackoverflow.com/
Request Method: GET
Status Code: 200 
Remote Address: 151.101.193.69:443
Referrer Policy: strict-origin-when-cross-origin
# скрин рядом с README.md
```
3. Какой IP адрес у вас в интернете?
```bash
# Использую https://whoer.net/
77.105.157.2
```

4. Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой `whois`
```bash
# Используем whois
# получаем информацию о провайдере
vagrant@vagrant:~$ whois  77.105.157.2 | grep "org-name"
org-name:       Plus Telecom LLC

# получаем информацию о AS
vagrant@vagrant:~$ whois  77.105.157.2 | grep "origin"
origin:         AS42031

```   
5. Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой `traceroute`
```bash
vagrant@vagrant:~$ traceroute -An 8.8.8.8
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max, 60 byte packets
 1  10.0.2.2 [*]  0.409 ms  0.381 ms  0.367 ms
 2  192.168.0.1 [*]  9.145 ms  9.116 ms  9.101 ms
 3  77.105.176.1 [AS42031]  9.078 ms  13.328 ms  13.080 ms
 4  77.105.154.35 [AS42031]  13.044 ms  13.029 ms  12.938 ms
 5  77.105.144.33 [AS42031]  12.919 ms  12.874 ms  12.875 ms
 6  185.232.60.148 [*]  12.809 ms  10.974 ms  7.315 ms
 7  108.170.250.66 [AS15169]  7.144 ms 108.170.250.130 [AS15169]  6.546 ms 108.170.250.83 [AS15169]  9.937 ms
 8  142.251.49.78 [AS15169]  18.191 ms  22.261 ms *
 9  209.85.254.20 [AS15169]  22.232 ms 172.253.66.110 [AS15169]  22.219 ms 172.253.65.159 [AS15169]  22.198 ms
10  142.250.210.47 [AS15169]  22.116 ms 142.250.56.219 [AS15169]  22.073 ms 216.239.49.113 [AS15169]  22.048 ms
11  * * *
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * * *
20  8.8.8.8 [AS15169]  28.164 ms  35.056 ms *
# AS указаны в квадратных скобках
1
```   
6. Повторите задание 5 в утилите `mtr`. На каком участке наибольшая задержка - delay?
```bash
                                     My traceroute  [v0.93]
vagrant (10.0.2.15)                                                    2021-07-24T09:01:52+0000
Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                                       Packets               Pings
 Host                                                Loss%   Snt   Last   Avg  Best  Wrst StDev
 1. AS???    10.0.2.2                                 0.0%    10    0.5   0.5   0.2   0.8   0.2
 2. AS???    192.168.0.1                              0.0%    10    8.6   6.6   4.9   9.4   1.8
 3. AS42031  77.105.176.1                             0.0%    10    8.8  10.0   8.0  18.5   3.1
 4. AS42031  77.105.154.35                            0.0%    10    8.4   8.3   7.2   9.0   0.6
 5. AS42031  77.105.144.33                            0.0%    10   14.6   8.6   5.3  14.6   2.5
 6. AS???    185.232.60.148                           0.0%    10    8.4   7.6   3.0   9.8   2.2
 7. AS15169  108.170.250.34                           0.0%    10   13.9   9.5   8.2  13.9   1.7
 8. AS15169  172.253.66.116                           0.0%    10   59.8  34.4  21.8  59.8  16.3
 9. AS15169  172.253.65.159                           0.0%    10   26.3  33.2  22.1  58.9  16.1
10. AS15169  216.239.63.25                            0.0%    10   60.9  47.3  19.8 101.3  26.1
11. (waiting for reply)
12. (waiting for reply)
13. (waiting for reply)
14. (waiting for reply)
15. (waiting for reply)
16. (waiting for reply)
17. (waiting for reply)
18. (waiting for reply)
19. (waiting for reply)
20. AS15169  8.8.8.8                                  0.0%    10   22.3  49.3  21.5 106.8  39.9

# максимальная задержка на последнем сегменте
20. AS15169  8.8.8.8                                  0.0%    10   22.3  49.3  21.5 106.8  39.9

```   
7. Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой `dig`
```bash
# DNS сервера, отвечающие за доменное имя dns.google:
# используем  dig +trace dns.google

dns.google.             10800   IN      NS      ns4.zdns.google.
dns.google.             10800   IN      NS      ns2.zdns.google.
dns.google.             10800   IN      NS      ns3.zdns.google.
dns.google.             10800   IN      NS      ns1.zdns.google.

# A записи:
;; ANSWER SECTION:
dns.google.             837     IN      A       8.8.8.8
dns.google.             837     IN      A       8.8.4.4

```   
8. Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой `dig`
```bash
# используем dig -x 8.8.8.8
# используем dig -x 8.8.4.4

;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.   1188    IN      PTR     dns.google.

;; ANSWER SECTION:
4.4.8.8.in-addr.arpa.   6863    IN      PTR     dns.google.

```
В качестве ответов на вопросы можно приложите лог выполнения команд в консоли или скриншот полученных результатов.
```bash
# полный лог последних двух заданий
vagrant@vagrant:~$ dig +trace dns.google

; <<>> DiG 9.16.1-Ubuntu <<>> +trace dns.google
;; global options: +cmd
.                       6496    IN      NS      e.root-servers.net.
.                       6496    IN      NS      k.root-servers.net.
.                       6496    IN      NS      b.root-servers.net.
.                       6496    IN      NS      i.root-servers.net.
.                       6496    IN      NS      m.root-servers.net.
.                       6496    IN      NS      l.root-servers.net.
.                       6496    IN      NS      g.root-servers.net.
.                       6496    IN      NS      f.root-servers.net.
.                       6496    IN      NS      j.root-servers.net.
.                       6496    IN      NS      a.root-servers.net.
.                       6496    IN      NS      d.root-servers.net.
.                       6496    IN      NS      h.root-servers.net.
.                       6496    IN      NS      c.root-servers.net.
;; Received 262 bytes from 127.0.0.53#53(127.0.0.53) in 0 ms

google.                 172800  IN      NS      ns-tld1.charlestonroadregistry.com.
google.                 172800  IN      NS      ns-tld2.charlestonroadregistry.com.
google.                 172800  IN      NS      ns-tld3.charlestonroadregistry.com.
google.                 172800  IN      NS      ns-tld4.charlestonroadregistry.com.
google.                 172800  IN      NS      ns-tld5.charlestonroadregistry.com.
google.                 86400   IN      DS      6125 8 2 80F8B78D23107153578BAD3800E9543500474E5C30C29698B40A3DB2 3ED9DA9F
google.                 86400   IN      RRSIG   DS 8 1 86400 20210806050000 20210724040000 26838 . XCOFkmQSqtkCMbPWJY+fGdDOb79UVVuXGQ0J3ANRMz6SD7NoYH+AxiO2 YG5VmsczwaG+apk+vqAIz0uyXsnhGIta0lzWGI+RdNDfaf2Ij3F3kAii xGMmPnz1xnsDpMw5KphHNYpKs8ps0Fiqf8oPI6TUZxJE8DcmRLYr2EpZ rcpw8NyTO5KL+PIXHCAEkudR7Vc0sMxe6UBGtU8p0u1QaV0Q+n3Lgkbb askyHOd7xqRZ4/Yf9Tbe1e4xawvq0qBQ5L1L/AWdImukXbrNu/F+DD4Q Knz3J8wE2PB7SujR/r2WtFeaa69uwFTpSkKdp15Gw0ZzZyzmRrv17AYk Z0s1Xw==
;; Received 730 bytes from 193.0.14.129#53(k.root-servers.net) in 16 ms

dns.google.             10800   IN      NS      ns2.zdns.google.
dns.google.             10800   IN      NS      ns1.zdns.google.
dns.google.             10800   IN      NS      ns3.zdns.google.
dns.google.             10800   IN      NS      ns4.zdns.google.
dns.google.             3600    IN      DS      56044 8 2 1B0A7E90AA6B1AC65AA5B573EFC44ABF6CB2559444251B997103D2E4 0C351B08
dns.google.             3600    IN      RRSIG   DS 8 2 3600 20210813162212 20210722162212 7144 google. dsHlV4LcvBreUOU4rBVNRoD+ab7cg/pLrRevNBEfkQCEU4xXDVZ7ZF22 hARkPOj+HNSDy8JixYJ7b9zuSGSeYdH5DxU1cAmgJk+uTztdkTZ1TZJ9 B/J98BQpqoC1EvM68Gsgy3X5uTL8mJCM3GhbaYoPJZ7QExnFBZd32bDn Z0o=
;; Received 506 bytes from 216.239.34.105#53(ns-tld2.charlestonroadregistry.com) in 271 ms

dns.google.             900     IN      A       8.8.4.4
dns.google.             900     IN      A       8.8.8.8
dns.google.             900     IN      RRSIG   A 8 2 900 20210822160918 20210723160918 1773 dns.google. IhdaIrm+cRq1jxAC7ZU1el7ta7F4heEH1vGoVK773zAayCYxE0BsjUsj JOMTCT5U4eQp7hOVXA5Ml1BwT0CKY+Vrhv1KgmB8QU+HCmHhRsOw31J7 8X1uzYzrpthDyMLsols/jyV09wMbdqQ2Twjxese7ruQx+iknYYE2jMgn AS0=
;; Received 241 bytes from 216.239.38.114#53(ns4.zdns.google) in 111 ms

vagrant@vagrant:~$ dig -x 8.8.8.8

; <<>> DiG 9.16.1-Ubuntu <<>> -x 8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54565
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;8.8.8.8.in-addr.arpa.          IN      PTR

;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.   1038    IN      PTR     dns.google.

;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Sat Jul 24 09:36:50 UTC 2021
;; MSG SIZE  rcvd: 73

vagrant@vagrant:~$ dig -x 8.8.4.4

; <<>> DiG 9.16.1-Ubuntu <<>> -x 8.8.4.4
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 21954
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;4.4.8.8.in-addr.arpa.          IN      PTR

;; ANSWER SECTION:
4.4.8.8.in-addr.arpa.   6807    IN      PTR     dns.google.

;; Query time: 0 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Sat Jul 24 09:36:53 UTC 2021
;; MSG SIZE  rcvd: 73

```

---

### Как оформить ДЗ?

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Также вы можете выполнить задание в [Google Docs](https://docs.google.com/document/u/0/?tgif=d) и отправить в личном кабинете на проверку ссылку на ваш документ.
Название файла Google Docs должно содержать номер лекции и фамилию студента. Пример названия: "1.1. Введение в DevOps — Сусанна Алиева"
Перед тем как выслать ссылку, убедитесь, что ее содержимое не является приватным (открыто на комментирование всем, у кого есть ссылка). 
Если необходимо прикрепить дополнительные ссылки, просто добавьте их в свой Google Docs.

Любые вопросы по решению задач задавайте в чате Slack.

---
