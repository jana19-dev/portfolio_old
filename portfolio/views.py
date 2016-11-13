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
    static_url = "https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/"
    SKILLS = requests.get(static_url+"programming_skills.json").json()
    KNOWLEDGE = requests.get(static_url+"knowledge.json").json()
    EXPERIENCE = requests.get(static_url+"work_experience.json").json()
    PROJECT = requests.get(static_url+"projects.json").json()

    context = {}
    context['GENERAL'] = requests.get(static_url+"general_info.json").json()
    context['CORE_PROGRAMMING_SKILLS'] = SKILLS["Programming"]
    context['WEB_FRAMEWORK_SKILLS'] = SKILLS["Framework"]
    context['TECHNICAL_KNOWLEDGE'] = KNOWLEDGE["Technical_Knowledge"]
    context['EDUCATIONAL_KNOWLEDGE'] = KNOWLEDGE["Educational_Knowledge"]
    context['LANGUAGE_SKILLS'] = KNOWLEDGE["Language"]
    context['EDUCATION'] = KNOWLEDGE["Education"]
    context['EXPERIENCE'] = sorted(EXPERIENCE.items())
    context['PROJECTS'] = sorted(PROJECT.items())
    context['FILTERS'] = []
    for item in PROJECT.values():
        context['FILTERS'] += [x.upper() for x in item["skills"].strip().split(' ')]
    context['FILTERS'] = sorted(list(set(context['FILTERS'])))

    return render(request, 'portfolio/index.html', context)


def project(request, project_name):
    context = {}
    static_url = "https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/"
    PROJECTS = sorted(requests.get(static_url+"projects.json").json().items())
    context['PROJECT'] = [item for item in PROJECTS if item[1]['id'] == project_name][0]
    pos = PROJECTS.index(context['PROJECT'])
    if pos == len(PROJECTS)-1:
        context['NEXT'] = False
    else:
        context['NEXT'] = PROJECTS[pos + 1]
    if pos == 0:
        context['PREV'] = False
    else:
        context['PREV'] = PROJECTS[pos - 1]

    return render(request, 'portfolio/single_project.html', context)
