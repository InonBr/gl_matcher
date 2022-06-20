import json
from django.http import JsonResponse, HttpResponse
from .models import Skill, Candidate, Job
from .serializers import CandidateSerializer
from django.core.exceptions import BadRequest
from django.db.models import Count


def get_candidates(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        candidates = Candidate.objects.filter(title__contains=job.title)

        serializer = CandidateSerializer(candidates, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Job.DoesNotExist:
        print("Job matching query does not exist")
        raise BadRequest("Job matching query does not exist")


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
