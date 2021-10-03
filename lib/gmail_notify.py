#/usr/bin/python3
'''
Created on 2021/10/02

@author: ZL Chen
@title: Sent the email notify.
'''

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class gmail_notify(object):
		
	def gmail(self, sent_email, receive_email):  
		self.content = MIMEMultipart()  #建立 MIMEMultipart 物件
		self.content['subject'] = 'Warning!'  #郵件標題
		self.content['from'] = sent_email  #寄件者
		self.content['to'] = receive_email #收件者
		self.content.attach(MIMEText(
			'\n\nDear SVT members,\n\n\tWarning! \
			\n\tWe are under a attack! \
			\n\t"The SVT NOTIFY is notify by ZL demo.\"\n\nZL.'))  #郵件內容

	def smtplib_smtp(self):
		with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:  # 設定 SMTP 伺服器
			try:
				smtp.ehlo()  # 驗證 SMTP 伺服器
				smtp.starttls()  # 建立加密傳輸
				smtp.login(self.content['from'], 'aipyrivzffkgwmbs')  # 登入寄件者gmail
				smtp.send_message(self.content)  # 寄送郵件
				print('Complete!')
			except Exception as e:
				print('Error message: ', e)
	
if __name__ == "__main__":
	g_n = gmail_notify()
	g_n.gmail('iec100535@gmail.com', 'Chen.ZL@inventec.com,chen.kerr@inventec.com')
	g_n.smtplib_smtp()