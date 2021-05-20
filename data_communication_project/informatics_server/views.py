from django.shortcuts import render,redirect
from .models import Team,FTPFileHandler,TeamMember,CloudRepositoryHandler,Repo, ForumPost
from django.contrib.auth.decorators import login_required
from  .forms import UploadFileForm,UploadToCloudForm,BlogForm,ForumsForm
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings



#display the teams 
def home(request):
	#get the teams 
	teams = Team.objects.all()

	return render(request, 'informatics_server/home.html',{'teams':teams})


#display the forums
@login_required
def forums(request):

	team_member  = TeamMember.objects.get()
	team = team_member.team

	private_forums = ForumPost.objects.filter(team = team,is_public='NO')

	public_forums = ForumPost.objects.filter(is_public='YES')

	if request.method == 'POST':
		form = ForumsForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			post = form.cleaned_data['post']
			forum_post = ForumPost.objects.create(member=team_member,team = team)

			forum_post.title = title
			forum_post.issue = post
			#forum_post.team = team
			#forum_post.member = team_member
			forum_post.is_public = "YES"

			forum_post.save()


	else:
		form = ForumsForm()

	return render(request, 'informatics_server/forums.html',{'private_fs':private_forums,'public_fs':public_forums,'form':form})


#display the repository
@login_required
def repository(request):

	team_member  = TeamMember.objects.get()
	team = team_member.team
	repo = Repo.objects.get(team= team)

	repo_uri = ""
	backup_uri = ""
	repo_handler = CloudRepositoryHandler()
	if repo.downloadToken1 != "0":
		repo_uri, backup_uri = repo_handler.getRepositoryVersion(team.team_name,"repo-"+team.team_name,repo.downloadToken1,repo.downloadToken2)


	if request.method == 'POST':
		form = UploadToCloudForm(request.POST,request.FILES)
		if form.is_valid():
			filenames = request.FILES['file']
			

			name = request.FILES['file'].name

			path = default_storage.save('tmp/' + name, ContentFile(filenames.read()))

			repo_name = team.team_name
			name = "repo-" + repo_name
			
			token1 , token2 = repo_handler.uploadRepository(repo_name,name,path)

			repo.downloadToken1 = token1
			repo.downloadToken2 = token2
			repo.save()

	else:
		form = UploadToCloudForm()



	return render(request, 'informatics_server/repository.html',{'form': form ,"repo_uri":repo_uri,"backup_uri":backup_uri})


#Add the team blog
@login_required
def blog(request):
	team_member  = TeamMember.objects.get()
	team = team_member.team

	if request.method == 'POST':
		form  = BlogForm(request.POST)
		if form.is_valid():
			blog = form.cleaned_data['blog']
			team.teams_blog = blog
			team.save()
			return redirect('informatics-home')
	else:
		form = BlogForm()

	return render(request, 'informatics_server/blog.html',{'form':form})

@login_required
def managesite(request):

	team_member  = TeamMember.objects.get()
	team = team_member.team

	fileHandler = FTPFileHandler()
	
	team_files = fileHandler.getFiles(team.team_name)

	print(team_files)

	if request.method == 'POST':
		form = UploadFileForm(request.POST,request.FILES)
		if form.is_valid():
			filenames = request.FILES['file']
			

			name = request.FILES['file'].name

			path = default_storage.save('tmp/' + name, ContentFile(filenames.read()))

			site_folder = team.team_name
			
			fileHandler.placeFile(site_folder,name,path)
			team.team_website_url = 'http://localhost/' + site_folder + '/'

			team.save()

	else:
		form = UploadFileForm()

	return render(request, 'informatics_server/managesite.html',{'form':form,'files':team_files})






