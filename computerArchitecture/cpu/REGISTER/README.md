# CPU
## Register
### Software
#### 내부 레지스터
- 프로그램 카운터(Program Counter)
    - 다음에 인출될 명령어 주소를 가짐
    - 인출 후에는 자동적으로 증가
    - 분기 명령 실행 시 목적지 주소로 갱신
- 누산기(Accumulator)
    - 데이터 일시 저장
    - 비트 수 == cpu 한번에 연산 처리량 == word 길이
- 명령어 레지스터(Instruction Register)
    - 가장 최근 인출된 명렁어 저장
- 기억장치 주소 레지스터(Memory Address Register)
    - 프로그램 카운터에 저장된 명령어 일시 저장
    - 시스템 주소 버스로 출력됨
    - 프로그램 카운터를 주소 버스로 전달하는 역할
-  기억장치 버퍼 레지스터(Memory Buffer Register)
    - 기억장치 데이터가 일시 저장
    - 데이터 버스 선과 연결됨
    - CPU로 데이터 입,출력 전달 역할