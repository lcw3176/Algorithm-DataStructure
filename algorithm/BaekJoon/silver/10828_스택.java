import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;


class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            String[] commands = br.readLine().split(" ");
            String command = commands[0];

            if (command.equals("push")) {
                Integer data = Integer.parseInt(commands[1]);
                stack.push(data);
            } else if (command.equals("top")) {
                System.out.println(stack.isEmpty() ? -1 : stack.peek());
            } else if (command.equals("size")) {
                System.out.println(stack.size());
            } else if (command.equals("empty")) {
                System.out.println(stack.isEmpty() ? 1 : 0);
            } else if (command.equals("pop")) {
                System.out.println(stack.isEmpty() ? -1 : stack.pop());
            }
        }
    }

}