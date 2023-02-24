import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String[] sentence = br.readLine().split(" ");
            StringBuilder completedSentence = new StringBuilder();

            for (String j : sentence) {
                StringBuilder reversedWord = new StringBuilder();
                char[] data = j.toCharArray();

                for (int k = data.length - 1; k >= 0; k--) {
                    reversedWord.append(data[k]);
                }

                completedSentence.append(reversedWord);
                completedSentence.append(" ");
            }

            completedSentence.delete(completedSentence.length() - 1, completedSentence.length());
            System.out.println(completedSentence);
        }
    }

}