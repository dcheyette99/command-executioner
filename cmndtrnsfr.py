import paramiko
import os.path

hostname = 'clab-srl-srl'
username = 'admin'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname, username=username,
            key_filename='/home/dcheyette/.ssh/id_ed25519')

remotepath = "/home/admin/test_config.txt"
localpath = "/home/dcheyette/cmndrexec/test_config.txt"
remotedir = "/home/admin"

sftp = ssh.open_sftp()
sftp.put(localpath=localpath, remotepath=remotepath)
print(sftp.listdir(path=remotedir))

# Cleanup
ssh.close()

