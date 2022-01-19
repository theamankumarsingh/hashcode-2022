import sys
file=open(sys.argv[1],"r").read().splitlines()
client=int(file[0])
like_ingr={}
final=[]
for i in range(1,client+1):
    like_ingredient=file[2*i-1].split()
    for t in range(len(like_ingredient)):
        if t!=0:
            if like_ingredient[t] in like_ingr.keys():
                like_ingr[like_ingredient[t]]=like_ingr.get(like_ingredient[t])+1
            else:
                like_ingr[like_ingredient[t]]=1
    dislike_ingredient=file[2*i].split()
    for t in range(len(dislike_ingredient)):
        if t!=0:
            if dislike_ingredient[t] in like_ingr.keys():
                like_ingr[dislike_ingredient[t]]=like_ingr.get(dislike_ingredient[t])-1
            else:
                like_ingr[dislike_ingredient[t]]=-1
print(client//3)
for k,v in like_ingr.items():
    if v>=client//client-1:
        final.append(k)
output=str(len(final))
for i in final:
    output=output+" "+i
output_file=open(sys.argv[2],"w")
output_file.write(output)