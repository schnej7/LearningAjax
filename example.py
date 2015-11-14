import json
import urllib2

data = json.load(urllib2.urlopen("http://api.tripadvisor.com/api/partner/2.0/location/48739/?key=4518e505-92d6-4490-957a-3b2da9a9024c"))
print data
