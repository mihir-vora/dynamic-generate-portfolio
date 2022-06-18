from django.contrib import admin
from .models import Project, Skill, Tag, Message,Endorsements,Comment,Questions
# Register your models here.

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Message)
admin.site.register(Endorsements)
admin.site.register(Comment)
admin.site.register(Questions)