import java.util.*;

public class 나머지한점 {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[][]{{1, 4}, {3, 4}, {3, 10}})));
        System.out.println(Arrays.toString(solution(new int[][]{{1, 1}, {2, 2}, {1, 2}})));
    }

    public static int[] solution(int[][] v) {
        int[] answer = {0, 0};

        Arrays.stream(v).forEach(i -> {
            answer[0] ^= i[0];
            answer[1] ^= i[1];
        });

        return answer;
    }

//    public static int[] solution(int[][] v) {
//        List<Integer> xLst = new LinkedList<>();
//        List<Integer> yLst = new LinkedList<>();
//        int[] answer = {0, 0};
//
//        Arrays.stream(v).forEach(i -> {
//            xLst.add(i[0]);
//            yLst.add(i[1]);
//        });
//
//        Optional<Integer> x = xLst.stream().filter(i -> Collections.frequency(xLst, i) == 1).findAny();
//        Optional<Integer> y = yLst.stream().filter(i -> Collections.frequency(yLst, i) == 1).findAny();
//
//        answer[0] = x.orElse(-1);
//        answer[1] = y.orElse(-1);
//
//        return answer;
//    }



}

