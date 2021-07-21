from arrayList import ArrayList

if __name__ == "__main__":
    arr = ArrayList()
    
    # add() 테스트
    for i in range(1000):
        arr.add(i)
    arr.display()

    # remove() 테스트
    for i in range(1000):
        arr.remove(0)
    arr.display()

    # clear() 테스트
    for i in range(1000):
        arr.add(i)
    arr.clear()
    arr.display()

    # contains() 테스트
    for i in range(1000):
        arr.add(i)
    print(arr.contains(121)) # True
    print(arr.contains(20000)) # False

    # get() 테스트
    print(arr.get(100)) # 100
    # print(arr.get(5000)) # Exception: 인덱스 초과

    # size() 테스트
    print(arr.size()) # 1000

    # indexOf() 테스트
    print(arr.indexOf(200)) # 200
    print(arr.indexOf(20000)) # -1