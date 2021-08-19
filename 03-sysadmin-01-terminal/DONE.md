# hw-3.1
1. Ok
2. Ok
3. Ok
4. Ok
5. Memory 1024, CPU 1
6.  Vagrant.configure("2") do |config|
      config.vm.box = "bento/ubuntu-20.04"
        config.vm.provider "virtualbox" do |v|
            v.memory = 2048
            v.cpus = 2
        end
     end
7. Ok
8.1. HISTSIZE (пример export HISTSIZE=5)
8.2 Параметры HISTCONTROL. Не писать строку после команды дублирования строки и не писать строки, начинающиеся с одного или нескольких пробелов в истории. Пример: export ISTCONTROL="ignoredups"
9. Последовательности. Раздел Brace Expansion
10. Лимит на арgetconf ARG_MAX
11. Условие, есть ли папка /tmp
12.
vagrant@vagrant:~$ mkdir tmp
vagrant@vagrant:~$ mkdir ./tmp/new_path_directory
vagrant@vagrant:~$ cp /bin/bash ./tmp/new_path_directory/
vagrant@vagrant:~$ export PATH=/home/vagrant/tmp/new_path_directory/:$PATH
vagrant@vagrant:~$ type -a bash
bash is /home/vagrant/tmp/new_path_directory/bash
bash is /usr/bin/bash
bash is /bin/bash

13. at - выполняет команду в назначенное время
batch - выполняет команды, когда позволяют уровни загрузки системы (когда среднее значение нагрузки падает ниже 1,5 или значения
, указанного в вызове atd.)
14. Ok


