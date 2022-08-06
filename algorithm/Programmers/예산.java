import java.util.*;

class Solution {

    public int solution(int[] d, int budget) {
        int answer = d.length;
        int temp = 0;
        Arrays.sort(d);

        for(int i = 0; i < d.length; i++){
            if(temp + d[i] > budget){
                return i;
            }            
            
            temp += d[i];
            
        }
        
        return answer;
    }
    
   
}