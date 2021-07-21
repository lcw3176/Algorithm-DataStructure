# ArrayList

## 개요, 특징
* 배열을 이용한 리스트
* 가변 길이
* 연속된 메모리 공간 활용, LinkedList에 비해 메모리 절약
* 저장된 데이터를 검색을 자주 하는 상황에 적합 

## 장점
* 검색
    - O(1) 
    - 인덱스를 통한 접근
* 가변 길이
    - 크기에 신경쓰지 않아도 됨

## 단점
* 추가
    - O(n)
    - 한 칸씩 뒤로 미뤄야함
* 삭제
    - O(n)
    - 한 칸씩 앞으로 땡겨야함

## 기타
* 자바에서는 제네릭 타입 지정 가능
```Java
ArrayList<Integer> list = new ArrayList<Integer>();
```

* C#에서는 박싱, 언박싱 과정 거쳐야함. 타입을 강제할 땐 List 사용
```C#
// 박싱, 언박싱 필연적 -> 속도 저하
ArrayList list = new ArrayList();

// 타입 지정 -> 속도 향상, 디버깅 편의성
List<int> list = new List<int>(); 
``` 
