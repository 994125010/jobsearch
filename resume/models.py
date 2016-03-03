from django.db import models


class Experience(models.Model):
    name = models.CharField(max_length=200, default="EXP")
    desc = models.CharField(max_length=500)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    keywords = models.CharField(max_length=500)
    format_str = "Exp: {0}"

    @property
    def display_date(self):
        return self.end_date.year if self.end_date.year == self.start_date.year \
            else "{0}-{1}".format(self.start_date.year, self.end_date.year)

    @property
    def display_str(self):
        s = self.desc
        for kw in eval(self.keywords):
            s = s.replace(kw, "<strong><code>{0}</code></strong>".format(kw))
        return s

    @property
    def display_name(self):
        return self.name

    def add_keyword(self, kw):
        updated = json.loads(self.keywords)
        updated.append(kw)
        self.keywords = json.dumps(updated)

    def set_keywords(self, kws):
        self.keywords = json.dumps(kws)

    def get_keywords(self):
        return json.loads(self.keywords)
    
    def __str__(self):
        return self.name

class Work(Experience):
    position = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    format_str = "Work: {0}"

    @property
    def display_name(self):
        return self.name+"<br>"+self.position

    @property
    def display_str(self):
        s = self.desc
        for kw in eval(self.keywords):
            s = s.replace(kw, "<strong><code>{0}</code></strong>".format(kw))
        return '<br>'.join(s.split('.'))

class Project(Experience):
    lang = models.CharField(max_length=200)
    format_str = "Proj: {0}"
    lang2suffix = {
        'C': '.c',
        'Java': '.java',
        'Python': '.py',
    }

    @property
    def display_name(self):
        return self.name + self.lang2suffix[self.lang]

class Hobby(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Education(models.Model):
    school = models.CharField(max_length=200)
    major = models.CharField(max_length=500)
    gpa = models.CharField(max_length=3)

    def __str__(self):
        return "{0} (2016) - {1}. (GPA: {2})".format(self.school, self.major, self.gpa)

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
