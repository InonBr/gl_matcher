import json
from django.http import JsonResponse, HttpResponse
from .models import Skill, Candidate, Job
from .serializers import CandidateSerializer
from django.core.exceptions import BadRequest
from django.db.models import Count


def get_candidates(request):
    params = request.GET.get("title")
    candidates = (
        Candidate.objects.all()
        if params == None
        else Candidate.objects.filter(title__contains=params)
    )

    serializer = CandidateSerializer(candidates, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_candidates_by_skills(request):
    params = request.GET.get("skills")

    if params == None:
        raise BadRequest("Invalid request.")

    params_list = params.replace(" ", "").split(",")

    good_candidates = (
        Candidate.objects.values()
        .filter(skills__name__in=params_list)
        .annotate(matching_skill_count=Count("id"))
        .order_by("-matching_skill_count")
    )

    response_list = list(good_candidates)

    return HttpResponse(json.dumps(response_list), content_type="application/json")
