from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from pages.models import Tutor, WebText, WebPage, WebImg, WebSection, WebInnerLink
import sys
# Create your views here.
def set_locale (args, code1, code2, text1, text2):
	args['nonlocal1'] = code1
	args['nonlocal2'] = code2
	args['nonlocaltext1'] = text1
	args['nonlocaltext2'] = text2
	args['nonlocallink1'] = 'pages/img/icons/flags/'+code1+'.png'
	args['nonlocallink2'] = 'pages/img/icons/flags/'+code2+'.png'
	return args
def set_http_flags(resp):
	resp["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
	resp["Pragma"] = "no-cache" # HTTP 1.0.
	resp["Expires"] = "0" # Proxies.
	return resp

def us(request):
	# This will load the U.S. version of the homepage
	homepage = WebPage.objects.get(name = "Home")
	try:
		# Collect the content for the "landing" section
		landing_section = WebSection.objects.filter(parent_page = homepage).get(name = "Landing")
		landing_fields = WebText.objects.filter(parent_section = landing_section)
		landing_title = landing_fields.get(name = "Title")
		landing_subtitle = landing_fields.get(name = "Subtitle")

		context = {
			'LandingTitle' : landing_title.text_us,
			'LandingSubtitle': landing_subtitle.text_us
		}
	except:
		context = {}
		context['LandingTitle'] = "Contact the webmaster."
		context['LandingSubtitle'] = "Contact the webmaster."

	try:
		# Collect the content for the "mission" section
		mission_section = WebSection.objects.filter(parent_page = homepage).get(name = "Mission")
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
		context['MissionSubsectionText1'] = "Contact the webmaster."
		context['MissionSubsectionTitle1'] = "Contact the webmaster."
		context['MissionSubsectionText2'] = "Contact the webmaster."
		context['MissionSubsectionTitle2'] = "Contact the webmaster."
		context['MissionSubsectionText3'] = "Contact the webmaster."
		context['MissionSubsectionTitle3'] = "Contact the webmaster."

	try:
		# Collect the content for the "how it works" section

		works_section = WebSection.objects.filter(parent_page=homepage).get(name = "Works")
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
		context['WorksSubsectionText1'] = "Contact the webmaster."
		context['WorksSubsectionText2'] = "Contact the webmaster."
		context['WorksSubsectionText3'] = "Contact the webmaster."
		context['WorksSubsectionTitle1'] = "Contact the webmaster."
		context['WorksSubsectionTitle2'] = "Contact the webmaster."
		context['WorksSubsectionTitle3'] = "Contact the webmaster."



	try:
		# Collect data for the "find out more" section.
		more_section = WebSection.objects.filter(parent_page = homepage).get(name = "More")
		context["MoreHeaderText"] = WebText.objects.get(parent_section = more_section).text_us

		more_wrappers = []
		for i in range(1,4):
			more_wrappers.append(WebSection.objects.filter(parent_section = more_section).get(name = "Button"+str(i)))

		more_links = ["https://globalmilestone.org/us/" + str(WebInnerLink.objects.get(parent_section = wrapper).page.link) for wrapper in more_wrappers]
		more_texts = [str(WebText.objects.get(parent_section = wrapper).text_us) for wrapper in more_wrappers]

		for i in range(1,4):
			context["MoreText" + str(i)] = more_texts[i-1]
			context["MoreLink" + str(i)] = more_links[i-1]

	except:

		context['MoreHeaderText'] = "Contact the webmaster."
		context['MoreText1'] = "Contact the webmaster."
		context['MoreLink1'] = '#',
		context['MoreText2'] = 'Contact the webmaster.'
		context['MoreLink2'] = '#'
		context['MoreText3'] = 'Contact the webmaster.'
		context['MoreLink3'] = '#'

	context = set_locale(context, 'mx', 'cn', "M&#233;xico", "&#20013;&#22269;")
	response = render(request, "index.html", context)
	response = set_http_flags(response)
	return response
def mx(request):
	# This will load the M.X. version of the homepage
	homepage = WebPage.objects.get(name = "Home")

	try:
		# Collect the content for the "landing" section
		landing_section = WebSection.objects.filter(parent_page = homepage).get(name = "Landing")
		landing_fields = WebText.objects.filter(parent_section = landing_section)
		landing_title = landing_fields.get(name = "Title")
		landing_subtitle = landing_fields.get(name = "Subtitle")

		context = {
			'LandingTitle' : landing_title.text_mx,
			'LandingSubtitle': landing_subtitle.text_mx
		}
	except:
		context['LandingTitle'] = "Contact the webmaster."
		context['LandingSubtitle'] = "Contact the webmaster."

	try:
		# Collect the content for the "mission" section
		mission_section = WebSection.objects.filter(parent_page = homepage).get(name = "Mission")
		mission_subsections_qset = WebSection.objects.filter(parent_section = mission_section)
		mission_subsection_text = []
		mission_subsection_title = []
		for i in range(1, 4):
			curr_parent_section = mission_subsections_qset.get(name = ("Column"+str(i)))
			mission_subsection_title.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Title").text_mx)
			mission_subsection_text.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Text").text_mx)
			context['MissionSubsectionText'+str(i)] = mission_subsection_text[i-1]
			context['MissionSubsectionTitle'+str(i)] = mission_subsection_title[i-1]


	except:
		context['MissionSubsectionText1'] = "Contact the webmaster."
		context['MissionSubsectionTitle1'] = "Contact the webmaster."
		context['MissionSubsectionText2'] = "Contact the webmaster."
		context['MissionSubsectionTitle2'] = "Contact the webmaster."
		context['MissionSubsectionText3'] = "Contact the webmaster."
		context['MissionSubsectionTitle3'] = "Contact the webmaster."

	try:
		# Collect the content for the "how it works" section

		works_section = WebSection.objects.filter(parent_page = homepage).get(name = "Works")
		works_subsections_qset = WebSection.objects.filter(parent_section = works_section)
		works_subsection_text = []
		works_subsection_title = []
		for i in range(1, 4):
			curr_parent_section = works_subsections_qset.get(name = ("Column"+str(i)))
			works_subsection_title.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Title").text_mx)
			works_subsection_text.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Text").text_mx)
			context['WorksSubsectionText'+str(i)] = works_subsection_text[i-1]
			context['WorksSubsectionTitle'+str(i)] = works_subsection_title[i-1]


	except:
		context['WorksSubsectionText1'] = "Contact the webmaster."
		context['WorksSubsectionText2'] = "Contact the webmaster."
		context['WorksSubsectionText3'] = "Contact the webmaster."
		context['WorksSubsectionTitle1'] = "Contact the webmaster."
		context['WorksSubsectionTitle2'] = "Contact the webmaster."
		context['WorksSubsectionTitle3'] = "Contact the webmaster."



	try:
		# Collect data for the "find out more" section.
		more_section = WebSection.objects.filter(parent_page = homepage).get(name = "More")
		context["MoreHeaderText"] = WebText.objects.get(parent_section = more_section).text_mx

		more_wrappers = []
		for i in range(1,4):
			more_wrappers.append(WebSection.objects.filter(parent_section = more_section).get(name = "Button"+str(i)))

		more_links = ["https://globalmilestone.org/mx/" + str(WebInnerLink.objects.get(parent_section = wrapper).page.link) for wrapper in more_wrappers]
		more_texts = [str(WebText.objects.get(parent_section = wrapper).text_mx) for wrapper in more_wrappers]

		for i in range(1,4):
			context["MoreText" + str(i)] = more_texts[i-1]
			context["MoreLink" + str(i)] = more_links[i-1]

	except:

		context['MoreHeaderText'] = "Contact the webmaster."
		context['MoreText1'] = "Contact the webmaster."
		context['MoreLink1'] = '#',
		context['MoreText2'] = 'Contact the webmaster.'
		context['MoreLink2'] = '#'
		context['MoreText3'] = 'Contact the webmaster.'
		context['MoreLink3'] = '#'

	context = set_locale(context, 'us', 'cn', "US", "&#20013;&#22269;")

	response = render(request, "index.html", context)
	response = set_http_flags(response)
	return response
def cn(request):
	# This will load the C.N. version of the homepage
	homepage = WebPage.objects.get(name = "Home")
	try:
		# Collect the content for the "landing" section
		landing_section = WebSection.objects.filter(parent_page = homepage).get(name = "Landing")
		landing_fields = WebText.objects.filter(parent_section = landing_section)
		landing_title = landing_fields.get(name = "Title")
		landing_subtitle = landing_fields.get(name = "Subtitle")

		context = {
			'LandingTitle' : landing_title.text_cn,
			'LandingSubtitle': landing_subtitle.text_cn,
		}
	except:
		context['LandingTitle'] = "Contact the webmaster."
		context['LandingSubtitle'] = "Contact the webmaster."

	try:
		# Collect the content for the "mission" section
		mission_section = WebSection.objects.filter(parent_page = homepage).get(name = "Mission")
		mission_subsections_qset = WebSection.objects.filter(parent_section = mission_section)
		mission_subsection_text = []
		mission_subsection_title = []
		for i in range(1, 4):
			curr_parent_section = mission_subsections_qset.get(name = ("Column"+str(i)))
			mission_subsection_title.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Title").text_cn)
			mission_subsection_text.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Text").text_cn)
			context['MissionSubsectionText'+str(i)] = mission_subsection_text[i-1]
			context['MissionSubsectionTitle'+str(i)] = mission_subsection_title[i-1]


	except:
		context['MissionSubsectionText1'] = "Contact the webmaster."
		context['MissionSubsectionTitle1'] = "Contact the webmaster."
		context['MissionSubsectionText2'] = "Contact the webmaster."
		context['MissionSubsectionTitle2'] = "Contact the webmaster."
		context['MissionSubsectionText3'] = "Contact the webmaster."
		context['MissionSubsectionTitle3'] = "Contact the webmaster."

	try:
		# Collect the content for the "how it works" section

		works_section = WebSection.objects.filter(parent_page = homepage).get(name = "Works")
		works_subsections_qset = WebSection.objects.filter(parent_section = works_section)
		works_subsection_text = []
		works_subsection_title = []
		for i in range(1, 4):
			curr_parent_section = works_subsections_qset.get(name = ("Column"+str(i)))
			works_subsection_title.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Title").text_cn)
			works_subsection_text.append(WebText.objects.filter(parent_section = curr_parent_section).get(name = "Text").text_cn)
			context['WorksSubsectionText'+str(i)] = works_subsection_text[i-1]
			context['WorksSubsectionTitle'+str(i)] = works_subsection_title[i-1]


	except:
		context['WorksSubsectionText1'] = "Contact the webmaster."
		context['WorksSubsectionText2'] = "Contact the webmaster."
		context['WorksSubsectionText3'] = "Contact the webmaster."
		context['WorksSubsectionTitle1'] = "Contact the webmaster."
		context['WorksSubsectionTitle2'] = "Contact the webmaster."
		context['WorksSubsectionTitle3'] = "Contact the webmaster."



	try:
		# Collect data for the "find out more" section.
		more_section = WebSection.objects.filter(parent_page = homepage).get(name = "More")
		context["MoreHeaderText"] = WebText.objects.get(parent_section = more_section).text_cn

		more_wrappers = []
		for i in range(1,4):
			more_wrappers.append(WebSection.objects.filter(parent_section = more_section).get(name = "Button"+str(i)))

		more_links = ["https://globalmilestone.org/cn/" + str(WebInnerLink.objects.get(parent_section = wrapper).page.link) for wrapper in more_wrappers]
		more_texts = [str(WebText.objects.get(parent_section = wrapper).text_cn) for wrapper in more_wrappers]

		for i in range(1,4):
			context["MoreText" + str(i)] = more_texts[i-1]
			context["MoreLink" + str(i)] = more_links[i-1]

	except:

		context['MoreHeaderText'] = "Contact the webmaster."
		context['MoreText1'] = "Contact the webmaster."
		context['MoreLink1'] = '#',
		context['MoreText2'] = 'Contact the webmaster.'
		context['MoreLink2'] = '#'
		context['MoreText3'] = 'Contact the webmaster.'
		context['MoreLink3'] = '#'

	context = set_locale(context, 'mx', 'us', "M&#233;xico", "US")

	response = render(request, "index.html", context)
	response = set_http_flags(response)
	return response

def about_us(request):
	aboutpage = WebPage.objects.get(name = "About")

	landing_section = WebSection.objects.filter(parent_page = aboutpage).get(name = "Landing")
	leadership_section = WebSection.objects.filter(parent_page = aboutpage).get(name = "Leadership")
	tutors_section = WebSection.objects.filter(parent_page = aboutpage).get(name = "Tutors")

	landing_title = WebText.objects.filter(parent_section = landing_section).get(name = "Title")
	context = {}
	context["Landing_Title"] = landing_title.text_us

	leaders = [WebSection.objects.filter(parent_section = leadership_section).get(name = str(i)) for i in range(1,8)]

	leader_names = [WebText.objects.filter(parent_section = leader).get(name = "Name").text_us for leader in leaders]
	for i in range(1,8):
		context["Leaders_"+str(i)+"_Name"] = leader_names[i-1]
	response = render(request, "sub/about.html", context)
	response = set_http_flags(response)
	return response

def enroll_us(request):

	response = render(request, "sub/enroll.html")
	response = set_http_flags(responses)
	return response



def tutor_us(request):
	response = render(request, "sub/become_student.html")
	response["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
	response["Pragma"] = "no-cache" # HTTP 1.0.
	response["Expires"] = "0" # Proxies.
	return response

def fallback(request):
	return redirect('/us')
