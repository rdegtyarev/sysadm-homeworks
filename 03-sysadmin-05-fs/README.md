# Домашнее задание к занятию "3.5. Файловые системы"

1. Узнайте о [sparse](https://ru.wikipedia.org/wiki/%D0%A0%D0%B0%D0%B7%D1%80%D0%B5%D0%B6%D1%91%D0%BD%D0%BD%D1%8B%D0%B9_%D1%84%D0%B0%D0%B9%D0%BB) (разряженных) файлах.
```bash
Done
```
1. Могут ли файлы, являющиеся жесткой ссылкой на один объект, иметь разные права доступа и владельца? Почему?
```bash
# Нет, жесткие ссылки реализованы низкоуровнево. Каждый файл жесткой ссылки ведет в к одному участку жесткого диска.
# При смене разрешений на жесткой ссылке, разрешения поменяются также на исходом файле. Пример:
vagrant@vagrant:~$ toush testfile
vagrant@vagrant:~$ ln -P testfile test_file_hard_link
vagrant@vagrant:~$ ls -li
# Меняем права на жесткую ссылку 
vagrant@vagrant:~$ chmod 0755 test_file_hard_link 
# Права изменятся также на исходном файле
vagrant@vagrant:~$ ls -li
total 12
131081 -rw-rw-r-- 1 vagrant vagrant 182 Jul 22 18:11 sdb-dump
131084 -rwxr-xr-x 2 vagrant vagrant  18 Jul 22 19:54 test_file_hard_link
131084 -rwxr-xr-x 2 vagrant vagrant  18 Jul 22 19:54 testfile

```
1. Сделайте `vagrant destroy` на имеющийся инстанс Ubuntu. Замените содержимое Vagrantfile следующим:

    ```bash
    Vagrant.configure("2") do |config|
      config.vm.box = "bento/ubuntu-20.04"
      config.vm.provider :virtualbox do |vb|
        lvm_experiments_disk0_path = "/tmp/lvm_experiments_disk0.vmdk"
        lvm_experiments_disk1_path = "/tmp/lvm_experiments_disk1.vmdk"
        vb.customize ['createmedium', '--filename', lvm_experiments_disk0_path, '--size', 2560]
        vb.customize ['createmedium', '--filename', lvm_experiments_disk1_path, '--size', 2560]
        vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', lvm_experiments_disk0_path]
        vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', lvm_experiments_disk1_path]
      end
    end
    ```

    Данная конфигурация создаст новую виртуальную машину с двумя дополнительными неразмеченными дисками по 2.5 Гб.
```bash
Done
```
1. Используя `fdisk`, разбейте первый диск на 2 раздела: 2 Гб, оставшееся пространство.
```bash
# смотрим доступные устройства
vagrant@vagrant:~$ sudo fdisk -l
Disk /dev/sda: 64 GiB, 68719476736 bytes, 134217728 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x551c7ad5

Device     Boot   Start       End   Sectors  Size Id Type
/dev/sda1  *       2048   1050623   1048576  512M  b W95 FAT32
/dev/sda2       1052670 134215679 133163010 63.5G  5 Extended
/dev/sda5       1052672 134215679 133163008 63.5G 8e Linux LVM

# диск 1
Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

# диск 2
Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/vgvagrant-root: 62.55 GiB, 67150807040 bytes, 131153920 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/vgvagrant-swap_1: 980 MiB, 1027604480 bytes, 2007040 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

# Приступаем к разметке первого диска
vagrant@vagrant:~$ sudo fdisk /dev/sdb

Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0x0d14c645.

# Проверяем текущую таблицу разделов (пустая)
Command (m for help): p
Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0d14c645

# Создаем новый раздел
Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
# Выбираем Primary
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-5242879, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-5242879, default 5242879): +2048M # Размер 2 ГБ
Created a new partition 1 of type 'Linux' and of size 2 GiB.
# Проверяем результат
Command (m for help): p
Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0d14c645

Device     Boot Start     End Sectors Size Id Type
/dev/sdb1        2048 4196351 4194304   2G 83 Linux
# Раздел sdb1 (2GB) создан
# Создаем второй раздел
Command (m for help): n
Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
# Выбираем Primary
Select (default p): p
Partition number (2-4, default 2): 2
First sector (4196352-5242879, default 4196352): # по умолчанию
Last sector, +/-sectors or +/-size{K,M,G,T,P} (4196352-5242879, default 5242879): # по умолчанию (до конца диска)

Created a new partition 2 of type 'Linux' and of size 511 MiB.
# Проверяем
Command (m for help): p
Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0d14c645

Device     Boot   Start     End Sectors  Size Id Type
/dev/sdb1          2048 4196351 4194304    2G 83 Linux
/dev/sdb2       4196352 5242879 1046528  511M 83 Linux
# Видим два раздела, sdb1 (2G) и sdb2 (511M)
# Сохраняем таблицу разделов
Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

# разделы созданы
```
1. Используя `sfdisk`, перенесите данную таблицу разделов на второй диск.
```bash
vagrant@vagrant:~$ sudo sfdisk -d /dev/sdb > sdb-dump # сохраняем дамп в файл sdb-dump

vagrant@vagrant:~$ cat sdb-dump # проверяем результат sdb-dump
label: dos
label-id: 0x0d14c645
device: /dev/sdb
unit: sectors

/dev/sdb1 : start=        2048, size=     4194304, type=83
/dev/sdb2 : start=     4196352, size=     1046528, type=83


vagrant@vagrant:~$ sudo sfdisk /dev/sdc < sdb-dump # восстанавливаем таблицу раздела на второй диск из дампа
Checking that no-one is using this disk right now ... OK

Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

>>> Script header accepted.
>>> Script header accepted.
>>> Script header accepted.
>>> Script header accepted.
>>> Created a new DOS disklabel with disk identifier 0x0d14c645.
/dev/sdc1: Created a new partition 1 of type 'Linux' and of size 2 GiB.
/dev/sdc2: Created a new partition 2 of type 'Linux' and of size 511 MiB.
/dev/sdc3: Done.

New situation:
Disklabel type: dos
Disk identifier: 0x0d14c645

Device     Boot   Start     End Sectors  Size Id Type
/dev/sdc1          2048 4196351 4194304    2G 83 Linux
/dev/sdc2       4196352 5242879 1046528  511M 83 Linux

The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.

vagrant@vagrant:~$ sudo fdisk /dev/sdc # проверяем результат

Welcome to fdisk (util-linux 2.34).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x0d14c645

Device     Boot   Start     End Sectors  Size Id Type
/dev/sdc1          2048 4196351 4194304    2G 83 Linux
/dev/sdc2       4196352 5242879 1046528  511M 83 Linux

Command (m for help): q

# второй диск размечен по аналогии с первым
```
1. Соберите `mdadm` RAID1 на паре разделов 2 Гб.
```bash
# создаем RAID1 на дисках 2 ГБ (sdb1, sdc1)
vagrant@vagrant:~$ sudo mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1
mdadm: Note: this array has metadata at the start and
    may not be suitable as a boot device.  If you plan to
    store '/boot' on this device please ensure that
    your boot-loader understands md/v1.x metadata, or use
    --metadata=0.90
mdadm: size set to 2094080K
Continue creating array? y
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.

# проверяем
vagrant@vagrant:~$ cat /proc/mdstat
Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10] 
md0 : active raid1 sdc1[1] sdb1[0]
      2094080 blocks super 1.2 [2/2] [UU]
      
unused devices: <none>

# RAID1 md0 готов

```
1. Соберите `mdadm` RAID0 на второй паре маленьких разделов.
```bash
# создаем RAID0 на дисках 511 M (sdc2, sdc2)
vagrant@vagrant:~$ sudo mdadm --create --verbose /dev/md1 --level=0 --raid-devices=2 /dev/sdb2 /dev/sdc2
mdadm: chunk size defaults to 512K
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md1 started.

# проверяем
vagrant@vagrant:~$ cat /proc/mdstat
Personalities : [linear] [multipath] [raid0] [raid1] [raid6] [raid5] [raid4] [raid10] 
md1 : active raid0 sdc2[1] sdb2[0]
      1042432 blocks super 1.2 512k chunks
      
md0 : active raid1 sdc1[1] sdb1[0]
      2094080 blocks super 1.2 [2/2] [UU]
      
unused devices: <none>

# RAID0 md1 готов
```
1. Создайте 2 независимых PV на получившихся md-устройствах.
```bash
# Проверяем имеющиеся PV
vagrant@vagrant:~$ sudo pvs
  PV         VG        Fmt  Attr PSize   PFree
  /dev/sda5  vgvagrant lvm2 a--  <63.50g    0 

# Создаем PV на md0 и md1
vagrant@vagrant:~$ sudo pvcreate /dev/md0 /dev/md1
  Physical volume "/dev/md0" successfully created.
  Physical volume "/dev/md1" successfully created.
# Проверяем статус
vagrant@vagrant:~$ sudo pvs
  PV         VG        Fmt  Attr PSize    PFree   
  /dev/md0             lvm2 ---    <2.00g   <2.00g
  /dev/md1             lvm2 ---  1018.00m 1018.00m
  /dev/sda5  vgvagrant lvm2 a--   <63.50g       0 
# PV созданы
```
1. Создайте общую volume-group на этих двух PV.
```bash
# Создаем группу vol_grp1
vagrant@vagrant:~$ sudo vgcreate vol_grp1 /dev/md0 /dev/md1
  Volume group "vol_grp1" successfully created
# Проверяем
vagrant@vagrant:~$ sudo vgdisplay
  --- Volume group ---
  VG Name               vgvagrant
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  3
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                2
  Open LV               2
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               <63.50 GiB
  PE Size               4.00 MiB
  Total PE              16255
  Alloc PE / Size       16255 / <63.50 GiB
  Free  PE / Size       0 / 0   
  VG UUID               7BSgp8-ukNs-898j-wRdT-jDVA-TLU9-sSZ36F
   
  --- Volume group ---
  VG Name               vol_grp1
  System ID             
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               <2.99 GiB
  PE Size               4.00 MiB
  Total PE              765
  Alloc PE / Size       0 / 0   
  Free  PE / Size       765 / <2.99 GiB
  VG UUID               Ft4thB-Mwr6-UdDW-6B95-GgqZ-IEZo-aFvPWe


```
1. Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.
```bash
# Создаем LV logical_vol1
vagrant@vagrant:~$ sudo lvcreate -L 100M -n logical_vol1 vol_grp1 /dev/md1
  Logical volume "logical_vol1" created.
# Проверяем
vagrant@vagrant:~$ sudo lvdisplay /dev/vol_grp1/logical_vol1 
  --- Logical volume ---
  LV Path                /dev/vol_grp1/logical_vol1
  LV Name                logical_vol1
  VG Name                vol_grp1
  LV UUID                NifJvs-wyB8-BqQM-Puvh-Qtfa-610w-AYLPdQ
  LV Write Access        read/write
  LV Creation host, time vagrant, 2021-07-22 19:02:38 +0000
  LV Status              available
  # open                 0
  LV Size                100.00 MiB
  Current LE             25
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     4096
  Block device           253:2

```
1. Создайте `mkfs.ext4` ФС на получившемся LV.
```bash
# Создание файловой ситемы
vagrant@vagrant:~$ sudo mkfs.ext4 /dev/vol_grp1/logical_vol1 
mke2fs 1.45.5 (07-Jan-2020)
Creating filesystem with 25600 4k blocks and 25600 inodes

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (1024 blocks): done
Writing superblocks and filesystem accounting information: done

```

1. Смонтируйте этот раздел в любую директорию, например, `/tmp/new`.
```bash
vagrant@vagrant:~$ mkdir /tmp/new
vagrant@vagrant:~$ sudo mount /dev/vol_grp1/logical_vol1 /tmp/new

```
1. Поместите туда тестовый файл, например `wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz`.
```bash
# Скачиваем файл
vagrant@vagrant:~$ sudo wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz
--2021-07-22 19:15:28--  https://mirror.yandex.ru/ubuntu/ls-lR.gz
Resolving mirror.yandex.ru (mirror.yandex.ru)... 213.180.204.183, 2a02:6b8::183
Connecting to mirror.yandex.ru (mirror.yandex.ru)|213.180.204.183|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 21100981 (20M) [application/octet-stream]
Saving to: ‘/tmp/new/test.gz’

/tmp/new/test.gz    100%[===================>]  20.12M  5.00MB/s    in 4.2s    

2021-07-22 19:15:32 (4.82 MB/s) - ‘/tmp/new/test.gz’ saved [21100981/21100981]
# Проверяем
vagrant@vagrant:~$ ls /tmp/new/
lost+found  test.gz

```
1. Прикрепите вывод `lsblk`.
```bash
vagrant@vagrant:~$ lsblk
NAME                        MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda                           8:0    0   64G  0 disk  
├─sda1                        8:1    0  512M  0 part  /boot/efi
├─sda2                        8:2    0    1K  0 part  
└─sda5                        8:5    0 63.5G  0 part  
  ├─vgvagrant-root          253:0    0 62.6G  0 lvm   /
  └─vgvagrant-swap_1        253:1    0  980M  0 lvm   [SWAP]
sdb                           8:16   0  2.5G  0 disk  
├─sdb1                        8:17   0    2G  0 part  
│ └─md0                       9:0    0    2G  0 raid1 
└─sdb2                        8:18   0  511M  0 part  
  └─md1                       9:1    0 1018M  0 raid0 
    └─vol_grp1-logical_vol1 253:2    0  100M  0 lvm   /tmp/new
sdc                           8:32   0  2.5G  0 disk  
├─sdc1                        8:33   0    2G  0 part  
│ └─md0                       9:0    0    2G  0 raid1 
└─sdc2                        8:34   0  511M  0 part  
  └─md1                       9:1    0 1018M  0 raid0 
    └─vol_grp1-logical_vol1 253:2    0  100M  0 lvm   /tmp/new

```
1. Протестируйте целостность файла:

    ```bash
    root@vagrant:~# gzip -t /tmp/new/test.gz
    root@vagrant:~# echo $?
    0
    ```
```bash
# Done
vagrant@vagrant:~$ gzip -t /tmp/new/test.gz
vagrant@vagrant:~$ echo $?
0

```

1. Используя pvmove, переместите содержимое PV с RAID0 на RAID1.
```bash
# Переносим
vagrant@vagrant:~$ sudo pvmove /dev/md1 /dev/md0
  /dev/md1: Moved: 12.00%
  /dev/md1: Moved: 100.00%
# Проверяем
vagrant@vagrant:~$ lsblk
NAME                        MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
sda                           8:0    0   64G  0 disk  
├─sda1                        8:1    0  512M  0 part  /boot/efi
├─sda2                        8:2    0    1K  0 part  
└─sda5                        8:5    0 63.5G  0 part  
  ├─vgvagrant-root          253:0    0 62.6G  0 lvm   /
  └─vgvagrant-swap_1        253:1    0  980M  0 lvm   [SWAP]
sdb                           8:16   0  2.5G  0 disk  
├─sdb1                        8:17   0    2G  0 part  
│ └─md0                       9:0    0    2G  0 raid1 
│   └─vol_grp1-logical_vol1 253:2    0  100M  0 lvm   /tmp/new
└─sdb2                        8:18   0  511M  0 part  
  └─md1                       9:1    0 1018M  0 raid0 
sdc                           8:32   0  2.5G  0 disk  
├─sdc1                        8:33   0    2G  0 part  
│ └─md0                       9:0    0    2G  0 raid1 
│   └─vol_grp1-logical_vol1 253:2    0  100M  0 lvm   /tmp/new
└─sdc2                        8:34   0  511M  0 part  
  └─md1                       9:1    0 1018M  0 raid0 

```
1. Сделайте `--fail` на устройство в вашем RAID1 md.
```bash
vagrant@vagrant:~$ sudo mdadm /dev/md0 --fail /dev/sdb1
mdadm: set /dev/sdb1 faulty in /dev/md0
```

1. Подтвердите выводом `dmesg`, что RAID1 работает в деградированном состоянии.
```bash
vagrant@vagrant:~$ dmesg | grep "md0"
[  769.996998] md/raid1:md0: not clean -- starting background reconstruction
[  769.996999] md/raid1:md0: active with 2 out of 2 mirrors
[  769.997012] md0: detected capacity change from 0 to 2144337920
[  769.998471] md: resync of RAID array md0
[  780.693920] md: md0: resync done.
[ 6020.240465] md/raid1:md0: Disk failure on sdb1, disabling device. # видим деградированыный режим
               md/raid1:md0: Operation continuing on 1 devices.

```
1. Протестируйте целостность файла, несмотря на "сбойный" диск он должен продолжать быть доступен:

    ```bash
    root@vagrant:~# gzip -t /tmp/new/test.gz
    root@vagrant:~# echo $?
    0
    ```
```bash
Done

vagrant@vagrant:~$ gzip -t /tmp/new/test.gz
vagrant@vagrant:~$ echo $?
0

```
1. Погасите тестовый хост, `vagrant destroy`.
```bash
Done
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
