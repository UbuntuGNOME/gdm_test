#!/usr/bin/python
import pexpect

git_command = 'git push -u origin master'
child = pexpect.spawn(git_command)
child.expect("Username for 'https://github.com':")
child.sendline('stratus-ss')
child.expect("Password for 'https://stratus-ss@github.com':")
child.sendline('Gv3hPJH*9ME!oJ7u0G')
cmd_show_data = child.before
cmd_output = cmd_show_data.split('\r\n')
for data in cmd_output:
	print data
