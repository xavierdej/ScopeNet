from blocks import *
import math
while 1:
	print "Let me see if I can do some work"
	job = requestJob();
	if job['jobid'] == '0':
		print "No work for now, let me have a nap ..."
		time.sleep(float(job['delay']))
	else:
		print "Time to get some work done!"
		body = convertCelestialToHorizonNow(job, 'University of York, England')
		az = round((float(body.az)*360/(2*math.pi))%180,2)
		alt = round((float(body.alt)*360/(2*math.pi))%180, 2)
		print "Lets have a look will we"
		print "And while were there, let's take a few pictures"
		setPosition(str(az), str(alt), '/dev/tty.usbmodem0E202A71')

		print "Now fetching new data's, fake ones for now"
		captureDatas()
		print "Let me process these for you, it might take a while"
		processDatas()
		print "Ok we got throug that, hang on a bit longer ..."
		print "We will enchance the result, just for you!"
		enchanceResults()
		print "Ok now were done with the heavy stuff"
		print "Let me send this to Skynet ..."
		postResult(job, body)