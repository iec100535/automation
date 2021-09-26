# -*- coding: utf-8 -*-
'''
Created on 2021/09/26

@author: ZL Chen
@title: Data transfer for samba export log.
'''

import os, time
from re import sub

class samba_convert(object):

	def initial(self, num):
		title = {
			0: 'Interfaces,RX bps,pps%,TX bps,pps%'
		}
		return title.get(num)

	def open_file(self, file_name):
		f_read = open(file_name, 'r').readlines()
		# print(f_read)
		count = len(f_read)
		print('Convert the samba.txt...')
		time.sleep(1)
		for i in range(count):
			l_r_strip = str(f_read[i]).lstrip().rstrip().strip('b\'')
			# print(l_r_strip)
			if 'Interface' in l_r_strip:
				output_title = self.initial(0)
				print(output_title)
				os.system('echo ' + output_title + ' >> samba_convert.txt')
			else:
				output_content = sub('\s{2,}', ',', l_r_strip.strip())
				print(output_content)
				os.system('echo ' + output_content + ' >> samba_convert.txt')	

if __name__ == '__main__':
	os.system('del samba_convert.txt')
	time.sleep(1)
	sb_t = samba_convert()
	print('Catch the samba.txt...')
	time.sleep(1)
	sb_t.open_file('samba.txt')
	print('\n\tThe \"samba.txt\" file is converted to \"samba_convert.txt\"')
