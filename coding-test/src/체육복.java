import java.util.Arrays;

public class 체육복 {

    public static void main(String[] args) {
        solution(5,	new int[]{2, 4}, new int[]{1, 3, 5});   // 5
        solution(5, new int[]{2, 4}, new int[]{3, 1});  // 5
        solution(3, new int[]{1,2}, new int[]{2,3}); // 2
        solution(5,	new int[]{1,2,3}, new int[]{1,3});   // 4
    }

    public static int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;

        Arrays.sort(lost);
        Arrays.sort(reserve);
        for(int i = 0; i < lost.length; i++){
            for(int j = 0; j < reserve.length; j++){
                if(lost[i] == reserve[j]){
                    lost[i] = -1;
                    reserve[j] = -1;
                    answer++;
                    break;
                }
            }
        }

        for(int i : lost){
            for(int j = 0; j < reserve.length; j++){
                if(Math.abs(i - reserve[j]) == 1) {
                    reserve[j] = -1;
                    answer++;
                    break;
                }
            }
        }

        System.out.println(answer);
        return answer;
    }
}
