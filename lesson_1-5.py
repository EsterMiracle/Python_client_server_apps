"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
 из байтовового в строковый тип на кириллице."""

import subprocess

args1 = ['ping', 'yandex.ru']
args2 = ['ping', 'youtube.com']

# почему-то не сработало с кодировкой форматов 'utf-8' и 'windows-1251', сработало только через 'CP866'
subproc_ping = subprocess.Popen(args1, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode('CP866'), end='')

subproc_ping = subprocess.Popen(args2, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode('CP866'), end='')
