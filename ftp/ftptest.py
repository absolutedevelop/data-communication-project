from ftplib import FTP

username = 'testuser'
password = 'mathalefortuneF5!'


with FTP('localhost') as ftp:
    ftp.login(username, password)

    ftp.cwd('/fortuwebsite.com/public_html')


    

    ftp.dir()  # List the files in the user's home directory

def gradFile():
	filename = "test.txt"
	file = open(filename,'wb')
	ftp.retrbinary('RETR' + filename,file.write,1024)
	ftp.quit()
	file.close()











