# uncompyle6 version 3.8.0
# Python bytecode 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
# [GCC 9.4.0]
# Embedded file name: sneakypass.py
import os, subprocess
subprocess.call('netsh wlan show profiles > temp_file.txt', shell=True)
filtered_wifi_names = []
with open('temp_file.txt', 'r') as (tempFile):
    lines = tempFile.readlines()
    for line in lines:
        if 'All User Profile     : ' in line:
            wifi = line.split('All User Profile     : ', 1)[(-1)]
            wifi = wifi.rstrip()
            filtered_wifi_names.append(wifi)

os.remove('temp_file.txt')
if len(filtered_wifi_names) != 0:
    print('There are currently', len(filtered_wifi_names), 'WiFi networks saved on this machine')
    print('Please wait while I find the passwords')
    for wifi_name in filtered_wifi_names:
        command = 'netsh wlan show profiles name="%s" key=clear | findstr "Key Content" >> temp_pass.txt' % wifi_name
        subprocess.call(command, shell=True)
    else:
        with open('temp_pass.txt', 'r') as (passFile):
            lines = passFile.readlines()
            filtered_passwords = []
            for line in lines:
                password = line.split(': ', 1)[(-1)]
                password = password.rstrip()
                filtered_passwords.append(password)

        with open('WiFi Passwords.txt', 'w') as (saveFile):
            if len(filtered_passwords) == len(filtered_wifi_names):
                for x in range(len(filtered_passwords)):
                    wife = filtered_wifi_names[x]
                    passwd = filtered_passwords[x]
                    if passwd == '1':
                        passwd = 'Wi-Fi has no password'
                        saveFile.write(wife + ' : ' + passwd + '\n')
                    else:
                        saveFile.write(wife + ' : ' + passwd + '\n')

            os.remove('temp_pass.txt')
            print('Passwords saved at WiFi Passwords.txt')

else:
    print('There is currently no WiFi saved on this machine')
# okay decompiling sneakypass.pyc
