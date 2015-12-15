#!/usr/bin/python
#by zhuxing
import datetime
def do_telnet(Host, username, password):
    import telnetlib

    tn = telnetlib.Telnet(Host)
    tn.set_debuglevel(2)

    tn.read_until('Username:')
    tn.write(username + '\n')

    tn.read_until('Password:')
    tn.write(password + '\n')

    tn.read_until('#')
    tn.write('sh run ' + '\n')
    spacetime = 0
    while spacetime <= 500:
        tn.write(" ")
        spacetime = spacetime + 1
    #msg=tn.read_until("#")
    msg=tn.read_until("# ")
    when = datetime.datetime.now().strftime("%Y%m%d")
    path = when+Host+"_config.txt"
    f = file(path,"wb")
    f.write(msg)
    f.close()

    tn.close() # tn.write('exit\n')

if __name__=='__main__':
    import random, string, re, os
    file = open("ip.txt")
    lines = file.readlines()
    username = 'user'
    password = 'pass'
    for line in lines:
        Host = line.split('\t')[0].strip()
        do_telnet(Host, username, password)
        time.sleep(5)
