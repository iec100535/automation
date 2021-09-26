# -*- coding: utf-8 -*-
'''
Created on 2021/09/26

@author: ZL Chen
@title: Data transfer for samba export log.
'''

from os import system
from re import sub

class samba_trans(object):

	def initial(self, num):
		numbers = {
			0: 'Interfaces,RX bps,pps%,TX bps,pps%'
		}
		return numbers.get(num)

	def open_file(self, file_name):
		f_read = open(file_name, 'r').readlines()
		# print(f_read)
		count = len(f_read)
		for i in range(count):
			l_r_strip = str(f_read[i]).lstrip().rstrip().strip('b\'')
			# print(l_r_strip)
			if 'Interface' in l_r_strip:
				output_title = self.initial(0)
				# print(output_title)
				system('echo ' + output_title + ' >> samba_trans.txt')
			else:
				output_content = sub('\s{2,}', ',', l_r_strip.strip())
				# print(output_content)
				system('echo ' + output_content + ' >> samba_trans.txt')	

if __name__ == '__main__':
	system('del samba_trans.txt')
	sb_t = samba_trans()
	sb_t.open_file('samba.txt')
