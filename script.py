import requests
import cv2
from boto.s3.connection import S3Connection
import json
keys = json.loads(open("config.json").read())
conn = S3Connection(keys['access'], keys['secret'])
