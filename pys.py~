import re
from datetime import *
from coclass import Course

def parse_file():
	weekday_dict = {'Mo' : 'Monday',
					'Tu' : 'Tuesday',
					'We' : 'Wednesday',
					'Th' : 'Thursday', 
					'Fr' : 'Friday'} 


	cfile = open('courses.txt', 'r')
	contents = cfile.readlines()
	rfc_format = '%Y-%m-%dT%I:%M:%S+08:00'
	#courses = (re.findall('[A-Z]{4} [0-9]{4}-[A-Z]{1,2}[0-9]{1,2}', contents) )
	mycourses = []
	qk_req = []

	for i in range(len(contents)):
		course = re.findall('[A-Z]{4} [0-9]{4}-[A-Z]{1,2}[0-9]{1,2}', contents[i])
		if course:
			course = ''.join(course)
		
			days = re.findall('[MTWF][ouehr]', contents[i+1])
			if days:
				w = weekday_dict[days[0]] + "s"
			if len(days) > 1:
				for d in range(len(days)):
					days[d] = weekday_dict[days[d]]
				w = "s and ".join(days) + "s"
			

			time = re.findall('[0-9]{1,2}:[0-9]{2}[AP]M - [0-9]{1,2}:[0-9]{2}[AP]M', contents[i+1])
			if time:
				qk_req.append( course + " on " + w + " "+ time[0] + " " + contents[i+2])
			
			
			mycourses.append(Course(course, days, time))
	return qk_req
