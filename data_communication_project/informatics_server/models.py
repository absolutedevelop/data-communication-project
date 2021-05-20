from django.db import models
from django.contrib.auth.models import User
from ftplib import FTP
import io
import pyrebase


class Team(models.Model):

	team_number = models.IntegerField()
	team_name = models.TextField()
	teams_blog = models.TextField()
	team_website_url = models.TextField()


class Repo(models.Model):
	downloadToken1 = models.TextField()
	downloadToken2 = models.TextField()
	team = models.ForeignKey(Team, on_delete=models.CASCADE)



class TeamMember(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	student_number = models.CharField(max_length =100)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)


class ForumPost(models.Model):
	title = models.TextField()
	issue = models.TextField()
	is_public = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	member= models.ForeignKey(TeamMember, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	

class FTPFileHandler():

	def __init__(self):
		self.username = 'testuser'
		self.password = 'mathalefortuneF5!'
		self.ftp = FTP('localhost')
		self.ftp.login(user=self.username, passwd=self.password)
		self.ftp.cwd('/html')
		#self.ftp.dir()

	def placeFile(self,webdir,name,filename):
		#self.ftp.mkd(webdir)
		if webdir not in self.ftp.nlst():
			self.ftp.mkd(webdir)
		self.ftp.cwd(webdir)
		self.ftp.storbinary('STOR ' + name, open(filename,'rb'))
		self.ftp.quit()

	def getFiles(self,team_dir):
		files = []
		if team_dir in self.ftp.nlst():
			self.ftp.cwd(team_dir)
			for file in self.ftp.nlst():
				files.append(file)
			return files 

		return None


class CloudRepositoryHandler():

	def __init__(self):
		self.config = {
		  "apiKey": "AIzaSyAYWh0vRFJlHH0gRpefrvhpgvYUHp5noiI",
		  "authDomain": "data-com-4536a.firebaseapp.com",
		  "projectId": "data-com-4536a",
		  "storageBucket": "data-com-4536a.appspot.com",
		  "messagingSenderId": "42603225736",
		  "appId": "1:42603225736:web:d3f8c3fce291badafe353d",
		  "measurementId": "G-B28QGFWPM6",
		  "databaseURL": ""
		}

		self.response1 = None
		self.response2 = None

		self.firebase  = pyrebase.initialize_app(self.config)
		self.storage = self.firebase.storage()


	def uploadRepository(self,team_name, filename , file_path):
				
		path_on_cloud = team_name + "/" + filename
		path_on_cloud_backup = team_name + "/" + "backup-" + filename
		path_local = file_path

		self.response1  = self.storage.child(path_on_cloud).put(path_local)	
		self.response2 = self.storage.child(path_on_cloud_backup).put(path_local)
		print(self.response1)
		return self.response1.get('downloadTokens'), self.response2.get('downloadTokens')


	def getRepositoryVersion(self,team_name, filename,token1,token2):
		path_on_cloud = team_name + "/" + filename
		path_on_cloud_backup = team_name + "/" + "backup-" + filename

		repo = self.storage.child(path_on_cloud).get_url(token1)
		repo_backup = self.storage.child(path_on_cloud).get_url(token2)

		return repo, repo_backup










