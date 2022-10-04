from django.db import models

# Create your models here.


class ProjectType(models.Model):
    typeName = models.CharField(max_length=20)

    def __str__(self):
        return str(self.typeName)


class ProjectDevelopment(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return str(self.status)


class ProjectBusiness(models.Model):
    status = models.CharField(max_length=30)

    def __str__(self):
        return str(self.status)


class Project(models.Model):
    projectName = models.CharField(max_length=100)
    projectType = models.ForeignKey(
        ProjectType, on_delete=models.DO_NOTHING)
    developmentStatus = models.ForeignKey(
        ProjectDevelopment, on_delete=models.DO_NOTHING)
    projectBusiness = models.ForeignKey(
        ProjectBusiness, on_delete=models.DO_NOTHING)
    projectLink = models.URLField(max_length=500)
    projectDescription = models.TextField(default="")
    projectIcon = models.ImageField(upload_to='projectIcon')
    coverImage = models.ImageField(upload_to='projectCover')

    def __str__(self):
        return str(self.projectName)


class Screenshots(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='projectScreenshots')


class Reviews(models.Model):
    senderEmail = models.EmailField()
    content = models.TextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE)
    date = models.DateField()
    fullName = models.CharField(max_length=100, default="")
    sendNotification = models.BooleanField(default=False)


class EducationLevel(models.Model):
    levelName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.levelName)


class Position(models.Model):
    positionName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.positionName)


class Members(models.Model):
    fullName = models.CharField(max_length=300)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    educationLevel = models.ForeignKey(
        EducationLevel, on_delete=models.DO_NOTHING,)
    skills = models.TextField()
    selfDescription = models.TextField()
    position = models.ForeignKey(
        Position, on_delete=models.DO_NOTHING,)
