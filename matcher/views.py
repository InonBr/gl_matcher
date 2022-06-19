from django.http import JsonResponse
from .models import Skill, Candidate, Job
from .serializers import CandidateSerializer


def get_candidates(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    return JsonResponse(serializer.data, safe=False)
