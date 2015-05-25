# -*-coding:utf-8 -*-
# author : zhuyb
#
# -- file : parse book mark 2 markdown .py

import requests
import gzip
import StringIO
import ConfigParser
import sys
from bs4 import BeautifulSoup
import time
import re
# import MySQLdb 
import urllib2
import urllib
import cookielib

########################################################################
class BookMark2MD:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.bookMarkFile = "bookmarks_15_5_25.html"
        try:
            self.bookmark = open(self.bookMarkFile,'r')
            self.page = self.bookmark.read()
        finally:
            self.bookmark.close()
            
            
    #----------------------------------------------------------------------
    def parseMarks(self,content):
        """"""
        soup = BeautifulSoup(content)
        tagA = soup.find_all('a')
        print len(tagA)
        #print tagA[0].prettify()
        hrefAndVal = []
        for a in tagA:
            href = a['href']
            val = a.get_text().encode('utf8').strip()
            pair = (href,val)
            hrefAndVal.append(pair)
        return hrefAndVal
            
        
        
    #----------------------------------------------------------------------
    def run(self):
        """"""
        md = open('bookmark.md','w+')
        #print self.page
        kav = self.parseMarks(self.page)
        try:
                
            for kv in kav:
                href, val = kv
                line = "* [%s](%s) \n" % (val,href)
                md.write(line)
            print 'done!'
        finally:
            md.close()
        
        
bookmark2md = BookMark2MD()
bookmark2md.run()
        
            
        
        
    
    

