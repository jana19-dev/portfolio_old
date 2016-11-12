from django.shortcuts import render
import requests
import json
from collections import OrderedDict

def custom_404(request):
    return render(request, 'portfolio/404.html', {}, status=404)

def custom_400(request):
    return render(request, 'portfolio/400.html', {}, status=400)

def custom_500(request):
    return render(request, 'portfolio/500.html', {}, status=500)


def index(request):
    context = {}
    context['CORE_PROGRAMMING_SKILLS'] = requests.get("https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/programming_skills.json").json()["Programming"]
    context['WEB_FRAMEWORK_SKILLS'] = requests.get("https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/programming_skills.json").json()["Framework"]
    context['TECHNICAL_KNOWLEDGE'] = requests.get("https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/knowledge.json").json()["Technical_Knowledge"]
    context['EDUCATIONAL_KNOWLEDGE'] = requests.get("https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/knowledge.json").json()["Educational_Knowledge"]
    context['LANGUAGE_SKILLS'] = requests.get("https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/knowledge.json").json()["Language"]
    context['EDUCATION'] = requests.get("https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/knowledge.json").json()["Education"]

    context['EXPERIENCE'] = sorted(requests.get("https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/work_experience.json").json().items())

    context['PROJECTS'] = _get_projects()
    return render(request, 'portfolio/index.html', context)


def project(request, project_name):
    context = {}
    context['PROJECT'] = [item for item in _get_projects() if item['id'] == project_name][0]
    pos = _get_projects().index(context['PROJECT'])
    if pos == len(_get_projects())-1:
        context['NEXT'] = False
    else:
        context['NEXT'] = _get_projects()[pos + 1]
    if pos == 0:
        context['PREV'] = False
    else:
        context['PREV'] = _get_projects()[pos - 1]

    return render(request, 'portfolio/single_project.html', context)


def _get_projects():
    return [
        {'name': 'Personal Budget',
         'id': 'budget',
         'subtitle': 'Owner, Web Developer, Graphic Designer',
         'class': 'item applications design',
         'pics': ['https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/budget0.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/budget1.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/budget2.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/budget3.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/budget4.PNG'],
         'description': 'Created a Personal Budget web application. Features adding monthly budgets and carry forwarding,'
                        ' adding daily trasactions and transfers, viewing reports in any date range and adding multiple'
                        ' financial accounts and cash accounts. I made this while learning Django framework as to test '
                        'my knowledge and get comfortable with the framework. This is mainly focused to be used at home for '
                        'personal simple budgeting needs. Check out more of the functions by logging in with the demo '
                        'credentials. Username: piedpiper, Passwrod: johncena. The site is hosted with Heroku. ',
         'duration': 'MAY 2016 - JUN 2016',
         'website': 'https://personal-budget.herokuapp.com/',
         'skills': 'PYTHON, DJANGO, JAVASCRIPT, JQERY, CSS-Bootstrap, Heroku, GIT'},

        {'name': 'Zodus Jobs (DISCONTINUED)',
         'id': 'zodus',
         'subtitle': 'Owner, Web Developer, Graphic Designer',
         'class': 'item applications design',
         'pics': ['https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/zodus0.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/zodus1.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/zodus2.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/zodus3.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/zodus4.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/zodus5.PNG'],
         'description': 'Created a Job Board website. Features candidate and employer dashboards, job posting & '
                        'resume pricing plans and front-end job & resume submissions.',
         'duration': 'JUN 2015 - JUN 2016',
         'skills': 'HTML, CSS, PHP, WORDPRESS, MYSQL, ADOBE FIREWORKS, GOOGLE API, SOCIAL MEDIA'},

        {'name': 'LionKingLimo',
         'id': 'lionkinglimo',
         'subtitle': 'Web Developer, Graphic Designer',
         'class': 'item websites design',
         'pics': ['https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/lionkinglimo0.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/lionkinglimo1.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/lionkinglimo2.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/lionkinglimo3.PNG'],
         'description': 'Created a website for a Taxi/Limo company. Features responsive content, online booking and '
                        'newsletter enrollment.',
         'duration': 'MAY 2016 - JUN 2016',
         'website': 'http://lionkinglimo.com/',
         'skills': 'HTML, CSS, PHP, ADOBE FIREWORKS'},

        {'name': 'The House of Pizzeria (DISCONTINUED)',
         'id': 'pizzeria',
         'subtitle': 'Web Developer, Graphic Designer',
         'class': 'item websites design',
         'pics': ['https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/pizzeria0.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/pizzeria1.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/pizzeria2.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/pizzeria3.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/pizzeria4.PNG'],
         'description': 'Created a website for a restaurant. Features responsive content, online ordering system, '
                        'online reservations, interactive food menu and carrousel gallery. The website was created '
                        'using WordPress. I designed the restaurant logo and the food menu board. Also created fliers'
                        ' and banners using Adobe Fireworks. The project was discontinued on Jan 2016.',
         'duration': 'MAR 2015 - MAY 2015',
         'skills': 'HTML, CSS, PHP, WORDPRESS, MYSQL, ADOBE FIREWORKS, GOOGLE API, SOCIAL MEDIA'},

        {'name': 'HiTech Bay',
         'id': 'hitech',
         'subtitle': 'EBay Store Designer',
         'class': 'item design',
         'pics': ['https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/hitech0.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/hitech1.PNG'],
         'description': 'Created a new Ebay HTML store template for the company.',
         'duration': 'MAY 2014 - JAN 2015',
         'website': 'http://stores.ebay.com/TechGiaant',
         'skills': 'HTML, CSS, JAVASCRIPT, ADOBE FIREWORKS, GOOGLE API, SEARCH ANALYTICS'},

        {'name': 'North York Senior Centre',
         'id': 'nysc',
         'subtitle': 'Owner, Software Developer, Volunteer',
         'class': 'item applications',
         'pics': ['https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/nysc0.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/nysc1.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/nysc2.PNG',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/nysc3.PNG'],
         'description': 'Developed an online registration service for the North York Senior’s Centre, with both user '
                        'and administrative functionalities as a part of a group project during university. '
                        'Implementing agile techniques with extensive documentation of source code, design decisions, '
                        'test strategies, team workflow, and client communication.',
         'duration': 'SEP 2013 - DEC 2013',
         'website': 'http://csc301h-fall2013.github.io/nysc-membership/',
         'skills': 'RUBY ON RAILS, HTML, CSS, BOOTSTRAP, AGILE, SCRUM, PAIR PROGRAMMING, TEAM WORK'},

        {'name': 'Battle Ship Game',
         'id': 'battle',
         'subtitle': 'Game Developer',
         'class': 'item game',
         'pics': ['https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/battle0.png',
                  'https://dl.dropboxusercontent.com/u/11206072/jana19/static/portfolio/images/battle1.png'],
         'description': 'Created the classic game BattleShip as part of a course assignment.',
         'duration': 'OCT 2012 - NOV 2012',
         'skills': 'PYTHON, PAIR PROGRAMMING, TEAM WORK'},

    ]