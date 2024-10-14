#coding=utf-8
import os, sys, platform
os.system("git pull")
os.system('rm -rf safeum.so')
 
try:
    if sys.argv[1]=='update':
        os.system('rm -rf safeum.so')
except:
    pass
 
 
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('safeum.so'):
        os.system('curl -L https://github.com/ALI-JUTT/SafeUM/blob/main/safeum.cpython-312.so?raw=true -o safeum.so') 
        import safeum
    else:
        import safeum
 
elif bit == '32bit':
    print("\033[1;90m [\033[1;91m Sorry Baby 32Bit Not Supported! ðŸ¥ºðŸ’”\033[1;90m]");exit()
 
 
