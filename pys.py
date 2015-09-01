import re
from datetime import *
from coclass import Course

cfile = open('courses.txt', 'r')
contents = cfile.readlines()
rfc_format = '%Y-%m-%dT%I:%M:%S+08:00'
#courses = (re.findall('[A-Z]{4} [0-9]{4}-[A-Z]{1,2}[0-9]{1,2}', contents) )
mycourses = []
for i in range(len(contents)):
    course = re.findall('[A-Z]{4} [0-9]{4}-[A-Z]{1,2}[0-9]{1,2}', contents[i])
    if course:
        course = ''.join(course)
    
        days = re.findall('[MTWF][ouehr]', contents[i+1])
        days = ''.join(days)
        #print days

        time = re.findall('[0-9]{1,2}:[0-9]{2}[AP]M', contents[i+1])
        for t in time:
            t = datetime.strptime(t, '%I:%M%p')
            print t
        mycourses.append(Course(course, days, time))
        
