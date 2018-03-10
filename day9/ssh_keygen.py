# author: zzq
# 基于公钥秘钥连接


import  paramiko

private_key = paramiko.RSAKey.from_private_key('/home/auto/.ssh/id_rsa')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='cl.salt.com', port=22, username='wupeiqi', key=private_key)

stdin, stdout, stderr = ssh.exec_command('df')

result = stdout.read()

ssh.close()
