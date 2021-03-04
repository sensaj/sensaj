from django.shortcuts import render
from .models import Project, Screenshots
# Create your views here.


def homepage(request):
    projects = Project.objects.all()
    return render(request, 'homepage/homepage.html', {'projects': projects})


def viewProject(request, id):
    template = "projectpage/view-project.html"
    project = Project.objects.filter(id=id)
    screenshots = Screenshots.objects.filter(project=id)
    clasName = ""
    for proj in project:
        className = prepareClassName(proj.projectBusiness.status)

    context = {"projectDescriptions": project,
               "screenshots": screenshots, "className": className}
    return render(request, template, context)


def viewProfile(request, whichPage):
    template = "myProfile/myProfile.html"
    context = {"whichPage": whichPage}
    return render(request, template, context)


def prepareClassName(status):
    if status == "Not for sale":
        return "text-danger"
    elif status == "on sale":
        return "text-primary"
    else:
        return "text-success"
