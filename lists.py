import time

def makeList(n):
    start = time.time()
    print([m*m for m in range(1,n)])
    end = time.time()
    lapse = end - start
    print(lapse)
    
makeList(10)

def reverseSubList(arr, i, j):
    start = time.time()
    arr2 = arr[i:j+1]
    print(arr2[::-1])
    end = time.time()
    lapse = end - start
    print(lapse)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverseSubList(lst, 2, 5)

def mergeLists(arr1, arr2):
    start = time.time()
    arra = sorted(arr1)
    arrb = sorted(arr2)
    arrc = sorted(arra + arrb)
    print(arrc)
    end = time.time()
    lapse = end - start
    print(lapse)

lst2 = [5, 7, 2, 8, 3, 11]
mergeLists(lst, lst2)


dic1 = {'name': 'fred', 'hobbies' : 'bball, surfing, eating', 'weight': '205'}
dic2 = {'name': 'jeff', 'hobbies' : 'cooking, football', 'weight': '180'}

def mergeDicts(dict1, dict2):
    start = time.time()
    dict1.update(dict2)
    end = time.time()
    lapse = end - start
    print(lapse)
    return dict1

print(mergeDicts(dic1, dic2))

dic1 = {'name': 'fred', 'hobbies' : 'bball, surfing, eating', 'weight': '205'}
dic2 = {'name': 'jeff', 'hobbies' : 'cooking, football', 'weight': '180'}

def intersecDicts(dict1, dict2):
    start = time.time()
    newDic = {x:(dict1[x], dict2[x]) for x in dict1 if x in dict2}
    print(newDic)
    end = time.time()
    lapse = end - start
    print(lapse)

intersecDicts(dic1, dic2)

newlst = ["bear", "cat", "bear", "car", "dog", "coffin", "bear"]
newdic = {'word' : 'bear'}

def countWords(lst, dic):
    start = time.time()
    count = 0
    for word in lst:
        if word == dic['word']:
            count +=1
    print('Bear count: ' + str(count))
    end = time.time()
    lapse = end - start
    print(lapse)

countWords(newlst, newdic)