#!/usr/bin/python3
"""Parsing log files"""

loginfail = 0 #counter for fails, starts at 0

keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r")

keystone_file_lines = keystone_file.readlines()

#loop over the list of lines
for line in keystone_file_lines:
    #looking for a fail pattern "- - - - -] Authorization failed"
    if "- - - - -] Authorization failed" in line:
        loginfail += 1 
print("the number of failed log in attempts in", loginfail)
keystone_file.close()


