from django.shortcuts import render
import requests
import json

def custom_404(request):
    return render(request, 'portfolio/404.html', {}, status=404)

def custom_400(request):
    return render(request, 'portfolio/400.html', {}, status=400)

def custom_500(request):
    return render(request, 'portfolio/500.html', {}, status=500)


def index(request):
#     static_url = "https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/"
#     SKILLS = requests.get(static_url+"programming_skills.json").json()
#     KNOWLEDGE = requests.get(static_url+"knowledge.json").json()
#     EXPERIENCE = requests.get(static_url+"work_experience.json").json()
#     PROJECT = requests.get(static_url+"projects.json").json()
#     INSTAGRAM = requests.get("https://api.instagram.com/v1/users/self/media/recent/?access_token=508727293.1677ed0.69d96553324f4468917af711a368260b&count=16").json()
#     INSTA_PHOTOS = ""
#     for item in (INSTAGRAM["data"]):
#         INSTA_PHOTOS += '<img src="'+item["images"]["standard_resolution"]["url"]+'" alt="'+item["caption"]["text"]+'">'
    

    context = {}
#     context['GENERAL'] = requests.get(static_url+"general_info.json").json()
#     context['CORE_PROGRAMMING_SKILLS'] = SKILLS["Programming"]
#     context['WEB_FRAMEWORK_SKILLS'] = SKILLS["Framework"]
#     context['TECHNICAL_KNOWLEDGE'] = KNOWLEDGE["Technical_Knowledge"]
#     context['EDUCATIONAL_KNOWLEDGE'] = KNOWLEDGE["Educational_Knowledge"]
#     context['LANGUAGE_SKILLS'] = KNOWLEDGE["Language"]
#     context['EDUCATION'] = KNOWLEDGE["Education"]
#     context['EXPERIENCE'] = sorted(EXPERIENCE.items())
#     context['PROJECTS'] = sorted(PROJECT.items())
#     context['FILTERS'] = []
#     for item in PROJECT.values():
#         context['FILTERS'] += [x.upper() for x in item["skills"].strip().split(' ')]
#     context['FILTERS'] = sorted(list(set(context['FILTERS'])))

#     context["INSTA_PHOTOS"] = INSTA_PHOTOS

    return render(request, 'portfolio/index.html', context)
