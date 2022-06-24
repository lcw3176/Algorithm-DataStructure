# SSL
## 용어 정리
- Symmetric key = 대칭키 = 세션키
- IKE(Internet Key Exchange)

## 비대칭 키를 이용한 방식
### 키 쌍 생성
- PC public key + PC private key
- Server public key + Server private key

### public 키 교환
- PC public key -> server 전달
- Server public key -> PC 전달


### public 키를 이용한 암호화
- PC -> Server
    - PC는 Server의 public key를 이용해 평문 암호화, 전송
    - Server는 자신의 private key를 이용해 복호화

- Server -> PC
    - Server는 PC의 public key를 이용해 평문 암호화, 전송
    - PC는 자신의 private key를 이용해 복호화

### 한계
- 키 쌍 생성에 드는 자원이 많음
- 소모한 자원에 비해 사용 시간도 짧음

## 비대칭 키 + 대칭 키 혼합 방식 (IKE)
### Server 키 쌍 미리 생성
- 통신 전에 미리 키 쌍을 생성, 저장해 놓음

### PC 대칭키 생성
- PC Sym Key 생성

### 키 교환
- Server -> PC
    - Server public key 전송

- PC -> Server
    - PC Sym Key 자체를 Server의 public key로 암호화 후 전송
    - Server의 private key로 PC의 Sym key 복호화

### 데이터 전송
- PC -> Server
    - PC Sym Key로 평문 암호화, 전송
    - Server는 복호화했던 PC의 Sym Key로 암호화된 데이터 복호화
