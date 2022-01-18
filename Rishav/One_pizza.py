import sys
file=open(sys.argv[1],"r").read().splitlines()
client=int(file[0])
like_ingr=[]
dislike_ingr=[]
for i in range(1,client+1):
    like_ingredient=file[2*i-1].split()
    for t in range(len(like_ingredient)):
        if t!=0:
            like_ingr.append(like_ingredient[t])
    dislike_ingredient=file[2*i].split()
    for t in range(len(dislike_ingredient)):
        if t!=0:
            dislike_ingr.append(dislike_ingredient[t])
len_like_ingr=len(like_ingr)
len_dislike_ingr=len(dislike_ingr)
i=0
t=0
while i<len_like_ingr:
    check=1
    t=0
    while t<len_dislike_ingr:
        if like_ingr[i]==dislike_ingr[t]:
            del dislike_ingr[t]
            del like_ingr[i]
            check=0
            len_dislike_ingr=len(dislike_ingr)
            len_like_ingr=len(like_ingr)
        else:
            t=t+1
    if check==1:
        i=i+1
unique_ingr=[]
for x in like_ingr:
    if x not in unique_ingr:
        unique_ingr.append(x)
output=str(len(unique_ingr))
for i in unique_ingr:
    output=output+" "+unique_ingr[i]
output_file=open(sys.argv[2],"w")
output_file.write(output)