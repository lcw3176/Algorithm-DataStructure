import java.util.*;

public class 모의고사 {

    public static void main(String[] args) {
        solution(new int[]{5, 5, 4, 2, 3});
    }

    public static int[] solution(int[] answers) {
        Map<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i < 3; i++){
            map.put(i, 0);
        }

        int[] one = new int[]{1, 2, 3, 4, 5};
        int[] two = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] three = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        for(int i = 0; i < answers.length; i++){
            map.put(0, one[i % one.length] == answers[i] ?  map.get(0) + 1 : map.get(0));
            map.put(1, two[i % two.length] == answers[i] ?  map.get(1) + 1 : map.get(1));
            map.put(2, three[i % three.length] == answers[i] ?  map.get(2) + 1 : map.get(2));
        }


        List<Map.Entry<Integer, Integer>> entryList = new LinkedList<>(map.entrySet());
        entryList.sort(Map.Entry.<Integer, Integer>comparingByValue().reversed());

        List<Integer> answer = new LinkedList<>();
        int index = 0;
        int maxValue = 0;
        for(Map.Entry<Integer, Integer> entry : entryList){
            if(entry.getValue() > 0 && entry.getValue() >= maxValue){
                answer.add(index++, entry.getKey() + 1);
                maxValue = entry.getValue();
            }
        }

        int[] arr = new int[answer.size()];


        for(int i = 0; i < answer.size(); i++){
            arr[i] = answer.get(i);
        }

        return arr;
    }
}
