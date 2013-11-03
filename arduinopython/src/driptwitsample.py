#******************************************#
# Tweet-a-Pot by Gregg Horton 2011         #
# Please email changes or                  # 
# updates to greggawatt@instructables.com  #
# so i can keep it updated		   #
# *****************************************#

##Import Libraries

import twitter
import serial  
import time

##authenticate yourself with twitter
api = twitter.Api(consumer_key='qsNzAlQRZ8sxDFTqWLAuw', consumer_secret='CsFpIBujbrzJvPoNu6HQ1V1IOQMBqZ3cE1SpRqvKSk', access_token_key='2171293940-VfiwNLKbWLssgb4fc5FNK50lJQScmptxNScNilh', access_token_secret='Um4LcZte9S4pezX7IpCBBxXKBcfuEH4Eb579AdAoMR5ec') 

##set to your serial port
ser = serial.Serial('/dev/ttyUSB0', 19200)

## check serial port
def checkokay():
	ser.flushInput()
	time.sleep(3)
	line=ser.readline()
	time.sleep(3)

	if line == ' ':
		line=ser.readline()
	print 'here'
## Welcome message
print 'Welcome To Drip Twit!'

def driptwit():
	status = [] 
	x = 0
	
	status = api.GetUserTimeline('yourusername') ##grab latest statuses
	
	checkIt = [s.text for s in status] ##put status in an array

	drip = checkIt[0].split() ##split first tweet into words

	## check for match and write to serial if match
	if drip[0] == '#driptwit':
		print 'Tweet Recieved, Making Coffee'
		ser.write('1')
	elif drip[0] == '#driptwitstop': ##break if done
		ser.write('0')
		print 'stopped, awaiting instructions.'
	else:
		ser.write('0')
		print 'Awaiting Tweet'
		
		
	
while 1:
	driptwit() ## call driptwit function
	time.sleep(15) ## sleep for 15 seconds to avoid rate limiting
	
