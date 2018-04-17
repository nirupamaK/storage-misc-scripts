#!/usr/bin/python
from sys import argv
from subprocess import call
import re
script, filename, dest = argv
data = []; file_names = []; archive_names = []

with open(filename) as f:
    for line in f.readlines():
        #print line
        TUP = tuple(line.strip().split(':'))
        #print TUP
        if any('Filename' in data for data in TUP):
            print "Inputfile is "+ TUP[1]
            file_names.append(TUP[1])
        elif any('Archive Name' in data for data in TUP):
            print "Archive Name" + TUP[1]
            archive_names.append(TUP[1])
        else:
            continue

for onefile in file_names:
    for archive in archive_names:
       call(["tar", "xvf", archive, "-C", dest, "--wildcards", "--no-anchored", onefile ])


print "All restore is complited.\nPlease check and ensure extracted files are properly located.\n"
