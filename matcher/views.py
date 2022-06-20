import json
from django.http import JsonResponse, HttpResponse
from .models import Skill, Candidate, Job
from .serializers import CandidateSerializer
from django.core.exceptions import BadRequest
from django.db.models import Count


def get_candidates_by_job_id(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        candidates = Candidate.objects.filter(title__icontains=job.title)

        serializer = CandidateSerializer(candidates, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Job.DoesNotExist:
        print("Job matching query does not exist")
        raise BadRequest("Job matching query does not exist")


def get_candidates_by_skills(request, job_id):
    skills = Skill.objects.filter(job=job_id)

    candidates = (
        Candidate.objects.values()
        .filter(skills__id__in=skills)
        .annotate(matching_skill_count=Count("id"))
        .order_by("-matching_skill_count")
    )

    good_candidates_list = list(candidates)

    return HttpResponse(
        json.dumps(good_candidates_list), content_type="application/json"
    )
