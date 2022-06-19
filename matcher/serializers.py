from rest_framework import serializers
from .models import Skill, Candidate, Job


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "name", "title", "skills"]
