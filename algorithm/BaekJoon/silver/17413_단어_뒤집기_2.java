import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Character> leftStack = new Stack<>();
        Stack<Character> rightStack = new Stack<>();

        char[] sentences = br.readLine().toCharArray();
        boolean signal = false;

        for (int i = 0; i < sentences.length; i++) {
            char data = sentences[i];

            if (data == '<') {
                moveData(leftStack, rightStack);
                signal = true;
            }

            if (data == '>') {
                rightStack.push('>');
                signal = false;
                continue;
            }

            if (signal) {
                rightStack.push(data);
                continue;
            }

            if (data == ' ') {
                moveData(leftStack, rightStack);
                rightStack.push(' ');
            }

            leftStack.push(data);

            if (i == sentences.length - 1) {
                moveData(leftStack, rightStack);

            }

        }

        System.out.println(rightStack.stream()
                .map(String::valueOf)
                .collect(Collectors.joining("")));
    }

    public static void moveData(Stack<Character> left, Stack<Character> right) {
        int size = left.size();

        for (int j = 0; j < size; j++) {
            char data = left.pop();

            if (data != ' ') {
                right.push(data);
            }
        }
    }

}