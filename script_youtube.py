try:
    import os,sys,time,requests
except:
    os.system('pip install requests')

def test(x):
    for i in x+ '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.10)

if sys.version[0] != '3':
    exit('run in python3')

test('✪ welcome to my tool ✪ hhhhhhhhhhhhhhhhhhhh')
ip = requests.get('https://api.ipify.org/').text.strip()
#print(f'Your IP : {ip}')

red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;36m'

print(f'{red}[1] {green}↧ INSTALL PKG ')
print(f'{red}[2] {green}⟲ UPDATE')
print(f'{red}[0] {green}☓ EXIT')
choose = input(f'{blue}Choose options :\033[1;37m')

if choose == '1':
    os.system('pip install gTTS')
    os.system('clear')
    print('Successfully installed')
    time.sleep(5)
    os.system('clear')
    os.system('python script_youtube.py')
elif choose == '2':
    os.system('git pull https://github.com/python-life/script')
elif choose == '0':
    sys.exit()
else:
    print('Please choose only 1 or 2 or 0 for exit')
    time.sleep(4)
    os.system('clear')
    os.system('python script_youtube.py')

