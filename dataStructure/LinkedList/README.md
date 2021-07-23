# LinkedList

## 개요, 특징
* 노드들로 이어진 리스트
* 시작 노드 head, 끝 노드 tail로 구성
* 가변적 길이. 배열 재할당, 값 복사 불필요
* 데이터를 자주 저장, 삭제하는 상황에 적합

## 장점
*  삽입 
    - O(1)
    - tail에 node추가
* 삭제
    - O(1)
    - node가 가리키는 포인터만 변경하면 끝 (next)
## 단점
* 검색
    - O(n)
    - arrayList에 비해 비교적 느림
* 용량
    - Node로 인한 저장 공간 낭비

## 기타
* 자바 제네릭 사용 가능, 재량
```Java
// Object로 선언됨
LinkedList list = new ArrayList(); 

// 타입 설정
LinkedList<Integer> numList = new LinkedList<Integer>(); 
```

* C# 제네릭 사용, 이중 연결 리스트로 내부 구현
```C#
// 이중 연결
// AddBefore(), AddAfter() 등 특정 노드 앞,뒤 노드 추가 가능
LinkedList<string> list = new LinkedList<string>(); 
list.AddLast("hello");
list.AddLast("new");
list.AddLast("world");

LinkedList<string> foundNode = list.Find("new");
LinkedList<string> newNode = new LinkedList<string>("Monsieur");

list.AddAfter(foundNode, newNode);
``` 