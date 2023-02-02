class Solution {
    public int[] solution(int brown, int yellow) {
        int total = brown + yellow;
        int[] answer = new int[2];
        
        for(int i = 3; i <= total; i++){
            if(i * i > total){
                break;
            }
            
            if(total % i == 0){
                int brownHeight = i * 2;
                int brownWidth = total / i * 2 - 4;
                
                if(brownHeight + brownWidth == brown){
                    answer[0] = total / i;
                    answer[1]= i;
                    break;
                }
            }
        }
        
        
        return answer;
    }
}