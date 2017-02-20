#!/bin/python

from subprocess import call

print('starting setup')

apps = ('php', 'git', 'vim', 'net-tools', 'telnet')
sysops = ('enable', 'start', 'status')
reload = ('reload', 'status')
svcs = ('--add-service=http','--add-service=https')


for app in apps:
  call(['yum', 'install', app, '-y'])

for op in sysops:
  call(['systemctl', op, 'httpd'])

for svc in svcs:
  call(['firewall-cmd', '--zone=public', '--permanent', svc])

for relo in reload:
  call(['systemctl', relo, 'firewalld'])

print('setup complete')
