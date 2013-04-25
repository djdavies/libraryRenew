#!/usr/bin/env python
import mechanize
import sys
import cookielib
import os
import datetime
#import BeautifulSoup

now = datetime.datetime.now()

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# The site we will navigate into, handling it's session
#r = br.open('https://library.cardiff.ac.uk/vwebv/myAccount?sk=en_CF')
r = br.open('https://library.cardiff.ac.uk/vwebv/login.cgi')
html = r.read()

# Show the source, for test run and > test.html
#print html

## Show the available forms, for testing/sanity
#for f in br.forms():
#        print f
#
## Select the first (index zero) form
br.select_form(nr=0)
##print "FORMS"
#
# Logging in
try:
    br.form['ext_id']='your_username'
    br.form['ext_pw']='your_password' # I don't care :-)
    br.submit()
    print "Login successful"
except:
    print "Login unsuccessful. Check your credentials"
    # print "Here are your current books and due dates: "
    # print books on loan here, and original due dates
#print br.response().read()

br.select_form(nr=1) # nr=1 -> 2nd form
# 'select all' checkbox
print "Now renewing all your books"
try:
    br.find_control("selectCharged").items[0].selected=True
    br.submit() # click renew button
    # push this read into output.html
    print br.response().read() # prints mass HTML 
    print "All books renewed, as of: ", now.strftime("%Y-%m-%d %H:%M")
    # print new due dates here
    os.system("python testEmail.py") # edit this file for your email needs
except:
    print "Something went wrong. :-("

