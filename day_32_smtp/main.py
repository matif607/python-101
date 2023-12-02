import smtplib as s

my_email = 'mohdatif.2097@gmail.com'
my_password = 'nvfjodqtjjprucit'

connection = s.SMTP('smtp.gmail.com')

connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs='atifshaikh1996@gmail.com', msg='Hello, this is automated email')
connection.close()
