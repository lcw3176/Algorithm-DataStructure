import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] numbers = br.readLine().split(" ");

        int n = Integer.parseInt(numbers[0]);
        int k = Integer.parseInt(numbers[1]);

        int index = 0;

        boolean[] visited = new boolean[n];
        List<Integer> answer = new ArrayList<>(n);

        while (answer.size() < n) {
            int count = 0;

            while (true) {
                if (!visited[index]) {
                    count++;
                }

                if (count == k) {
                    visited[index] = true;
                    answer.add(index + 1);
                    break;
                }

                index++;

                if (index >= n) {
                    index -= n;
                }
            }

        }

        System.out.println(answer.stream()
                .map(String::valueOf)
                .collect(Collectors.joining(", ", "<", ">")));
    }

}