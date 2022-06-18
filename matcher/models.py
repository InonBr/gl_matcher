from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return {"name": self.name, "title": self.title}

class Job (models.Model):
    title = models.CharField(max_length=300)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title