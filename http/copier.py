#!/usr/bin/env python

import os, sys
from glob import glob
from classes.Spider import Spider

import urllib2

url = spiderman.link

url = 'https://programminghistorian.org/lessons/working-with-web-pages'

response = urllib2.urlopen(url)
webContent = response.read()

f = open('test.html', 'w')
f.write(webContent)
f.close
