import java.util.Stack;

public class 크레인인형뽑기게임 {

    public static void main(String[] args) {
        System.out.println(solution(
                new int[][]{{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}},
                new int[]{1,5,3,5,1,2,1,4})); // 4

        System.out.println(solution(
                new int[][]{{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1},{1,1,1,1,1}},
                new int[]{1,5,3,5,1,2,1,4})); // 4
    }

    public static int solution(int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<>();

        int answer = 0;
        int peekValue = 0;

        for(int i = 0; i < moves.length; i++){
            int index = 0;

            while(index < board[0].length){
                int value = board[index][moves[i] - 1];

                if(value != 0){
                    if(peekValue == value){
                        stack.pop();

                        if(stack.size() == 0){
                            peekValue = 0;
                        } else {
                            peekValue = stack.peek();
                        }

                        answer += 2;

                    } else {
                        stack.push(value);
                        peekValue = value;
                    }

                    board[index][moves[i] - 1] = 0;
                    break;
                }
                index++;
            }
        }

        return answer;
    }
}
