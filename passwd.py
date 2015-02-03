#!/usr/bin/phyton

file = open("/etc/passwd" , "r")
list = file.readlines()
dictionary = {}

for line in list:
    list2 = line.split(':')
    user = list2[0]
    shell = list2[len(list2)-1]
    dictionary[user] = shell
	
print "Root:", dictionary["root"]

try: 
    print "Imaginario: ", dictionary["imaginario"]
except KeyError:
    print "Usuario 'imaginario' incorrecto\n"

n_users = len(dictionary) 
print "Numero de usuarios:", n_users, "\n"
	

