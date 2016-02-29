from django.db import models


class Experience(models.Model):
    name = models.CharField(max_length=200, default="EXP")
    desc = models.CharField(max_length=500)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    keywords = models.CharField(max_length=500)
    format_str = "Exp: {0}"

    def add_keyword(self, kw):
        updated = json.loads(self.keywords)
        updated.append(kw)
        self.keywords = json.dumps(updated)

    def set_keywords(self, kws):
        self.keywords = json.dumps(kws)

    def get_keywords(self):
        return json.loads(self.keywords)
    
    def __str__(self):
        return self.format_str.format(self.name)

class Work(Experience):
    position = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    format_str = "Work: {0}"

class Project(Experience):
    lang = models.CharField(max_length=200)
    format_str = "Proj: {0}"

class Hobby(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return "Hobby: "+self.name

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Course: "+self.name
