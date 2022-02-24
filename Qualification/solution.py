def quick_sort(projects_name, projects):
    if len(projects_name)<=1:
        return projects_name
    else:
        pivot=projects[projects_name[0]]['S']
        print(pivot)
        less=[]
        greater=[]
        for i in range(1,len(projects_name)):
            if projects[projects_name[i]]['S']<pivot:
                less.append(projects_name[i])
            else:
                greater.append(projects_name[i])
        print(less,greater)
        return quick_sort(less,projects)+[projects_name[0]]+quick_sort(greater,projects)

import os, sys, math

#input

input_data=open(sys.argv[1], 'r').read().splitlines()

CP=list(map(int,input_data[0].split(' ')))
#print(CP)
i=1
contributors=dict()
contributors_name=[]
projects=dict()
projects_name=[]

#
#{BOB:[skill1{name:level}, skill2, skill3]}
#[{name: bob,skills:[skill1{name:level}, skill2, skill3]}, ]


# Aman's code
for j in range(CP[0]):
    contributors[input_data[i].split(' ')[0]]=[]
    name=input_data[i].split(' ')[0]
    contributors_name.append(name)
    for k in range(int(input_data[i].split(' ')[1])):
        contributors[name].append(input_data[i+k+1])
    i+=int(input_data[i].split(' ')[1])+1
print(contributors)

#{'WebServer': {'BestBefore': val, "Skills":[], }}
for j in range(CP[1]):
    #print(input_data[i])
    projects[input_data[i].split(' ')[0]]=dict()
    name=input_data[i].split(' ')[0]
    projects_name.append(name)
    projects[name]['D']=int(input_data[i].split(' ')[1])
    projects[name]['S']=int(input_data[i].split(' ')[2])
    projects[name]['B']=int(input_data[i].split(' ')[3])
    projects[name]['R']=int(input_data[i].split(' ')[4])
    projects[name]['roles']=[]
    for k in range(projects[name]['R']):
        projects[name]['roles'].append(input_data[i+k+1])
    i+=projects[name]['R']+1
print(projects)

#logic
#quick sort
projects_name=quick_sort(projects_name, projects)
projects_name.reverse()
print(projects_name)
print(projects[projects_name[0]])

assigned_projects = []

for i in range(len(projects_name)):
    d = dict()
    d["name"] = projects_name[i]
    d["assigned"] = []
    for role in projects[projects_name[i]]['roles']:
        for contributor in contributors.keys():
            #skills = contributors[contributor].split(' ')
            #skills = [x.split(' ')[0] for x in contributors[contributor]]
            #print(skills)
            #if role.split(' ')[0] in contributors[contributor]
            contributor_found = False
            for skill in contributors[contributor]:
                if skill.startswith(role.split(' ')[0]) and int(role.split(' ')[1]) <= int(skill.split(' ')[1]):
                    d["assigned"].append(contributor)
                    contributor_found = True
                    #print(contributor, skill, projects_name[i], role)
            if not contributor_found:
                 break        
    assigned_projects.append(d)

print(assigned_projects)