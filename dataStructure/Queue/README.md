# Queue

## 개요, 특징
* FIFO, 선입선출, 대기열
* Back으로 데이터 입력, Front로 데이터 출력
* 앞과 뒤의 인덱스를 나타내는 front, rear 존재
* 데이터 입력은 enqueue, 데이터 출력은 dequeue
* 순차처리, BFS

## 장점
*  삽입 
    - O(1)
    - back에 데이터 추가
* 삭제
    - O(1)
    - front에서 데이터 인출
## 단점
* 탐색
    - 중간에 위치한 데이터 접근 힘듬

## 기타
* 스택과 반대로 동작
* 음악 재생 프로그램 만들때 많이 사용함, [StrawberryM](https://github.com/lcw3176/StrawberryM)
    - 다음 재생곡
    - 노래 다운로드 대기열