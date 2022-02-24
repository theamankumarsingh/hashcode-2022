import os, sys, math

input_data=open(sys.argv[1], 'r').read().splitlines()

CP=list(map(int,input_data[0].split(' ')))
print(CP)
i=1
contributors=dict()
projects=dict()

#
#{BOB:[skill1{name:level}, skill2, skill3]}

# Aman's code
for j in range(CP[0]):
    contributors[input_data[i].split(' ')[0]]=[]
    name=input_data[i].split(' ')[0]
    for k in range(int(input_data[i].split(' ')[1])):
        contributors[name].append(input_data[i+k+1])
    i+=int(input_data[i].split(' ')[1])+1
print(contributors)

#{'WebServer': {'BestBefore': val, "Skills":[], }}
for j in range(CP[1]):
    #print(input_data[i])
    projects[input_data[i].split(' ')[0]]=dict()
    name=input_data[i].split(' ')[0]
    projects[name]['D']=int(input_data[i].split(' ')[1])
    projects[name]['S']=int(input_data[i].split(' ')[2])
    projects[name]['B']=int(input_data[i].split(' ')[3])
    projects[name]['R']=int(input_data[i].split(' ')[4])
    projects[name]['roles']=[]
    for k in range(projects[name]['R']):
        projects[name]['roles'].append(input_data[i+k+1])
    i+=projects[name]['R']+1
print(projects)
