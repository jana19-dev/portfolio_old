from django.shortcuts import render

def custom_404(request):
    return render(request, 'portfolio/404.html', {}, status=404)

def custom_400(request):
    return render(request, 'portfolio/400.html', {}, status=400)

def custom_500(request):
    return render(request, 'portfolio/500.html', {}, status=500)


def index(request):
    context = {}
    context['CORE_PROGRAMMING_SKILLS'] = _get_programming_skills()
    context['WEB_FRAMEWORK_SKILLS'] = _get_framework_skills()
    context['TECHNICAL_KNOWLEDGE'] = _get_technical_knowledge()
    context['EDUCATIONAL_KNOWLEDGE'] = _get_educational_knowledge()
    context['LANGUAGE_SKILLS'] = _get_language_skill()
    context['EXPERIENCE'] = _get_experience()
    context['EDUCATION'] = _get_education()
    context['PROJECTS'] = _get_projects()
    return render(request, 'portfolio/index.html', context)


def project(request, project_name):
    context = {}
    context['PROJECT'] = [item for item in _get_projects() if item['id']==project_name][0]
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



def _get_experience():
    return [
        {'name': 'LionKingLimo',
         'duration': '2016 MAY - 2016 JUN',
         'position': 'WEB DEVELOPER',
         'description': 'Created a website for a Taxi/Limo company. Features responsive content, online booking and '
                        'newsletter enrollment. The website was created using plain HTML with CSS and PHP for contact '
                        'forms.',
         'icon': 'ion-network',
         'proj_name': 'lionkinglimo',},

        {'name': 'INDIVIDUAL',
         'duration': '2010 OCT - CURRENT',
         'position': 'PRIVATE TUTOR',
         'description': 'Conducting private classes for students in Mathematics. Students from Grades 6 to University '
                        'Level. Helping with homework, assignments and teaching course material.',
         'icon': 'ion-ios-book'},

        {'name': 'Zodus Jobs',
         'duration': '2015 JUN - 2016 JUN',
         'position': 'FOUNDER & WEB DEVELOPER (DISCONTINUED)',
         'description': 'Created a Job Board website. Features candidate and employer dashboards, job posting & resume '
                        'pricing plans with front-end job & resume submissions. The website was created using WordPress. '
                        'The project was discontinued on Jun 2016. Website layouts and functionality can be found under '
                        '"projects" section.',
         'icon': 'ion-flag',
         'proj_name': 'zodus'},

        {'name': 'THE HOUSE OF PIZZERIA',
         'duration': '2015 MAR - 2015 MAY',
         'position': 'WEB DEVELOPER & GRAPHIC DESIGNER (DISCONTINUED)',
         'description': 'Created a website for a restaurant. Features responsive content, online ordering system, '
                        'online reservations, interactive food menu and carrousel gallery. The website was created '
                        'using WordPress. I designed the restaurant logo and the food menu board. Also created fliers'
                        ' and banners using Adobe Fireworks. The project was discontinued on Jan 2016. Website layouts '
                        'and functionality can be found under "projects" section.',
         'icon': 'ion-pizza',
         'proj_name': 'pizzeria'},

        {'name': 'HITECH BAY',
         'duration': '2014 MAY - 2015 JAN',
         'position': 'ONLINE SALES, COMPUTER REPAIR TECHNICIAN, WEB DEVELOPER',
         'description': 'Conducting online sales on e-commerce websites such as Amazon and Ebay. Processing online '
                        'orders and handling shipping. Maintaining store website and Ebay shop templates. Debugging, '
                        'upgrading and repairing computer systems from desktops to laptops. Taking pictures of products'
                        ' and processing through image editing software(Adobe Fireworks). Handling customer inquiries '
                        'in person and via online. During my stay, I introduced an order management system called '
                        'Lynn Works that integrates all selling platforms under a single management unit. I also '
                        'created a new Ebay HTML store template for the company.',
         'icon': 'ion-wrench',
         'proj_name': 'hitech'},

        {'name': 'UNIVERSITY OF TORONTO',
         'duration': '2014 SEP - 2014 DEC',
         'position': 'VOLUNTEER EXPERIENCE - NOTE TAKING',
         'description': 'Contributed to the Accessibility Services Note-Taking Program during my studies. As a '
                        'volunteer note-taker, I attend classes on a regular basis and continue to take lecture notes '
                        'and upload them to the respective department. For more info about the program, click  '
                        'at <a href="http://www.accessibility.utoronto.ca/volunteer-note-taking.htm" target="_blank">here.</a>',
         'icon': 'ion-edit'},

        {'name': 'NORTH YORK SENIOR CENTRE',
         'duration': '2013 SEP - 2013 DEC',
         'position': 'VOLUNTEER EXPERIENCE - SOFTWARE DEVELOPER',
         'description': 'Developed an online registration service for the North York Senior’s Centre, with both user '
                        'and administrative functionalities as a part of a group project during university. '
                        'Implementing agile techniques with extensive documentation of source code, design decisions, '
                        'test strategies, team workflow, and client communication. We used Ruby on Rails as our '
                        'main programming language, HTML, Bootstrap and Agile Programming.',
         'icon': 'ion-code-working',
         'proj_name': 'nysc'},

        {'name': 'TIM HORTONS',
         'duration': '2010 NOV - 2011 APR',
         'position': 'BAKER & CASHIER',
         'description': 'Responsible for baking a variety of products. Interact with customers and handle their concerns '
                        'effectively. Handling cash register transactions. Provide a high standard of customer service.',
         'icon': 'ion-coffee'},
    ]


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


