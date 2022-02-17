def MissingNum(array):
    n=len(array)
    missNum = n*(n+1)/2
    for i in range(n):
        missNum = missNum - array[i]
        missNum=int(missNum)
    return missNum

if __name__ == "__main__" :
    #array = [0,1,2,4]
    #array = [0,2,3,4,5]
    array = [1,4,2,3]
    print('The missing number is', MissingNum(array))

    