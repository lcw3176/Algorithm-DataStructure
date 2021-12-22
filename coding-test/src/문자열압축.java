import java.util.*;

public class 문자열압축 {
    public static void main(String[] args) {
//        System.out.println(solution(""));
        System.out.println(solution(""));
        System.out.println(solution("aabbaccc"));
        System.out.println(solution("ababcdcdababcdcd"));
        System.out.println(solution("abcabcdede"));
        System.out.println(solution("abcabcabcabcdededededede"));
        System.out.println(solution("xababcdcdababcdcd"));
    }

    public static int solution(String s) {
        StringBuilder sb = new StringBuilder();
        StringBuilder temp = new StringBuilder();

        Stack<String> stack = new Stack<>();
        int index = 1;
        int minLength = 2000;

        if(s.length() <= 1){
            return s.length();
        }

        while (index <= s.length() / 2){
            int count = 0;

            for(int i = 0; i < s.length(); i++){
                temp.append(s, i, i + 1);
                count++;

                if(count == index){
                    stack.push(temp.toString());
                    temp.setLength(0);
                    count = 0;
                }
            }

            if(temp.length() > 0){
                stack.push(temp.toString());
                temp.setLength(0);
            }

            String recentValue = stack.pop();
            int size = stack.size();
            HashMap<String, Integer> map = new HashMap<>();


            for(int i = 0; i < size; i++){
                String oldValue = stack.pop();

                if(recentValue.equals(oldValue)){
                    if(map.containsKey(recentValue)){
                        map.put(recentValue, map.get(recentValue) + 1);
                    } else {
                        map.put(recentValue, 2);
                    }
                } else {
                    if(map.containsKey(recentValue)){
                        sb.insert(0, recentValue);
                        sb.insert(0, map.get(recentValue));
                        map.put(recentValue, 0);
                    } else {
                        sb.insert(0, recentValue);
                    }
                }

                if(stack.size() == 0){
                    if(map.containsKey(oldValue)){
                        sb.insert(0, oldValue);
                        sb.insert(0, map.get(oldValue));
                        map.put(oldValue, 0);
                    } else {
                        sb.insert(0, oldValue);
                    }
                }

                recentValue = oldValue;
            }

            index++;

            if(sb.length() < minLength){
                minLength = sb.length();
                System.out.println(sb);
            }
            sb.setLength(0);
        }

        return minLength;
    }
}