def _get_programming_skills():
    return  [{'name':'Python', 'value': 90}, {'name': 'PHP', 'value': 85}, {'name': 'Haskell', 'value': 85},
             {'name': 'Racket', 'value': 85}, {'name': 'PROLOG', 'value': 80},{'name': 'Java', 'value': 85},
             {'name': 'Ruby', 'value': 80}, {'name': 'C', 'value': 80}, {'name': 'BASH', 'value': 80},
             {'name': 'SQL', 'value': 75}, ]


def _get_framework_skills():
    return [{'name':'HTML & CSS', 'value': 95}, {'name':'PHP Codeigniter', 'value': 90},
            {'name':'Python Django', 'value': 90}, {'name':'Ruby on Rails', 'value': 85},
            {'name':'WordPress', 'value': 90}, {'name':'JQUERY', 'value': 80}, {'name':'Javascript', 'value': 80},
            {'name':'MYSQL', 'value': 75},{'name':'Node JS (learning)', 'value': 50}, {'name':'Angular JS (learning)', 'value': 50}, ]



def _get_technical_knowledge():
    return ['INSTALL AND CONFIGURE','HARDWARE & NETWORKING','WEB USABILITY', 'LOGO DESIGN', 'MS OFFICE ENVIRONMENT',
            'SEARCH ANALYTICS', 'WINDOWS OPERATING SYSTEM', 'LINUX OPERATING SYSTEM','MOBILE APP DESIGN', 'PHOTOGRAPHY',
            'GRAPHICAL DESIGN', 'WEB DEVELOPMENT', 'SEO OPTIMIZATION', 'E-COMMERCE']


def _get_educational_knowledge():
    return  ['COMPUTER NETWORK SYSTEMS', 'DATABASES', 'MACHINE LEARNING', 'DATA MINING', 'SOFTWARE TESTING',
             'NATURAL LANGUAGE', 'OPERATING SYSTEMS', 'AGILE, SCRUM DEVELOPMENT', 'SOFTWARE ENGINEERING',
             'ECONOMICS & SOCIAL NETWORKS', 'NUMERICAL METHODS', 'ALGORITHM DESIGN & ANALYSIS',
             'COMPUTER ORGANIZATION', 'STATISTICAL SCIENCE']


def _get_language_skill():
    return [{'name': 'English Experienced', 'value': 99},
            {'name': 'Tamil Experienced', 'value': 99},
            {'name': 'Sinhala Intermediate', 'value': 65}]

def _get_education():
    return [{'name': "S. THOMAS' COLLEGE", 'type': 'HIGH SCHOOL', 'year': '1997 - 2010',
             'link': 'http://www.stcmount.edu.lk/'},
            {'name': "TURNKEY IT TRAINING", 'type': 'DIPLOMA IN COMPUTER HARDWARE & NETWORKING', 'year': '2006 - 2007',
             'link': 'http://www.turnkey.lk/'},
            {'name': "UNIVERSITY OF TORONTO", 'type': 'BSc in Computer Science', 'year': '2011 - 2016',
             'link': 'http://www.utoronto.ca/'},]