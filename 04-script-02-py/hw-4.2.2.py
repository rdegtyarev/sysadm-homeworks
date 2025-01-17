#!/usr/bin/env python3

import os
# Задаем рабочую директорию и передаем ее bash_command на следующем шаге
full_dir = '~/PycharmProjects/sysadm-homeworks'
bash_command = ["cd " + full_dir, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')

        # добавляем к результату полный путь директории исполнения  вместе с /
        prepare_result = full_dir + '/' + prepare_result

        print(prepare_result)
        # для отображения всех измененных файлов нужно убрать прерывание цикла
        # break
