import os

file = input("filename: ")
try:
  f = open(file)
except:
  exit()