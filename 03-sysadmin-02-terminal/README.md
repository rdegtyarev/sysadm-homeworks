# Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"

1. Какого типа команда `cd`? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.  
   
    **Решение:**  
   Относится к builtin командам 
   ``` bash
   type cd
   cd is a shell builtin
   ```
   Команда встроенная в интерпретатор оболочки (всегда в ОЗУ).
   Причина: Основная команда для работы с директориями. Linux - file-based ОС, команды работающие с каталогами и файлами должны быть приоритетными и присктствовтаь как базовые во всех дистрибутивах ОС.<br/>

2. Какая альтернатива без pipe команде `grep <some_string> <some_file> | wc -l`? `man grep` поможет в ответе на этот вопрос. Ознакомьтесь с [документом](http://www.smallo.ruhr.de/award.html) о других подобных некорректных вариантах использования pipe.  
   **Решение:**  
   ```bash
   grep -c <some_string> <some_file>
   ```  
   
3. Какой процесс с PID `1` является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?   
   **Решение:**  
   systemd  
   
4. Как будет выглядеть команда, которая перенаправит вывод stderr `ls` на другую сессию терминала?  
   **Решение:**  
   ```bash
   ls > /dev/pts/1
   ```
5. Получится ли одновременно передать команде файл на stdin и вывести ее stdout в другой файл? Приведите работающий пример.  
    **Решение:**  
      ```bash
    vagrant@vagrant:~/tmp/test$ echo -e "first \nsecond \nthird" > newfile
    vagrant@vagrant:~/tmp/test$ cat newfile
    first
    second
    third
    vagrant@vagrant:~/tmp/test$ cat newfile > result
    vagrant@vagrant:~/tmp/test$ cat result
    first
    second
    third
    ```

6. Получится ли вывести находясь в графическом режиме данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?  
   **Решение:**  
   ```bash
   roman@ThinkPad:~$ ls /dev/pts #отобразить все tty
   0  1  ptmx
   roman@ThinkPad:~$ tty #определить какой из них текущий pty
   /dev/pts/0
   roman@ThinkPad:~$ echo "hello" > /dev/pts/1 #вывести "hello" в другой tty
    ```
7. Выполните команду `bash 5>&1`. К чему она приведет? Что будет, если вы выполните `echo netology > /proc/$$/fd/5`? Почему так происходит?  
   **Решение:**  
   `bash 5>&1` - перенаправление файла с дескриптором `5` в поток вывода (stdout, дескриптор 1) `bash`  
   `echo netology > /proc/$$/fd/5` - передать `netology` в созданный дескриптор `5`. Результатом будет вывод `netology` в `stdout`.
     
8. Получится ли в качестве входного потока для pipe использовать только stderr команды, не потеряв при этом отображение stdout на pty? Напоминаем: по умолчанию через pipe передается только stdout команды слева от `|` на stdin команды справа.
Это можно сделать, поменяв стандартные потоки местами через промежуточный новый дескриптор, который вы научились создавать в предыдущем вопросе.  
   **Решение:**  
   ```bash
   vagrant@vagrant:~$ mkdir folder #создал папку folder, файлы non_exist и non_exist_two не существуют
   vagrant@vagrant:~$ ls ./folder ./non_exist ./non_exist_two  5>&1 2>&5 1>/dev/pts/0 | grep "two"
   ls: cannot access './non_exist_two': No such file or directory #grep по stderr
   ./folder: #ответ команды в stdout pty
    ```
   
9. Что выведет команда `cat /proc/$$/environ`? Как еще можно получить аналогичный по содержанию вывод?  
   **Решение:**  
   `/proc/$$/environ` - переменные окружения для текущего `bash` процесса
   Аналогичный по содержанию вывод: `env`  
   
10. Используя `man`, опишите что доступно по адресам `/proc/<PID>/cmdline`, `/proc/<PID>/exe`.  
   **Решение:**  
   `/proc/<PID>/cmdline` - содержит команду, которая запустила данный процесс.  
   `/proc/<PID>/exe` - ссылка на исполняемый файл.  
   
11. Узнайте, какую наиболее старшую версию набора инструкций SSE поддерживает ваш процессор с помощью `/proc/cpuinfo`.  
   **Решение:**  
    `cat /proc/cpuinfo | grep flags | grep sse`  
    Старщая версия - SSE  
    `flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr` **sse** `sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local clzero irperf xsaveerptr rdpru wbnoinvd arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif umip rdpid overflow_recov succor smca`
    
12. При открытии нового окна терминала и `vagrant ssh` создается новая сессия и выделяется pty. Это можно подтвердить командой `tty`, которая упоминалась в лекции 3.2. Однако:

    ```bash
	vagrant@netology1:~$ ssh localhost 'tty'
	not a tty
    ```

	Почитайте, почему так происходит, и как изменить поведение.  
   **Решение:**  
    ```bash
    
    ```
    

1. Бывает, что есть необходимость переместить запущенный процесс из одной сессии в другую. Попробуйте сделать это, воспользовавшись `reptyr`. Например, так можно перенести в `screen` процесс, который вы запустили по ошибке в обычной SSH-сессии.  
   **Решение:**  
    ```bash
    
    ```
   
1. `sudo echo string > /root/new_file` не даст выполнить перенаправление под обычным пользователем, так как перенаправлением занимается процесс shell'а, который запущен без `sudo` под вашим пользователем. Для решения данной проблемы можно использовать конструкцию `echo string | sudo tee /root/new_file`. Узнайте что делает команда `tee` и почему в отличие от `sudo echo` команда с `sudo tee` будет работать.  
   **Решение:**
    Команда  tee сохраняет вывод команды в файл. Пример:
   ```bash
   vagrant@vagrant:~$ echo netoloy | tee result
   netoloy
   vagrant@vagrant:~$ cat result
   netoloy
    ```
   Перенаправление выполняет процесс shell'a, который запущен без sudo и не имеет доступа для записи в root
   Отличие tee в том, что это команда, которую можно запустить под sudo
   ```bash
   vagrant@vagrant:~$ echo string | sudo tee /root/new_file
   string
   vagrant@vagrant:~$ sudo cat /root/new_file
   string
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
