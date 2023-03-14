import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> queue = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            String command = br.readLine();

            if (command.contains("push")) {
                queue.offerLast(Integer.parseInt(command.split(" ")[1]));

            } else if (command.contains("pop")) {

                if (queue.isEmpty()) {
                    System.out.println(-1);
                    continue;
                }

                System.out.println(queue.pollFirst());

            } else if (command.contains("size")) {
                System.out.println(queue.size());

            } else if (command.contains("empty")) {
                System.out.println(queue.isEmpty() ? 1 : 0);

            } else if (command.contains("front")) {

                if (queue.isEmpty()) {
                    System.out.println(-1);
                    continue;
                }

                System.out.println(queue.peekFirst());

            } else if (command.contains("back")) {

                if (queue.isEmpty()) {
                    System.out.println(-1);
                    continue;
                }

                System.out.println(queue.peekLast());
            }
        }

    }

}