#!/usr/bin/env python
#coding=utf-8
#coding=gbk

#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
# Author   : hao lv (L), hlvpku@gmail.com
# Date     : 13 January 2015
# Version  : 1.0. Initial version.
# Details  : extrate data using python regulation expression.
# Required :            
#IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Header for import statements
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#import sys as sys
import os as os

import re as re

#=========================================================================
# FUNCTIONS
#=========================================================================

#Python Regular Expressions: Basic Patterns
#a, X, 9, < -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves because they have special meanings are: . ^ $ * + ? { [ ] \ | ( ) (details below)
#. (a period) -- matches any single character except newline '\n'
#\w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any non-word character.
#\b -- boundary between word and non-word
#\s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]. \S (upper case S) matches any non-whitespace character.
#\t, \n, \r -- tab, newline, return
#\d -- decimal digit [0-9] (some older regex utilities do not support but \d, but they all support \w and \s)
#^ = start, $ = end -- match the start or end of the string
#\ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash. If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to make sure it is treated just as a character. 

def match_re(str):
  #match = re.search(r'word:<\w+.+>', str) # Greedy match. 
  match = re.search(r'word:<\w+.+?>', str) # Non-Greedy match. \w is similar with [a-zA-Z0-9_]
  if match:
     print 'Match found: ', match.group() ## 'found word:xxx'
  else:
     print 'did not find'

#==========================================================================
# MAIN PROGRAM
#==========================================================================
def main():
  
  addrs = os.getcwd() #absolute path of current directory
  print 'Current path is ' + addrs
 
  #read file in absolute path
  #fh = open(addrs + '\\test.txt') #method #1
  fh = open(addrs + r'\test.txt') #method #1, r is used to avoid escape character, and here is \t.
  #fh = open('C:\\Users\\holv\\Desktop\\test.txt') #method #2
  #fh = open(r'C:\Users\holv\Desktop\test.txt') #method #2, r is used to avoid escape character
  
  #read file in relative path
  #fh = open('test.txt') 

  for line in fh.readlines():
    #print line
    match_re(line)


if __name__ == '__main__':
  main()

