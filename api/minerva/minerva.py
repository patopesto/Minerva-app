import requests
import json
import sys, time, math, logging
from datetime import datetime

from bs4 import BeautifulSoup
from xml.etree import ElementTree

logger = logging.getLogger(__name__)


def minerva_task(course):
	url = url_generator(course['term'], course['dept'], course['code'])
	spaces = minerva_request(url, course['crn'])
	if spaces > 0:
		logger.info("Found the course {}-{} ({}) with {} spaces available".format(course['dept'],course['code'],course['crn'],spaces))
	else:
		logger.info("No spaces found for the course {}-{} ({})".format(course['dept'],course['code'],course['crn']))
	return spaces

def minerva_request(url,key):
	try:
		r = requests.get(url)
		r.raise_for_status()
		logger.debug("Successful get request")
	except Exception as error:
		logger.error(error)
	#print(r.content)
	
	spaces = 0

	tree = ElementTree.fromstring(r.content)
	
	for child in tree.iter('course'):
		#print(child.tag, child.attrib)
		#print(child.tag)
		for child2 in child.iter('*'):
			#print(child2.tag)
			if child2.tag == "block":
				#print(child2.attrib)
				#print("key: {} with os: {}".format(child2.attrib['key'],child2.attrib['os']))
				if child2.attrib['key'] in key and int(child2.attrib['os']) > 0:
					#logger.info('Found the course {} ({}) with {} spaces available.'.format(child.attrib['key'],child2.attrib['key'],child2.attrib['os']))
					#notify(child.attrib['key'],child2.attrib['key'],child2.attrib['os'])
					spaces = int(child2.attrib['os'])
					return spaces
	
	return spaces
	

def url_generator(term,dept,course_code):
	now = time.time()
	now_milli = int(round(now * 1000))

	f8b0=["\x26\x74\x3D","\x26\x65\x3D"]
	t = (math.floor(now_milli/60000)%1000);
	#print(t)
	e = t%3+t%19+t%42;
	#print(e)
	result = f8b0[0]+str(t)+f8b0[1]+str(e);
	#print(result)

	url = 'https://vsb.mcgill.ca/vsb/getclassdata.jsp?'
	term = getTerm(term)
	url += 'term={}'.format(term)
	url += '&course_0_0={}-{}'.format(dept, course_code)
	url += ('&rq_0_0=null' + result + '&nouser=1&_=' + str(int(now)))

	return url


#format: Fall2020
def getTerm(term):
	period = term[:-4].lower()
	year = term[-4:]

	url_term = year

	if period == 'fall':
		url_term += '09'
	elif period == 'winter':
		url_term += '01'
	elif period == 'summer':
		url_term += '05'
	else:
		logger.error("Bad term provided: {}".format(term))

	return url_term






