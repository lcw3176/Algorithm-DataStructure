import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String sentence = br.readLine();
        Character beforeChar = null;
        int piece = 0;

        List<Coord> lst = new ArrayList();
        List<Coord> store = new ArrayList();

        for (char datum : sentence.toCharArray()) {

            if (beforeChar == null) {
                beforeChar = datum;
                continue;
            }

            if (beforeChar == '(' && datum == ')') {
                for (Coord j : lst) {
                    j.hitCount++;
                }
            }

            if (beforeChar == '(' && datum == '(') {
                Coord coord = new Coord();

                lst.add(coord);
            }

            if (beforeChar == ')' && datum == ')') {
                Coord temp = lst.get(lst.size() - 1);
                store.add(temp);
                lst.remove(lst.size() - 1);
            }

            beforeChar = datum;
        }

        for (Coord i : store) {
            piece += i.hitCount;
            piece++;
        }

        System.out.println(piece);

    }

    static class Coord {
        public int hitCount = 0;

    }


}