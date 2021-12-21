public class 문자열압축 {
    public static void main(String[] args) {
        solution("aabbaccc");
        solution("ababcdcdababcdcd");
        solution("abcabcdede");
        solution("abcabcabcabcdededededede");
        solution("xababcdcdababcdcd");
    }

    public static int solution(String s) {
        int piece = 1;

        StringBuilder sb = new StringBuilder();

        for(int i = 1; i <= s.length() / 2; i++){
            String data = s.substring(0, i);

            for(int j = i; j < s.length(); j++){
                if(j + j > s.length()){
                    break;
                }

                sb.append(s, j, j + j);
                if(data.equals(sb.toString())){
                    piece = i;
                }
            }

            sb.setLength(0);
        }

        String beforeValue = s.substring(0, piece);
        int count = 0;

        for(int i = piece; i < s.length(); i += piece){
            if(i + piece > s.length()){
                sb.append(s, i, s.length());
                break;
            }

            String temp = s.substring(i, i + piece);

            if(temp.equals(beforeValue)){
                count++;
            } else {
                if(count > 1){
                    sb.append(count);
                }

                sb.append(beforeValue);
                count = 0;
            }

            beforeValue = temp;
        }

        System.out.println(sb);

        return 1;
    }
}
