from ftplib import FTP

class FTPFileHandler():

	def __init__(self):
		self.username = 'testuser'
		self.password = 'mathalefortuneF5!'
		self.ftp = FTP('localhost')
		self.ftp.login(user=username, passwd=password)
		self.ftp.cwd('/html')

	def placeFile(self,webdir, filenames):
		self.ftp.mkd(webdir)
		self.ftp.cwd(webdir)
		for filename in filenames:
			self.ftp.storbinary('STOR ' + filename, open(filename,'rb'))
		self.ftp.quit()

#username = 'testuser'
#password = 'mathalefortuneF5!'

#ftp = FTP('localhost')

#ftp.login(user=username, passwd=password)
#ftp.cwd('/html')
#ftp.dir()  # List the files in the user's home directory

#myfiles = ['test.txt','test2.txt']
#website_dir = "team1"
#def placeFile(webdir, filenames):
#	filename="test.txt"
#	ftp.mkd(webdir)
#	ftp.cwd(webdir)
#	for filename in filenames:
#		ftp.storbinary('STOR ' + filename, open(filename,'rb'))
#	ftp.quit()

#placeFile(website_dir,myfiles)


















