import java.util.Arrays;

public class 로또의최고순위최저순위 {

    public static void main(String[] args) {
        solution(new int[]{44, 1, 0, 0, 31, 25}, new int[]{31, 10, 45, 1, 6, 19}); // [3, 5]
        solution(new int[]{0, 0, 0, 0, 0, 0}, new int[]{38, 19, 20, 40, 15, 25}); // [1, 6]
        solution(new int[]{45, 4, 35, 20, 3, 9}, new int[]{20, 9, 3, 45, 4, 35}); // [1, 1]
        solution(new int[]{2, 2, 2, 2, 2, 2}, new int[]{1, 1, 1, 1, 1, 1}); // [1, 1]
    }

    public static int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int count = 0;
        int zeroCount = 0;

        for(int i : lottos){
            if(i == 0 || Arrays.stream(win_nums).anyMatch(j -> j == i)){
                count++;
            }

            if(i == 0){
                zeroCount++;
            }
        }

        if(zeroCount == 6){
            zeroCount--;
        }

        if(count == 0){
            count++;
        }

        answer[0] = Math.abs(count - 7);
        answer[1] = Math.abs(count - zeroCount - 7) ;

        return answer;
    }
}
