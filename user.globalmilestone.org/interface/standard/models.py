from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student (models.Model):
	# Identity and Contact Info
	first_name = models.CharField(max_length = 100, default = "")
	last_name = models.CharField(max_length = 100, default = "")
	age = models.IntegerField(default = 1)
	grade = models.IntegerField(default = 1)
	gclass_name = models.CharField(max_length = 100, default = "")
	contact_email = models.EmailField(default = "")
	student_email = models.EmailField(default = "")
	gclass_email = models.EmailField(default = "")
	student_id = models.CharField(default = "", max_length = 100)

	# Academic Information
	placement_code = models.CharField(max_length = 1000, default = "")
	courses_enrolled = models.CharField(max_length = 1000, default = "")
	academic_comment = models.TextField(default = "")

	# Attendance and Behavioral
	behavioral_comment = models.TextField(default = "")
	misc_comment = models.TextField(default = "")
	attendance_record = models.TextField(default = "")
	academic_record = models.TextField(default = "")
	behavioral_record = models.TextField(default = "")
	admin_extra = models.TextField(default = "")

	def __str__(self):
		return str(self.first_name)+str(self.last_name)+str(self.student_id)

class Tutor(models.Model):
	# Identity
	random_id = models.CharField(default = "", max_length = 100)
	first_name = models.CharField(max_length = 100, default = "")
	last_name = models.CharField(max_length = 100, default = "")
	age = models.IntegerField(default = 1)
	us_grade = models.IntegerField(default = 1)

	# Contact
	contact_email = models.EmailField(default = "")
	slack_email = models.EmailField(default = "")
	gclass_email = models.EmailField(default = "")

	# Service Hours
	teaching_hours = models.TextField(default = "")
	prep_hours = models.TextField(default = "")
	hours_sem_total = models.IntegerField(default = 0)

	# Teaching assignments


	# Comments and etc
	tutoring_history = models.TextField(default = "")
	attendance_record = models.TextField(default = "")
	admin_extra = models.TextField(default = "")

	def __str__(self):
		return str(self.first_name)+str(self.last_name)+str(self.random_id)

class PackageCourse(models.Model):
	full_name = models.CharField(max_length = 100, default = "")
	abbrev_name = models.CharField(max_length = 100, default = "")
	def __str__(self):
		return str(self.abbrev_name)

class PackageInstance(models.Model):
	section = models.IntegerField(default = 1)
	parent_package = models.ForeignKey(PackageCourse, on_delete = models.CASCADE, null = True)

	def __str__(self):
		if parent := self.parent_package:
			return parent.__str__() + ":SCT" + str(self.section)

class Course(models.Model):
	full_name = models.CharField(max_length = 100, default = "")
	abbrev_name = models.CharField(max_length = 100, default = "")
	parent_package = models.ForeignKey(PackageCourse, on_delete = models.CASCADE, null = True,  blank = True)
	subject_leader = models.ForeignKey(Tutor, on_delete = models.CASCADE, null = True)
	primary_contact = models.EmailField(default = "")
	def __str__(self):
		if parent := self.parent_package:
			return parent.__str__()+ "." + str(self.abbrev_name)
		else:
			return str(self.abbrev_name)

class CourseInstance(models.Model):
	parent_course = models.ForeignKey(Course, on_delete = models.CASCADE, default = "")
	level = models.IntegerField(default = 0)
	section = models.IntegerField(default = 0)
	tutors = models.ManyToManyField(Tutor, null = True)
	students_enrolled = models.ManyToManyField(Student, blank = True)

	def __str__(self):
		return self.parent_course.__str__() + ":SCT" + str(self.section) + ":LVL" + str(self.level)

class Session(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	parent_course_instance = models.ForeignKey(CourseInstance, null = True, on_delete = models.CASCADE)
	tutors = models.ManyToManyField(Tutor, related_name = "sessions_tutoring")
	monitors = models.ManyToManyField(Tutor, related_name = "sessions_monitoring", blank=True)
	students_attending = models.ManyToManyField(Student, related_name = "sessions_attending", blank= True)
	students_attended = models.ManyToManyField(Student, related_name = "sessions_attended", blank = True)
	conducted = models.BooleanField(default = False)
	session_id = models.CharField(default = "", max_length = 100)
	class_report_text = models.TextField(default = "")
	def __str__(self):
		return "Session"+str(self.parent_course_instance)+":"+str(self.session_id)+"@"+str(self.start_time)
