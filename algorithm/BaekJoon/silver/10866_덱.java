import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            String commands = br.readLine();
            String command = commands.split(" ")[0];

            switch (command) {
                case "push_front":
                    deque.offerFirst(parseData(commands));
                    break;

                case "push_back":
                    deque.offerLast(parseData(commands));
                    break;

                case "pop_front":
                    System.out.println(deque.isEmpty() ? -1 : deque.pollFirst());
                    break;

                case "pop_back":
                    System.out.println(deque.isEmpty() ? -1 : deque.pollLast());
                    break;

                case "size":
                    System.out.println(deque.size());
                    break;

                case "empty":
                    System.out.println(deque.isEmpty() ? 1 : 0);
                    break;

                case "front":
                    System.out.println(deque.isEmpty() ? -1 : deque.peekFirst());
                    break;

                case "back":
                    System.out.println(deque.isEmpty() ? -1 : deque.peekLast());
                    break;

                default:
                    break;
            }


        }

    }

    public static int parseData(String command) {
        return Integer.parseInt(command.split(" ")[1]);
    }

}