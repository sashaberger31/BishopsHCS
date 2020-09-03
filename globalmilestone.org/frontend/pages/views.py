from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from pages.models import Tutor, WebText, WebPage, WebImg, WebSection, WebInnerLink
import sys
# Create your views here.

def us(request):

	try:
		# Collect the content for the "landing" section
		landing_section = WebSection.objects.get(name = "Landing")
		landing_fields = WebText.objects.filter(parent_section = landing_section)
		landing_title = landing_fields.get(name = "Title")
		landing_subtitle = landing_fields.get(name = "Subtitle")

		context = {
			'LandingTitle' : landing_title.text_us,
			'LandingSubtitle': landing_subtitle.text_us
		}
	except:
		context = {
			'LandingTitle' : "Contact the webmaster.",
			'LandingSubtitle': "Contact the webmaster."
		}

	try:
		# Collect the content for the "mission" section
		mission_section = WebSection.objects.get(name = "Mission")
		mission_subsections_qset = WebSection.objects.filter(parent_section = mission_section)
		mission_subsection_text = []
		mission_subsection_title = []
		for i in range(1, 4):
			curr_parent_section = mission_subsections_qset.get(name = ("Column"+str(i)))
			mission_subsection_title.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Title").text_us)
			mission_subsection_text.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Text").text_us)
			context['MissionSubsectionText'+str(i)] = mission_subsection_text[i-1]
			context['MissionSubsectionTitle'+str(i)] = mission_subsection_title[i-1]


	except:
		context = {
			'MissionSubsectionText1' : "Contact the webmaster.",
			'MissionSubsectionText2' : 'Contact the webmaster.',
			'MissionSubsectionText3' : 'Contact the webmaster.',
			'MissionSubsectionTitle1' : 'Contact the webmaster.',
			'MissionSubsectionTitle2' : 'Contact the webmaster.',
			'MissionSubsectionTitle3' : 'Contact the webmaster.'
		}

	try:
		# Collect the content for the "how it works" section
		works_section = WebSection.objects.get(name = "Works")
		works_subsections_qset = WebSection.objects.filter(parent_section = works_section)
		works_subsection_text = []
		works_subsection_title = []
		for i in range(1, 4):
			curr_parent_section = works_subsections_qset.get(name = ("Column"+str(i)))
			works_subsection_title.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Title").text_us)
			works_subsection_text.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Text").text_us)
			context['WorksSubsectionText'+str(i)] = works_subsection_text[i-1]
			context['WorksSubsectionTitle'+str(i)] = works_subsection_title[i-1]


	except:
		context = {
			'WorksSubsectionText1' : "Contact the webmaster.",
			'WorksSubsectionText2' : 'Contact the webmaster.',
			'WorksSubsectionText3' : 'Contact the webmaster.',
			'WorksSubsectionTitle1' : 'Contact the webmaster.',
			'WorksSubsectionTitle2' : 'Contact the webmaster.',
			'WorksSubsectionTitle3' : 'Contact the webmaster.'
		}


	#try:
	# Collect data for the "find out more" section.
	more_section = WebSection.objects.get(name = "More")
	context["MoreHeaderText"] = WebText.objects.get(parent_section = more_section).text_us

	more_wrappers = []
	for i in range(1,4):
		more_wrappers.append(WebSection.objects.filter(parent_section = more_section).get(name = "Button"+str(i)))

	more_links = ["https://globalmilestone.org/us/" + str(WebInnerLink.objects.get(parent_section = wrapper).page.link) for wrapper in more_wrappers]
	more_texts = [str(WebText.objects.get(parent_section = wrapper).text_us) for wrapper in more_wrappers]

	for i in range(1,4):
		context["MoreText" + str(i)] = more_texts[i-1]
		context["MoreLink" + str(i)] = more_links[i-1]

#except:
	"""
	context['MoreHeaderText'] = "Contact the webmaster."
		context['MoreText1'] = "Contact the webmaster."
		context['MoreLink1'] = '##',
		context['MoreText2'] = 'Contact the webmaster.'
		context['MoreLink2'] = '##'
		context['MoreText3'] = 'Contact the webmaster.'
	context['MoreLink3'] = '##'
	"""

	response = render(request, "index.html", context)
	response["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
	response["Pragma"] = "no-cache" # HTTP 1.0.
	response["Expires"] = "0" # Proxies.
	return response
def mx(request):
	return HttpResponse('hola')
def cn(request):
	return HttpResponse('ni hao')

def enroll_us(request):

	response = render(request, "sub/enroll.html")
	response["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
	response["Pragma"] = "no-cache" # HTTP 1.0.
	response["Expires"] = "0" # Proxies.
	return response

def about_us(request):
	response = render(request, "sub/become_student.html")
	response["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
	response["Pragma"] = "no-cache" # HTTP 1.0.
	response["Expires"] = "0" # Proxies.
	return response

def tutor_us(request):
	response = render(request, "sub/become_student.html")
	response["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
	response["Pragma"] = "no-cache" # HTTP 1.0.
	response["Expires"] = "0" # Proxies.
	return response

def fallback(request):
	return redirect('/us')
