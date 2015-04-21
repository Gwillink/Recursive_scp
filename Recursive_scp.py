from findtools.find_files import (find_files, Match)
import paramiko # from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.load_host_keys('/Users/geeshan/.ssh/known_hosts')
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) ### add key if needed??
ssh.connect('130.211.97.164', username='dm')

scp = SCPClient(ssh.get_transport())

sh_files_pattern = Match(filetype='f', name='*')
found_files = find_files(path='/Users/geeshan/Downloads', match=sh_files_pattern)

for found_file in found_files:
     print found_file
     scp.put(found_file, remote_path='/home/dm')
    
#scp.put('/Users/geeshan/Documents/linux.txt', remote_path='/home/dm')
#scp.put('test.txt', 'test2.txt')
#scp.get('test2.txt')