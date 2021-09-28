# BFS (너비 우선 탐색)
## 개요, 특징
- 루트 노드 or 임의의 시작 노드에서 인접한 노드를 먼저 탐색
- 시작 정점 -> 가까운 정점 -> 멀리 떨어진 정점
- 두 노드 사이의 최단 경로 or 임의의 경로 탐색
- 구현 방법
    - 반복문
    - 큐
- 시간 복잡도
    - 인접 행렬: O(V^2) 
    - 인접 리스트: O(V + E) 
- 용어 정리
    - V(Vertex): 노드, 정점 
    - E(edge): 노드 간 연결선, 간선 
    - arc: 방향성 엣지
<div>
    <img src="https://user-images.githubusercontent.com/59993347/135012975-a3caf234-f263-4211-8628-0bc962471546.png">
    <p>출처 https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/</p>
</div>


## 대표적인 문제들
- 탐색
- 최단 거리
- 최소 시간
- 최적의 해

 
