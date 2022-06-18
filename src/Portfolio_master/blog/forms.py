from django.forms import ModelForm
from .models import Project, Message,Skill,Endorsements,Comment,Questions

class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = ['title', 'thumbnail', 'tag', 'body', 'slug']

	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({
				'class' : 'form-group form-control col-md-6 ',
				'placeholder' : 'Project Title',
			})
		self.fields['thumbnail'].widget.attrs.update({
				'class' : 'form-group form-control col-md-6 ',
				'placeholder' : 'Project Image',
			})	
		self.fields['tag'].widget.attrs.update({
				'class' : 'form-group form-control col-md-6',
				'placeholder' : 'Add Technology To develop Project ',
			})
		self.fields['body'].widget.attrs.update({
				'class' : 'form-group form-control col-md-6  ',
				'placeholder' : 'Project Description',
			})
		self.fields['slug'].widget.attrs.update({
				'class' : 'form-group form-control col-md-6',
				'placeholder' : 'Project Url',
			})


class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = '__all__'
		exclude = ['is_read']

	def __init__(self, *args, **kwargs):
		super(MessageForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({
				'class': 'form-group form-control '
			})

		self.fields['email'].widget.attrs.update({
				'class' : 'form-group form-control '
			})

		self.fields['body'].widget.attrs.update({
				'class' : 'form-group form-control '
			})
		self.fields['subject'].widget.attrs.update({
				'class' : 'form-group form-control '
			})
	
class SkillForm(ModelForm):
	class Meta:
		model = Skill
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(SkillForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({
				'class': 'form-group form-control'
			})
		self.fields['image'].widget.attrs.update({
				'class' : 'form-group form-control'
			})
		self.fields['body'].widget.attrs.update({
				'class' : 'form-group form-control'
			})

class EndorsementsForm(ModelForm):
	class Meta:
		model = Endorsements
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(EndorsementsForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({
				'class': 'form-group form-control'
			})
		self.fields['body'].widget.attrs.update({
				'class' : 'form-group form-control'
			})
		
class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'
		exclude =  ['project']

	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({
				'class': 'form-group form-control'
			})
		self.fields['body'].widget.attrs.update({
				'class' : 'form-group form-control'
			})

class QuestionForm(ModelForm):
	class Meta:
		model = Questions
		fields = '__all__'


	def __init__(self, *args, **kwargs):
		super(QuestionForm, self).__init__(*args, **kwargs)
		self.fields['answer'].widget.attrs.update({
				'class' : 'form-group form-control'
			})