# author: zzq


import paramiko

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='GSuser', password='123')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()