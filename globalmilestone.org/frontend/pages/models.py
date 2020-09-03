from django.db import models

# Create your models here.

class Tutor(models.Model):
    first_name = models.CharField(max_length = 100, default = "")
    last_name = models.CharField(max_length = 100, default = "")
    contact_email = models.EmailField(default = "")
    age = models.IntegerField(default = 1)
    us_grade = models.IntegerField(default = 1 )
    slack_email = models.EmailField(default = "")
    gclass_email = models.EmailField(default = "")
    teaching_hours = models.TextField(default = "")
    prep_hours = models.TextField(default = "")
    cs_hours_sem = models.IntegerField(default = 0)
    course_assignment_code  = models.CharField(max_length = 1000, default = "")
    tutoring_history = models.TextField(default = "")
    attendance_record = models.TextField(default = "")
    admin_extra = models.TextField(default = "")
    random_id = models.CharField(default = "", max_length = 100)
    dev_type = "use_backend"
    def __str__(self):
        return "Tutor"+str(self.first_name)+str(self.last_name)+str(self.random_id)
    class Meta:
        managed = False
        db_table = 'standard_tutor'


class WebPage(models.Model):
    dev_type = "use_frontend"
    name = models.CharField(default = "", max_length = 100)
    link = models.CharField(default = "", max_length = 100)
    def __str__(self):
        return "WebPage" + str(self.name)

class WebSection(models.Model):
    dev_type = "use_frontend"
    parent_section = models.ForeignKey('self', on_delete = models.CASCADE, null = True, blank = True)
    parent_page = models.ForeignKey(WebPage, on_delete = models.CASCADE, null = True)
    name = models.CharField(default = "", max_length = 100)
    def __str__(self):
        if self.parent_section:
            return str(self.parent_page.name) + ":" + self.parent_section.__str__().split(":")[1] + "." + str(self.name)
        else:
            return str(self.parent_page.name) + ":" + str(self.name)



class WebText(models.Model):
    dev_type = "use_frontend"
    text_us = models.TextField(default = "")
    text_mx = models.TextField(default = "")
    text_cn = models.TextField(default = "")
    parent_section = models.ForeignKey(WebSection, on_delete = models.CASCADE, null = True)
    parent_page = models.ForeignKey(WebPage, on_delete = models.CASCADE, null = True)
    name = models.CharField(default = "", max_length = 100)
    def __str__(self):
        if self.parent_section:
            return str(self.parent_page.name) +  ":" + self.parent_section.__str__().split(":")[1] + "." + str(self.name)
        else:
            return str(self.parent_page.name) +  ":" + str(self.name)



class WebImg(models.Model):
    dev_type = "use_frontend"
    alt_us = models.CharField(default = "", max_length = 100)
    alt_cn = models.CharField(default = "", max_length = 100)
    alt_mx = models.CharField(default = "", max_length = 100)
    path_to_file = models.CharField(max_length = 100, default = "")
    parent_section = models.ForeignKey(WebSection, on_delete = models.CASCADE, null = True)
    parent_page = models.ForeignKey(WebPage, on_delete = models.CASCADE, null = True)
    name = models.CharField(default = "", max_length = 100)
    def __str__(self):
        return "WebImg" + str(self.name)

class WebInnerLink(models.Model):
    dev_type = "use_frontend"
    parent_section = models.ForeignKey(WebSection, on_delete = models.CASCADE, null = True)
    page = models.ForeignKey(WebPage, on_delete = models.CASCADE, null = True)
    def __str__(self):
        return "Link:" + str(self.parent_section.__str__()) + "->" + str(self.page.__str__())
