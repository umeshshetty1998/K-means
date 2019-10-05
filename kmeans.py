length=int(input("Enter the no of elements :"))
inputList=[]
differenceList=[]
selectedMeanList=[]
newList=[]
oldclusterList=[]
finalList=[]
for x in range (length):
	item=int(input("Enter element : "))
	inputList.append(item)
	
clusterCount=int(input("Enter the no of clusters"))
if(clusterCount>length):
	print("Invalid input")
	exit()
else:
	clusterList=[]
	for i in range(clusterCount):
		clusterList.append(inputList[i])
while True:
        for p in inputList:
                for q in clusterList:
                        diff=abs(p-q)
                        differenceList.append(diff)
                x=differenceList.index(min(differenceList))
                selectedMean=clusterList[x]
                selectedMeanList.append(selectedMean)
                del differenceList[:]
        oldclusterList=clusterList.copy()
        for m in range(clusterCount):
            for n in range(length):
                if clusterList[m]!=selectedMeanList[n]:
                    newList.append(inputList[n])
            clusterList[m]=sum(newList)/len(newList)
            del newList[:] 
        s=set(selectedMeanList)
        newSelectedMeanList=list(s)
        if oldclusterList==clusterList:
                for j in range(clusterCount):
                        for i in range(length):
                                if newSelectedMeanList[j]==selectedMeanList[i]:
                                        finalList.append(inputList[i])
                        print(finalList)
                        del finalList[:]
                exit()
        else:
                del selectedMeanList[:]
                continue
