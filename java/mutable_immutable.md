# Mutable - Immutable
## String
<div style="text-align:center;">
<image src="https://img1.daumcdn.net/thumb/R1280x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/xTa/image/a-dK-z0Ot2TCAyoDM_Db9KTTD8g.png">
<p>출처: https://brunch.co.kr/@kd4/1</p>
</div>


```java
  public static void main(String[] args) {
        String immutable = "hello";
        String shallowCopy = immutable;
        String staticImmutable = new String("hello");
        String constant = "constant";
        String staticConstant = new String("constant");
        String brandNew = new String("good");
        String brandNewGood = new String("good");
        String brandNewTwo = new String("goodTwo");
        String brandNewGoodTwo = new String("goodTwo");

        printHash(
            immutable, shallowCopy, staticImmutable, 
            constant, staticConstant, 
            brandNew,brandNewGood, 
            brandNewTwo, brandNewGoodTwo);
    }

    public static void printHash(String... data){

        for(String i : data){
            System.out.print("데이터: " + i + "  ");
            System.out.print("해시코드: " + i.hashCode() + "  ");
            System.out.println("객체주소: " + System.identityHashCode(i));
        }

    }
```
```java
## result

데이터: hello       해시코드: 99162322      객체주소: 2052915500
데이터: hello       해시코드: 99162322      객체주소: 2052915500
데이터: hello       해시코드: 99162322      객체주소: 1121172875
데이터: constant    해시코드: -567811164    객체주소: 649734728
데이터: constant    해시코드: -567811164    객체주소: 1595953398
데이터: good        해시코드: 3178685       객체주소: 998351292
데이터: good        해시코드: 3178685       객체주소: 1684106402
데이터: goodTwo     해시코드: 207008847     객체주소: 335471116
데이터: goodTwo     해시코드: 207008847     객체주소: 1308927845
```

- 대표적인 Immutable 객체

## StringBuilder, StringBuffer