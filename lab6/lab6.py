#!/usr/bin/python
import os, sys

POST={}
args=sys.stdin.read().split('&')

for arg in args: 
    t=arg.split('=')
    
    if len(t)>1: k, v=arg.split('='); POST[k]=v

print "Content-type: text/html\n\n"
print "This is the Python script.<br>"
print POST.get('name').title().replace("+", " ")
print "<br>"
print POST.get('address').title().replace("+", " ")
print "<br>"
phone = POST.get('phone').replace("%28", "(").replace("%29", ")")
arr = phone.split('-')
print("<link rel='stylesheet' type='text/css' href='../css/lab6-scripts.css'>")
print("<span id='segment1' style='color:red; display:inline'>" + arr[0] + "</span>")
print("<span id='segment2' style='color:green; display:inline'>" + arr[1] + "</span>")
print("<span id='dash' style='color:black; display:inline'>-</span>")
print("<span id='segment3' style='color:blue; display:inline'>" + arr[2] + "</span>")

print "<script type='text/javascript' src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>"
print "<script type='text/javascript' src='../js/py-fades.js'></script>"
