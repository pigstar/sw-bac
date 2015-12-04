#by zhuxing
import datetime
def do_telnet(Host, username, password):
import telnetlib
 
tn = telnetlib.Telnet(Host)
tn.set_debuglevel(2)
 
tn.read_until(‘Username:’)
tn.write(username + ‘\n’)
 
tn.read_until(‘Password:’)
tn.write(password + ‘\n’)
 
tn.read_until(‘switch#’)
tn.write(‘sh run ‘ + ‘\n’)
spacetime = 0
while spacetime &lt;= 500:
tn.write(” “)
spacetime = spacetime + 1
msg=tn.read_until(“switch# “)
when = datetime.datetime.now().strftime(“%Y%m%d”)
path = when+”_swconfig.txt”
f = file(path,”wb”)
f.write(msg)
f.close()
 
tn.close() # tn.write(‘exit\n’)
 
if __name__==’__main__’:
Host = ‘switch ip address’
username = ‘username’
password = ‘password’
do_telnet(Host, username, password)
