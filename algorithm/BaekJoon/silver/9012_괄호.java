import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;


class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            Stack<Character> stack = new Stack<>();

            for (char j : str.toCharArray()) {
                stack.push(j);

                if (stack.size() >= 2) {
                    char rightExpected = stack.pop();
                    char leftExpected = stack.pop();

                    if (rightExpected != ')' || leftExpected != '(') {
                        stack.push(leftExpected);
                        stack.push(rightExpected);
                    }
                }

            }

            System.out.println(stack.isEmpty() ? "YES" : "NO");
        }
    }
}