from django.http import JsonResponse
from .models import Skill, Candidate, Job
from .serializers import CandidateSerializer


def get_candidates(request):
    params = request.GET.get("title")
    candidates = (
        Candidate.objects.all()
        if params == None
        else Candidate.objects.filter(title__contains=params)
    )

    serializer = CandidateSerializer(candidates, many=True)
    return JsonResponse(serializer.data, safe=False)
