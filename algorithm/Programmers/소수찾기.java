import java.util.*;
import java.util.stream.*;
 
class Solution {
    List<Integer> temp = new LinkedList<>();
    
    public int solution(String numbers) {
        int[] arr = Stream.of(numbers.split(""))
            .mapToInt(Integer::parseInt)
            .toArray();
        
        boolean[] visited = new boolean[arr.length];
        int[] output = new int[arr.length];
        
        for(int i = 1; i <= arr.length; i++){
             permutation(arr, output, visited, 0, arr.length, i);
        }
        
        
        for(int i = 0; i < temp.size(); i++){
            int val = temp.get(i);
            
            for(int j = 2; j < val; j++){
                if(val % j == 0){
                    temp.set(i, -1);
                    break;
                }
            }
        }

        return Long.valueOf(temp.stream()
            .filter(i -> i != -1)
            .count()).intValue();
    }
    
    public void permutation(int[] arr, int[] output, boolean[] visited, int depth, int n, int r) {
        if (depth == r) {
            StringBuilder tempSb = new StringBuilder();
            
            for(int i = 0; i < r; i++){
                tempSb.append(output[i]);
            }
            
            int value = Integer.parseInt(tempSb.toString());

            if(!temp.contains(value) && value != 0 && value != 1){
                temp.add(value);
            }
            
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i] != true) {
                visited[i] = true;
                output[depth] = arr[i];
                permutation(arr, output, visited, depth + 1, n, r);
                visited[i] = false;
            }
        }
    }
}