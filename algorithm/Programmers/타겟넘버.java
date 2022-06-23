public class 타겟넘버 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        sol.solution(new int[]{1, 1, 1, 1, 1}, 3);
//        sol.solution(new int[]{1, 2, 3}, 3);
    }
}

class Solution {
    private int count = 0;

    public int solution(int[] numbers, int target) {
        boolean[] visited = new boolean[numbers.length];
        for(int i = 1; i < numbers.length; i++){
            combination(numbers, visited, 0, numbers.length, i, target);
        }

        return count;
    }

    public void combination(int[] arr, boolean[] visited, int start, int n, int r, int target) {
        if(r == 0) {
            int value = 0;
            for(int i = 0; i < arr.length; i++){
                if(visited[i]){
                    value += arr[i];
                } else {
                    value -= arr[i];
                }
            }

            if(value == target){
                count++;
            }
        }

        for(int i = start; i < n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, r - 1, target);
            visited[i] = false;
        }

    }
}
