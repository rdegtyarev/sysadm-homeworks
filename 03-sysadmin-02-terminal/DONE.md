# hw-3.2

1. Относится к builtin командам<br/>
  type cd<br/>
  cd is a shell builtin<br/>
Команда встроенная в интерпретатор оболочки (всегда в ОЗУ).<br/>
Причина: Основная команда для работы с директориями. Linux - file-based ОС, команды работающие с каталогами и файлами должны быть приоритетными и присктствовтаь как базовые во всех дистрибутивах ОС.<br/>

2. grep -c <some_string> <some_file><br/>

3. systemd<br/>

4. ls > /dev/pts/1<br/>

5. <br/>
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
6. 
