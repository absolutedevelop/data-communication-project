from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


class UploadToCloudForm(forms.Form):
    file = forms.FileField()

class BlogForm (forms.Form):
	blog = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":100,'style': 'height: 300px'}))

form_choices  = []

form_choices.append(('YES','public'))
form_choices.append(('NO','private'))


class ForumsForm(forms.Form):
	title = forms.CharField()
	
	post = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":100,'style': 'height: 100px'}))

