#!/usr/bin/ruby

require 'cgi'
cgi = CGI.new

puts "Content-type: text/html\n\n"
puts "This is the Ruby script.<br>"
puts cgi['name'].split.map(&:capitalize).join(' ')
puts "<br>"
puts cgi['address'].split.map(&:capitalize).join(' ')
puts "<br>"
$phone =  cgi['phone']
$arr = $phone.split('-')
puts "<link rel='stylesheet' type='text/css' href='../css/lab6-scripts.css'>"
puts "<span id='segment1' style='color:red; display:none'>"+$arr[0]+"</span>"
puts "<span id='segment2' style='color:green; display:none'>"+$arr[1]+"</span>"
puts "<span id='dash' style='color:black; display:none'>-</span>"
puts "<span id='segment3' style='color:blue; display:none'>"+$arr[2]+"</span>"

puts "<script type='text/javascript' src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js'></script>"
puts "<script type='text/javascript' src='../js/rb-fades.js'></script>"
