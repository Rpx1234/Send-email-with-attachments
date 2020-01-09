#make sure you allow less secure app access in google security https://myaccount.google.com/security
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders
import glob
#email address of sender
fromaddress = "From email"                                           # You Must edit this line
#email address of recipient 
toaddress = ["Email 1","email 2"]         #just add ,"another email" to have more than 2 emails or remove ,"email 2" to have only one email.
#sets directory for file scan
dir_path = 'C:\\Random file location'
# finds files in specific directory
filelist = []
files = [f for f in glob.glob(dir_path + "**/*.txt", recursive=True)]          # change file type
files1 = [g for g in glob.glob(dir_path + "**/*.xlsx", recursive=True)]       # change file type
files2 = [h for h in glob.glob(dir_path + "**/*.temp", recursive=True)]       # change file type

for f in files:
    filelist.append(f)
for g in files1:
    filelist.append(g)
for h in files2:
    filelist.append(h)

#converts list to sting
email = MIMEMultipart()

email['From'] = fromaddress
email['To'] = ",".join(toaddress)
#subject line
email['Subject'] = "Subject line"                              # change this
#stuff you want in the body
body = "Stuff you want in the body"                            # Change this

email.attach(MIMEText(body, 'plain'))
for file in filelist:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
    email.attach(part)


#connects to smtp server on port 587
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#logs into gmail account
server.login("account username", "password")                              # insert your username and password for your gmail account.
text = email.as_string()
server.sendmail(fromaddress, toaddress, text)
server.quit()




#deletes files from specific folder after emailing them
folder = 'C:\\Random file location'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
