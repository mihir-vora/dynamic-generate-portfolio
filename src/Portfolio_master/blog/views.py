from django.shortcuts import render, redirect
from .models import Project,Skill, Tag, Message,Endorsements,Comment
from .forms import (ProjectForm, 
                    MessageForm,
                    SkillForm,EndorsementsForm,CommentForm,QuestionForm)
# importing message module
from django.contrib import messages
# Create your views here.

def homePage(request):
    project = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body='')
    otherskill = Skill.objects.filter(body='')
    endorsement = Endorsements.objects.filter(approved=True)

    item_name = request.GET.get('get_item')

    if item_name != '' and item_name is not None:
        project = project.filter(title__icontains=item_name)

    form  = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Message Was Successfully Send")
            form = MessageForm()
    else:
        form = MessageForm()

    message = Message.objects.all()


    context = {
        'project' : project,
        'otherskill' : otherskill,
        'detailedSkills': detailedSkills,
        'form' : form,
        'message' : message,
        'endorsement' : endorsement,
       
    }
    print(context)
    return render(request, 'blog/home.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    # django will use the name of the model in lowercase followedb y _set
    count = project.comment_set.count()
    comments  = project.comment_set.all()

    form = CommentForm()
    if request.method == 'POST':
        form  = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project  = project
            comment.save()
            messages.success(request, 'Thank you, For Your Comments!')
            form = CommentForm()
    else:
        form = CommentForm()

    context = {
        'project':project,
        'comments': comments,
        'count':count,
       'form' : form, 
    }
    return render(request, 'blog/project.html', context)


def addProject(request):

    # creating instance of class
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()

    context = {
        'form': form,
    }
    return render(request, 'blog/add-project.html', context)

# edit project
def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
    }
    return render(request, 'blog/edit-project.html', context)


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    # unreading message count
    unreadmessageCount = Message.objects.filter(is_read=False).count() 
    context = {
        'inbox' : inbox,
        'unreadmessageCount' : unreadmessageCount,
    }
    return render(request, 'blog/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {
        'message' : message
    }

    return render(request, 'blog/message.html', context)


def addSkill(request):
    # creating the form instance
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Skill Are Added Successfully')
            form = SkillForm()
    else:
        form = SkillForm()
    context = {
        'form' : form,
    }
    return render(request, 'blog/add-skill.html', context)

def addEndorsements(request):
    form = EndorsementsForm()
    if request.method == "POST":
        form = EndorsementsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank You,your EndorsementsForm was Successfully added!")
            return redirect('home')
            form = EndorsementsForm()
    else:
        form = EndorsementsForm() 
    context = {
        'form ': form,
    }
    return render(request, 'blog/add-endorsements.html', context)


def chartPage(request):

    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "Thanks For Your Voting...")
            return redirect('chartPage')
            form = QuestionForm()
    else:
        form = QuestionForm()

    context = {
        'form' : form,
    }
    return render(request, 'blog/chart.html', context)

