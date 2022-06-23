public class 키패드누르기 {
    public static void main(String[] args) {
        System.out.println(solution(new int[]{1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5}, "right")); //"LRLLLRLLRRL"
        System.out.println(solution(new int[]{7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2}, "left")); //"LRLLRRLLLRR"
        System.out.println(solution(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}, "right")); //"LLRLLRLLRL"
    }

    public static String solution(int[] numbers, String hand) {
        StringBuilder sb = new StringBuilder();
        int[] leftHand = {3, 0};
        int[] rightHand = {3, 2};

        for(int i : numbers){
            if(i == 0){
                i = 11;
            }

            int xPos = (i - 1) / 3;
            int yPos = (i - 1) % 3;

            int leftHandValue = Math.abs(leftHand[0] - xPos) + Math.abs(leftHand[1] - yPos);
            int rightHandValue = Math.abs(rightHand[0] - xPos) + Math.abs(rightHand[1] - yPos);

            switch (yPos){
                case 0:
                    sb.append("L");
                    leftHand = new int[]{xPos, yPos};
                    break;
                case 1:
                    if(leftHandValue > rightHandValue){
                        sb.append("R");
                        rightHand = new int[]{xPos, yPos};
                    } else if(leftHandValue < rightHandValue){
                        sb.append("L");
                        leftHand = new int[]{xPos, yPos};
                    } else {
                        if (hand.equals("right")) {
                            sb.append("R");
                            rightHand = new int[]{xPos, yPos};
                        } else {
                            sb.append("L");
                            leftHand = new int[]{xPos, yPos};
                        }
                    }
                    break;
                case 2:
                    sb.append("R");
                    rightHand = new int[]{xPos, yPos};
                    break;
                default:
                    break;
            }
        }

        return sb.toString();
    }
}
