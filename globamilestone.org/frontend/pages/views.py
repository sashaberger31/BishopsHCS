from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from pages.models import Tutor, WebText, WebPage, WebImg, WebSection, WebInnerLink
import sys
import math

"""
Class-based views documentation

CacheView: views that don't set any caching flags in the HTTP Headers
NoCacheView: views that set no-cache, no-store flags
"""

def partition(self, num_rows, per_row, tail, objects):
	ret = "\n"
	for j in range(num_rows-1):
		row = "\""
		for i in range(per_row):
			row += "tutor" + str(objects[per_row*j+i]["i"])
			if i != per_row-1:
				row += " "
		row += "\"\n"
		ret += row
	row = "\""
	for k in range(tail):
		row += "tutor" + str(objects[per_row*(num_rows-1)+k]["i"]) + " "
		if k != tail-1:
			row += " "
	row += ". " * (per_row-tail)
	row += "\";"
	ret += row
	return ret


class NoCacheView(View):
	"""
	This is a view which returns the correct version of the page for each locale.
	It will also set no-cache, no-store flags in the HTTP headers.
	"""
	locale = "us"	# Default
	def set_header_locale(self, args, code):
		"""
		This will take in a dictionary and add the correct variables to ensure
		that the header bar always displays the correct locale swap buttons.

		args - dictionary to work with
		code - the code of the current locale

		WARNING:
		In order to work, the flag icon corresponding to an 'mx' code locale
		must have a path of /static/pages/img/icons/flags/mx.png.
		"""
		codes = {
			'mx': [('us', 'United States'), ('cn', "&#20013;&#22269;")],
			'cn': [('us', 'United States'), ('mx', 'M&#233;xico')],
			'us': [('cn',"&#20013;&#22269;"), ('mx', 'M&#233;xico')]
		}

		alt1 = codes[code][0]
		alt2 = codes[code][1]
		args['locale'] = code
		args['nonlocal1'] = alt1[0]
		args['nonlocal2'] = alt2[0]
		args['nonlocaltext1'] = alt1[1]
		args['nonlocaltext2'] = alt2[1]
		args['nonlocallink1'] = 'pages/img/icons/flags/'+alt1[0]+'.png'
		args['nonlocallink2'] = 'pages/img/icons/flags/'+alt2[0]+'.png'

		return args

	def set_http_flags(self, resp):
		"""
		Set any HTTP Flags that you want here

		Takes in a response to alter and returns it after changing flags.
		"""
		resp["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
		resp["Pragma"] = "no-cache" # HTTP 1.0.
		resp["Expires"] = "0" # Proxies.

		return resp
	def template_response(self, request, locale):
		"""
		This will be overriden by child classes. It should return a response.
		"""

		return HTTPResponse("")

	def get(self, request):
		"""
		Django will call this method on receiving a "GET" request.
		Takes in a request object as well as a locale code.
		"""

		response = self.template_response(request, self.locale) # Render the template
		response = self.set_http_flags(response) # Set flags
		return response

class HomeView(NoCacheView):
	def template_response(self, request, locale):
		"""
		Will render the homepage template with the appropriate locale.

		The only supported locales at the moment are us, mx, cn.
		"""

		homepage = WebPage.objects.get(name = "Home")	# Model for the homepage
		try:
			# Collect the content for the "landing" section
			landing_section = WebSection.objects.filter(parent_page = homepage).get(name = "Landing")
			landing_fields = WebText.objects.filter(parent_section = landing_section)
			landing_title = landing_fields.get(name = "Title")
			landing_subtitle = landing_fields.get(name = "Subtitle")

			context = {}
			# ---------------------------------------------------------- #
			# ----- WARNING: DO NOT FEED USER INPUT INTO eval()!!! ----- #
			context['LandingTitle'] = eval("landing_title.text_" + locale)
			context['LandingSubtitle'] = eval("landing_subtitle.text_" + locale)
			# ---------------------------------------------------------- #
			# ---------------------------------------------------------- #

		except:
			# If there is an error, someone probably deleted the model instance
			# In that case, just put dummy text
			context = {}
			context['LandingTitle'] = "Contact the webmaster."
			context['LandingSubtitle'] = "Contact the webmaster."

		try:
			# Collect the content for the "mission" section
			mission_section = WebSection.objects.filter(parent_page = homepage).get(name = "Mission")
			mission_subsections_qset = WebSection.objects.filter(parent_section = mission_section)
			mission_subsection_text = []
			mission_subsection_title = []
			for i in range(1,4):
				curr_parent_section = mission_subsections_qset.get(name = ("Column"+str(i)))
				# ---------------------------------------------------------- #
				# ----- WARNING: DO NOT FEED USER INPUT INTO eval()!!! ----- #
				curr_title = eval("WebText.objects.filter(parent_section = curr_parent_section).get(name = 'Title').text_" + locale)
				curr_text = eval("WebText.objects.filter(parent_section = curr_parent_section).get(name = 'Text').text_" + locale)
				# ---------------------------------------------------------- #
				# ---------------------------------------------------------- #
				context['MissionSubsectionText'+str(i)] = curr_text
				context['MissionSubsectionTitle'+str(i)] = curr_title
		except:
			# If there is an error, someone probably deleted the model instance
			# In that case, just put dummy text
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
				# ---------------------------------------------------------- #
				# ----- WARNING: DO NOT FEED USER INPUT INTO eval()!!! ----- #
				curr_title = eval("WebText.objects.filter(parent_section = curr_parent_section).get(name = 'Title').text_" + locale)
				curr_text = eval("WebText.objects.filter(parent_section = curr_parent_section).get(name = 'Text').text_" + locale)
				# ---------------------------------------------------------- #
				# ---------------------------------------------------------- #
				context['WorksSubsectionText'+str(i)] = curr_text
				context['WorksSubsectionTitle'+str(i)] = curr_title
		except:
			# If there is an error, someone probably deleted the model instance
			# In that case, just put dummy text
			context['WorksSubsectionText1'] = "Contact the webmaster."
			context['WorksSubsectionText2'] = "Contact the webmaster."
			context['WorksSubsectionText3'] = "Contact the webmaster."
			context['WorksSubsectionTitle1'] = "Contact the webmaster."
			context['WorksSubsectionTitle2'] = "Contact the webmaster."
			context['WorksSubsectionTitle3'] = "Contact the webmaster."

		try:
			# Collect data for the "find out more" section.
			more_section = WebSection.objects.filter(parent_page = homepage).get(name = "More")
			# ---------------------------------------------------------- #
			# ----- WARNING: DO NOT FEED USER INPUT INTO eval()!!! ----- #
			context["MoreHeaderText"] = eval("WebText.objects.get(parent_section = more_section).text_" + locale)
			# ---------------------------------------------------------- #
			# ---------------------------------------------------------- #

			more_wrappers = []
			for i in range(1,4):
				more_wrappers.append(WebSection.objects.filter(parent_section = more_section).get(name = "Button"+str(i)))

			more_links = ["https://globalmilestone.org/us/" + str(WebInnerLink.objects.get(parent_section = wrapper).page.link) for wrapper in more_wrappers]
			# ---------------------------------------------------------- #
			# ----- WARNING: DO NOT FEED USER INPUT INTO eval()!!! ----- #
			more_texts = [str(eval("WebText.objects.get(parent_section = wrapper).text_" + locale)) for wrapper in more_wrappers]
			# ---------------------------------------------------------- #
			# ---------------------------------------------------------- #
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

		context = self.set_header_locale(context, locale)
		response = render(request, "index.html", context)
		return response
class AboutView(NoCacheView):
	def partition_tutors(self, num_rows, per_row, tail, tutors):
		ret = "\n"
		for j in range(num_rows-1):
			row = "\""
			for i in range(per_row):
				row += "tutor" + str(tutors[per_row*j+i]["i"])
				if i != per_row-1:
					row += " "
			row += "\"\n"
			ret += row
		row = "\""
		for k in range(tail):
			row += "tutor" + str(tutors[per_row*(num_rows-1)+k]["i"]) + " "
			if k != tail-1:
				row += " "
		row += ". " * (per_row-tail)
		row += "\";"
		ret += row
		return ret

	def template_response(self, request, locale):
		aboutpage = WebPage.objects.get(name = "About")

		landing_section = WebSection.objects.filter(parent_page = aboutpage).get(name = "Landing")
		leadership_section = WebSection.objects.filter(parent_page = aboutpage).get(name = "Leadership")
		tutors_section = WebSection.objects.filter(parent_page = aboutpage).get(name = "Tutors")

		landing_title = WebText.objects.filter(parent_section = landing_section).get(name = "Title")
		context = {}
		context["Landing_Title"] = landing_title.text_us

		leaders = [WebSection.objects.filter(parent_section = leadership_section).get(name = str(i)) for i in range(1,8)]

		leader_names = [eval("WebText.objects.filter(parent_section = leader).get(name = 'Name').text_"+locale) for leader in leaders]
		leader_img_paths = [WebImg.objects.filter(parent_section = leader).get(name = "Face").path_to_file for leader in leaders]
		leader_img_alt = [eval("WebImg.objects.filter(parent_section = leader).get(name='Face').alt_" +locale)  for leader in leaders]
		leader_titles = [eval("WebText.objects.filter(parent_section = leader).get(name='Title').text_" + locale) for leader in leaders]


		for i in range(1,8):
			context["Leaders_"+str(i)+"_Name"] = leader_names[i-1]
			context["Leaders_"+str(i)+"_Path"] = leader_img_paths[i-1]
			context["Leaders_"+str(i)+"_Alt"] = leader_img_alt[i-1]
			context["Leaders_"+str(i)+"_Title"] = leader_titles[i-1]

		tutors_qset = WebSection.objects.filter(parent_section = tutors_section)
		tutor_sections = [[i, tutors_qset.get(name = str(i))] for i in range(1,len(tutors_qset)+1)]

		tutors = [{"i": sect[0], "Name":  eval("WebText.objects.filter(parent_section = sect[1]).get(name = 'Name').text_" + locale),\
		"Title": eval("WebText.objects.filter(parent_section = sect[1]).get(name = 'Title').text_"+locale), \
		"Path":	WebImg.objects.filter(parent_section = sect[1]).get(name = "Face").path_to_file, \
		"Alt": 	eval("WebImg.objects.filter(parent_section = sect[1]).get(name = 'Face').alt_" + locale), \
		"parity": "grid" + str(1+(-1)**int(sect[0])), "GridName" : "tutor"+str(sect[0])} for sect in tutor_sections]

		# CAN BE ALTERED WITHOUT BREAKING THINGS #
		per_row = [1, 2, 3, 4]
		# -------------------------------------- #

		# DON'T ALTER #
		divs = len(per_row)	# Amount of responsive divisions
		row_num = [math.ceil((len(tutor_sections)/per_row[i])) for i in range(divs)]
		tail = [per_row[i]- (row_num[i]*per_row[i] - len(tutor_sections)) for i in range(divs)]
		grid_area_string = [self.partition_tutors(row_num[i], per_row[i], tail[i], tutors) for i in range(divs)]
		# ---------- #


		context["Tutors"] = tutors
		context["TemplateColumns"] = {}
		context["TemplateRows"] = {}
		context["GAString"] = {}

		for i in range(divs):
			context["TemplateColumns"]["brk"+str(i)] = "1fr "*per_row[i]
			context["TemplateRows"]["brk"+str(i)] = "1fr "*row_num[i]
			context["GAString"]["brk"+str(i)] = grid_area_string[i]

		context = self.set_header_locale(context, locale)
		response = render(request, "sub/about.html", context)
		return response
class EnrollView(NoCacheView):
	def template_response(self, request, locale):
		enroll_page = WebPage.objects.get(name = "Enroll")
		class_section = WebSection.objects.filter(parent_page = enroll_page).get(name = "Classes")
		class_section_qset = WebSection.objects.filter(parent_section = class_section)
		classes = [class_section_qset.get(name = str(i)) for i in range(1,len(class_section_qset)+1)]

		# Partition them
		context = self.set_header_locale(context, locale)
		response = render(request, "sub/enroll.html", context)
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
