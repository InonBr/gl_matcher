from django.contrib import admin
from .models import Skill, Candidate, Job

admin.site.register([Skill, Candidate, Job])
