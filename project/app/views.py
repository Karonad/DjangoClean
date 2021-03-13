from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Fruits, Contact, Cv, Hobby, Skill, Experience, Formation
from app.forms import ContactForm, CvForm
import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.
def index(request):
    test = 'wesh'
    fruits = Fruits.objects.all()
    return render(request, 'app/index.html', {'fruits': fruits})


def contact(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                mail = form.cleaned_data['mail'],
                name = form.cleaned_data['name'],
                message = form.cleaned_data['message'],
            )
            msg_plain = ''
            msg_html = render_to_string('app/emails/welcome.html', {'name': form.cleaned_data['name']})
            objet = "Message bien recu " + form.cleaned_data['name'] + " !"
            send_mail(
                objet,
                msg_plain,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['mail']],
                html_message=msg_html,
            )
            form = ContactForm()
    return render(request, 'app/contact.html', {'form': form})

def cv(request):
    cvs = Cv.objects.all()
    return render(request, 'app/cv/index.html', {'cvs': cvs})

def cv_ajout(request):

    if request.method == "GET":
        form = CvForm()
    else:
        form = CvForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['permis'] == 1:
                permis = True
            else: 
                permis = False
            # save cv
            new_cv = Cv(
                lastname = form.cleaned_data['lastname'],
                firstname = form.cleaned_data['firstname'],
                mail = form.cleaned_data['mail'],
                phone_number = form.cleaned_data['phone_number'],
                city = form.cleaned_data['city'],
                sector = form.cleaned_data['sector'],
                age = form.cleaned_data['age'],
                permis = permis,
            )
            new_cv.save()
            # save hobby
            for item in request.POST.getlist('hobby[]'):
                if len(item) > 0:
                    hobby = Hobby(
                        name = item,
                        cv = new_cv,
                    )
                    hobby.save()
            # save Skill
            i = 0
            while i <= 5:
                skill = 'skill[' + str(i) + ']'
                level = 'level[' + str(i) + ']'
                skill = request.POST.get(skill)
                level = request.POST.get(level)

                if skill != '' and level != 3:
                    Skill.objects.create(
                        name = skill,
                        level = level,
                        cv = new_cv,
                    )
                i += 1
            # save Exp
            j = 0
            while j <= 2:
                exp_title = 'exp_title[' + str(j) + ']'
                exp_content = 'exp_content[' + str(j) + ']'
                exp_start = 'exp_start[' + str(j) + ']'
                exp_end = 'exp_end[' + str(j) + ']'
                exp_title = request.POST.get(exp_title)
                exp_content = request.POST.get(exp_content)
                exp_start = request.POST.get(exp_start)
                exp_end = request.POST.get(exp_end)
    
                if len(exp_title) > 0 and len(exp_content) > 0 and len(exp_start) > 0 and len(exp_end) > 0:
                    Experience.objects.create(
                        title = exp_title,
                        content = exp_content,
                        start_at = exp_start,
                        end_at = exp_end,
                        cv = new_cv,
                    )
                j += 1
            # save Formation
            k = 0
            while k <= 2:
                exp_title = 'exp_title[' + str(k) + ']'
                exp_content = 'exp_content[' + str(k) + ']'
                exp_start = 'exp_start[' + str(k) + ']'
                exp_end = 'exp_end[' + str(k) + ']'
                exp_title = request.POST.get(exp_title)
                exp_content = request.POST.get(exp_content)
                exp_start = request.POST.get(exp_start)
                exp_end = request.POST.get(exp_end)
    
                if len(exp_title) > 0 and len(exp_content) > 0 and len(exp_start) > 0 and len(exp_end) > 0:
                    Formation.objects.create(
                        title = exp_title,
                        content = exp_content,
                        start_at = exp_start,
                        end_at = exp_end,
                        cv = new_cv,
                    )
                k += 1
            
        else:
            print(form.errors)      

            form = CvForm()

    return render(request, 'app/cv/ajout.html')

def cv_show(request, id=None):
    records = {}
    cv = Cv.objects.get(id= id)
    if cv:
        records['cv'] = cv
    hobbies = Hobby.objects.all().filter(cv= id)
    if hobbies:
        records['hobbies'] = hobbies
    skills = Skill.objects.all().filter(cv_id= id)
    if skills:
        records['skills'] = skills
    experiences = Experience.objects.all().filter(cv_id= id)
    if experiences:
        records['experiences'] = experiences
    formations = Formation.objects.all().filter(cv_id= id)
    if formations:
        records['formations'] = formations
    return render(request, 'app/cv/show.html', {'records': records})
