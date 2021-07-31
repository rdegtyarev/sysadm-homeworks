#!/usr/bin/env python3

import os
import sys

# при запуске скрипта в параметр нужно передать путь до директории
# параметр передаем в переменную full_dir
full_dir = sys.argv[1]
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