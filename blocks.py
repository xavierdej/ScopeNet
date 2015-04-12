import requests
import json

import ephem
import datetime
from geopy.geocoders import Nominatim

import serial
import time

from cv2 import *

import os, numpy, PIL
from PIL import Image, ImageEnhance
import matplotlib as plt
import numpy as np


def requestJob():
	r = requests.get("http://scopenet.agm.me.uk/api/getnext.php")
	return json.loads(r.content)
	print r

def convertCelestialToHorizonNow(job, location):
	bodyName = job['body']

	dt = datetime.datetime.now();
	dt = str(dt.year) +'/'+ str(dt.month) +'/'+ str(dt.day)  +' '+ str(dt.hour-1) + ':' +str(dt.minute)
	gatech = ephem.Observer()
	gatech.epoch = dt

	if bodyName == "Sun":
		body = ephem.Sun()
	elif bodyName == "Moon":
		body = ephem.Moon()
	elif bodyName == "Mercury":
		body = ephem.Mercury()
	elif bodyName == "Venus":
		body = ephem.Venus()
	elif bodyName == "Mars":
		body = ephem.Mars()
	elif bodyName == "Phobos":
		body = ephem.Phobos()
	elif bodyName == "Deimos":
		body = ephem.Deimos()
	elif bodyName == "Jupiter":
		body = ephem.Jupiter()
	elif bodyName == "Io":
		body = ephem.Io()
	elif bodyName == "Europa":
		body = ephem.Europa()
	elif bodyName == "Ganymede":
		body = ephem.Ganymede()
	elif bodyName == "Callisto":
		body = ephem.Callisto()
	elif bodyName == "Saturn":
		body = ephem.Saturn()
	elif bodyName == "Mimas":
		body = ephem.Mimas()
	elif bodyName == "Enceladus":
		body = ephem.Enceladus()
	elif bodyName == "Tethys":
		body = ephem.Tethys()
	elif bodyName == "Dione":
		body = ephem.Dione()
	elif bodyName == "Rhea":
		body = ephem.Rhea()
	elif bodyName == "Titan":
		body = ephem.Titan()
	elif bodyName == "Iapetus":
		body = ephem.Iapetus()
	elif bodyName == "Hyperion":
		body = ephem.Hyperion()
	elif bodyName == "Uranus":
		body = ephem.Uranus()
	elif bodyName == "Miranda":
		body = ephem.Miranda()
	elif bodyName == "Ariel":
		body = ephem.Ariel()
	elif bodyName == "Umbriel":
		body = ephem.Umbriel()
	elif bodyName == "Titania":
		body = ephem.Titania()
	elif bodyName == "Oberon":
		body = ephem.Oberon()
	elif bodyName == "Neptune":
		body = ephem.Neptune()
	elif bodyName == "Pluto":
		body = ephem.Pluto()
	else:
		body = ephem.star(bodyName)

	geolocator = Nominatim()
	location = geolocator.geocode(location)
	gatech.lon, gatech.lat = str(location.longitude), str(location.latitude)
	gatech.date = dt
	body.compute(gatech)
	return body

def setPosition(azimuth, elevation, serialPort):
	telescope = serial.Serial(serialPort, 9600)
	command = 'a' + azimuth + 'e' + elevation + 'c'
	print command
	telescope.write(command)
	time.sleep(10)

def captureDatas():
	cam = VideoCapture(0)
	for x in xrange(1,6):
		s, img = cam.read()
		if s:
			imwrite("datas/capture_" + str(x).zfill(3) + ".png",img)


def processDatas():
	allfiles=os.listdir(os.getcwd() + "/datas")
	imlist=[filename for filename in allfiles if  filename[-4:] in [".png",".png"]]


	w,h=Image.open("datas/" + imlist[0]).size
	N=len(imlist)
	number = 1

	arr=numpy.zeros((h,w,3),numpy.float)
	first = numpy.array(Image.open("datas/" + imlist[0]),dtype=numpy.float)

	loop = 0

	for im in imlist:
	    loop = loop + 1
	    imarr=numpy.array(Image.open("datas/" + im),dtype=numpy.float)
	    diff = first - imarr
	    total = 0
	    for idx, value in np.ndenumerate(diff):
	    	total = total + value
	    total = total / first.size

	    if total*total < 0.1:
	    	number +=1
	    	arr=arr+imarr
	arr = arr/number

	arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

	out=Image.fromarray(arr,mode="RGB")
	out.save("results/Average.png")

def enchanceResults():
	arr=numpy.array(Image.open('results/Average.png'),dtype=numpy.float)
	arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)
	out=Image.fromarray(arr,mode="RGB")
	enhancer = ImageEnhance.Contrast(out)
	outimg = enhancer.enhance(3)
	outimg.save('results/Enchanced.png')

def postResult(job, body):
	url = "http://scopenet.agm.me.uk/api/uploadimage.php"
	payload = {'file': open('results/Enchanced.png', 'rb')}
	meta = {'bodyName':body.name, 'jobid':job['jobid']}
	# values = {'author': 'John Smith'}
	r = requests.post(url, files=payload, data=meta)
	print r.content

