public class 신규아이디추천 {

    public static void main(String[] args) {
        solution("...!@BaT#*..y.abcdefghijklm");
        solution("z-+.^.");
        solution("=.=");
        solution("123_.def");
        solution("abcdefghijklmn.p");
    }

    public static String solution(String newId) {
        String firstId = first(newId);
        String secondId = second(firstId);
        String thirdId = third(secondId);
        String fourthId = fourth(thirdId);
        String fifthId = fifth(fourthId);
        String sixthId = sixth(fifthId);
        String seventhId = seventh(sixthId);

        return seventhId;
    }

    public static String first(String id){
        return id.toLowerCase();
    }

    public static String second(String id){
        return id.replaceAll("[^a-z0-9-_.]", "");
    }

    public static String third(String id){
        return id.replaceAll("\\.{2,}", ".");
    }

    public static String fourth(String id){
        if(id.charAt(0) == '.'){
            id = id.replaceFirst(".", "");
        }

        if(id.lastIndexOf(".") == id.length() - 1){
            String newId = "";
            for(int i = 0; i < id.length() - 1; i++){
                newId += id.charAt(i);
            }

            id = newId;
        }

        return id;
    }

    public static String fifth(String id){
        if(id.isEmpty()){
            id = "a";
        }

        return id;
    }

    public static String sixth(String id){
        if(id.length() >= 16){
            id = id.substring(0, 15);

            if(id.charAt(id.length() - 1) == '.'){
                id = id.substring(0, 14);
            }
        }

        return id;
    }

    public static String seventh(String id){
        if(id.length() <= 2){
            char lastWord = id.charAt(id.length() - 1);

            while (id.length() < 3){
                id += lastWord;
            }
        }

        return id;
    }
}
