import requests
import cv2
from boto.s3.connection import S3Connection
import json
import sys
from boto.s3.key import Key
import xmltodict
import os
import hashlib
import math
import imp
import random

utils = imp.load_source("utils","/usr/lib/python2.7/site-packages/google/modules/utils.py")
calculator = imp.load_source("calculator","/usr/lib/python2.7/site-packages/google/modules/calculator.py")
currency = imp.load_source("currency","/usr/lib/python2.7/site-packages/google/modules/currency.py")
shopping_search = imp.load_source("shopping_search","/usr/lib/python2.7/site-packages/google/modules/shopping_search.py")
standard_search = imp.load_source("standard_search","/usr/lib/python2.7/site-packages/google/modules/standard_search.py")
images = imp.load_source("images","/usr/lib/python2.7/site-packages/google/modules/images.py")
modules = imp.load_source("modules","/usr/lib/python2.7/site-packages/google/modules/__init__.py")
google = imp.load_source("google","/usr/lib/python2.7/site-packages/google/google.py")

if len(sys.argv) < 2:
  sys.exit(0)
user = sys.argv[1]
response = requests.get("https://myanimelist.net/malappinfo.php?status=all&type=anime&u="+user)
anime = json.loads(json.dumps(xmltodict.parse(response.content)))["myanimelist"]["anime"]
anime = [a["series_title"] for a in anime]
if len(anime) == 0:
  print "add anime to your profile please"
  sys.exit(0)
trimmedAnime = []
for i in xrange(min(len(anime),5)):
  trimmedAnime.append(anime.pop(random.randint(0,len(anime)-1)))
md5user = hashlib.md5(user.encode()).hexdigest()
os.system("mkdir " + md5user)
picsDl = math.ceil(100/float(len(trimmedAnime)))
print "downloading "+str(picsDl)+" per anime"
options = images.ImageOptions()
options.size_category = images.SizeCategory.SMALL
for anim in trimmedAnime:
  results = google.search_images(anim, options)
  images.fast_download(results[:int(picsDl)], path = md5user, threads=12)
os.system("python mosaic.py faces/"+hashlib.md5((user+"face").encode()).hexdigest()+".png "+md5user+"/ "+user)
keys = json.loads(open("config.json").read())
conn = S3Connection(keys['access'], keys['secret'])
mal = Key(conn.get_bucket('myanimeprofilepic'))
mal.key = user+".png"
mal.set_contents_from_filename(mal.key)
os.system("rm -rf faces/"+hashlib.md5((user+"face").encode()).hexdigest()+".png "+md5user+" "+user+".png")
print "done"
