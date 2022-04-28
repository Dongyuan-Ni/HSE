#!/usr/bin/env python
import os
# for PBE and HSE
fname = os.listdir('.')
os.chdir('1')
with open('eigen.dat', 'r') as f:
	data = f.readlines()[:-3]
for i in range(len(data)):
	data[i] = [float(tmp) for tmp in data[i].split()]
k1 = data[0][0]
for i in range(len(data)):
	data[i][0] -= k1
k_pre = data[-2][0]
print('File: 1')
print('k-point: {}'.format(k_pre))
os.chdir('..')

fdir = []
for i in fname:
	if os.path.isdir(i) == True:
		fdir.append(i)
fdir = [float(i) for i in fdir]
fdir.sort()
fdir = fdir[1:]
for i in range(len(fdir)):
	if fdir[i]*10%10 == 0:
		fdir[i] = int(fdir[i])		
fdir = [str(i) for i in fdir]

for name in fdir:
	os.chdir(str(name))
	with open('eigen.dat', 'r') as f:
		data_part = f.readlines()[:-3]
	for i in range(len(data_part)):
		data_part[i] = [float(tmp) for tmp in data_part[i].split()]
	k1 = data_part[0][0]
	for i in range(len(data_part)):
        	data_part[i][0] -= k1
		data_part[i][0] += k_pre
	data = data + data_part
	k_pre = data_part[-2][0]
	print('File: {}'.format(name))
	print('k-point: {}'.format(k_pre))
	os.chdir('..')

for i in range(len(data)):
	data[i] = '   '.join([str(tmp) for tmp in data[i]])+'\n'

with open('eigen_tot.dat', 'w') as f:
	f.writelines(data)

