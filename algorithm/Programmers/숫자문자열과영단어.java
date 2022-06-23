import java.util.Arrays;
import java.util.List;

public class 숫자문자열과영단어 {

    public static void main(String[] args) {
        solution("one4seveneight");
        solution("23four5six7");
        solution("2three45sixseven");
        solution("123");
    }

    public static int solution(String s) {
        List<String> elements = Arrays.asList("zero", "one", "two", "three", "four", "five","six","seven","eight", "nine");

        for(int i = 0; i < elements.size(); i++){
            s = s.replaceAll(elements.get(i), Integer.toString(i));

        }

        return Integer.parseInt(s);
    }
}
