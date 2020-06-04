import smtplib, os, time
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
	os.system('figlet Mail.Sender')
	
	print('')
	print('Author: Exploit-A')
	print('My telegram channel: https://t.me/exp1oited')
	print('')
	time.sleep(2)

# Your Gmail address
fromaddr = raw_input("Gmail login: ")
#############################

# Password of your account
passw    = raw_input("Gmail password: ")
#############################

# Receiver address
toaddr   = raw_input("Receiver's address: ")
#############################

# This is your message you want to send receiver
message  = raw_input("Your message: ")
#############################
print('')
print("Starting...")
# Create server
server = smtplib.SMTP('smtp.gmail.com', 587)
# Check connection
server.ehlo()
# Start connection
server.starttls()
# Check connection
server.ehlo()
# Logging in (Login, Password)
server.login(fromaddr, passw)

# Send mail (Your address, to address, message)
try:	
	server.sendmail(fromaddr, toaddr, message)
	print("Success! :)")
except:
	print("Fail! :(")

# Close connection
server.quit()
print("If you want to do it automaticaly, write your data in this file. Good luck! :)")
time.sleep(1)

