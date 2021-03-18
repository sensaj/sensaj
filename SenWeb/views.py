import datetime
from django.shortcuts import render
from .models import Project, Screenshots, Reviews
# Create your views here.


def homepage(request):
    projects = Project.objects.all()
    return render(request, 'homepage/homepage.html', {'projects': projects})


def viewProject(request, id):
    template = "projectpage/view-project.html"
    context = projectContext(id)
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


def addComment(request):
    template = "projectpage/view-project.html"
    if request.method == "POST":
        email = request.POST['txtEmail']
        fullName = request.POST['txtName']
        sendNotification = request.POST.getlist('sendNotification')
        comment = request.POST['txtMsg']
        project = Project.objects.get(id=request.POST['project'])
        today = datetime.datetime.now()
        if sendNotification == "on":
            sendNotification = False
        else:
            sendNotification = True
        review = Reviews.objects.create(
            senderEmail=email, fullName=fullName, content=comment, project=project, sendNotification=sendNotification, date=today)
        review.save()
        context = projectContext(request.POST['project'])
        return render(request, template, context)


def projectContext(projectId):
    project = Project.objects.filter(id=projectId)
    screenshots = Screenshots.objects.filter(
        project=projectId)
    reviews = Reviews.objects.filter(
        project=projectId).order_by("-date")[::-1]
    clasName = ""
    context = ""
    for proj in project:
        className = prepareClassName(proj.projectBusiness.status)

    context = {"projectDescriptions": project,
               "screenshots": screenshots, "className": className, "reviews": reviews}
    return context
