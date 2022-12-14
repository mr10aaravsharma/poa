def worstfit(blockSize, processSize):
    print("Worst Fit")
    print(blockSize)
    print(processSize)
    alloc = [-1]*len(processSize)
    for i in range (len(processSize)):
        worst_index = -1
        for j in range(len(blockSize)):
            if(blockSize[j] >= processSize[i]):
                if(worst_index == -1):
                    worst_index = j;
                elif(blockSize[j] >= blockSize[worst_index]):
                    worst_index=j;
        if(worst_index!=-1):
            alloc[i]=worst_index
            blockSize[worst_index]-=processSize[i]
    print("\nProcess No \tProcess Size \tBlock No")
    for i in range(len(processSize)):
        if(alloc[i]!=-1): 
            print((i+1) ,"\t\t", processSize[i],"\t\t", alloc[i])
        else: 
            print("Not Allocated")
    print("Hole Sizes are: " ,blockSize)

def firstfit(blockSize, processSize):
    print("First Fit")
    print(blockSize)
    print(processSize)
    alloc = [-1]*len(processSize)
    for i in range (len(processSize)):
        for j in range(len(blockSize)):
            if(blockSize[j]>= processSize[i]):
                blockSize[j]-=processSize[i]
                alloc[i]=j;
                break;
    print("\nProcess No \tProcess Size \tBlock No")
    for i in range(len(processSize)):
        if(alloc[i]!=-1): 
            print((i+1) ,"\t\t", processSize[i],"\t\t", alloc[i])
        else: 
            print("Not Allocated")
    print("Hole Sizes are: " ,blockSize)

def nextfit(blockSize, processSize):
    print("Next fit")
    print(blockSize)
    print(processSize)
    alloc = [-1]*len(processSize)
    for i in range (len(processSize)):
        next_index = 0
        for j in range(len(blockSize)):
            if(blockSize[j] >= processSize[i]):
                if(next_index == -1):
                    next_index = j;
                else:
                    next_index = (next_index +1)%len(blockSize)
        if(next_index!=-1):
            alloc[i]=next_index
            blockSize[next_index]-=processSize[i]
    print("\nProcess No \tProcess Size \tBlock No")
    for i in range(len(processSize)):
        if(alloc[i]!=-1): 
            print((i+1) ,"\t\t", processSize[i],"\t\t", alloc[i])
        else: 
            print("Not Allocated")
    print("Hole Sizes are: " ,blockSize)

def bestfit(blockSize, processSize):
    print("Best fit")
    print(blockSize)
    print(processSize)
    alloc = [-1]*len(processSize)
    for i in range (len(processSize)):
        best_index = -1
        for j in range(len(blockSize)):
            if(blockSize[j] >= processSize[i]):
                if(best_index == -1):
                    best_index = j;
                elif(blockSize[j]<=blockSize[best_index]):
                    best_index=j;
        if(best_index!=-1):
            alloc[i]=best_index
            blockSize[best_index]-=processSize[i]
    print("\nProcess No \tProcess Size \tBlock No")
    for i in range(len(processSize)):
        if(alloc[i]!=-1): 
            print((i+1) ,"\t\t", processSize[i],"\t\t", alloc[i])
        else: 
            print("Not Allocated")
    print("Hole Sizes are: " ,blockSize)

def main():
    print("Enter Block Sizes: ")
    blockSize = list(map(int, input().split()))
    print("Enter Process Sizes: ")
    processSize = list(map(int, input().split()))
    choice = int(input("Enter 1)Best Fit 2)Worst Fit 3)Next Fit 4)First Fit"))
    if(choice == 1 ):
        bestfit(blockSize, processSize)
    elif(choice ==2):
        worstfit(blockSize, processSize)
    elif(choice == 3):
        nextfit()
    elif(choice ==4):
        firstfit(blockSize, processSize)


if __name__ == '__main__':
    main()  