import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static StringBuilder stringBuilder = new StringBuilder();

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int stage = s.nextInt(10);

        BigInteger result = new BigInteger("1");
        if (stage == 1) {
            System.out.println(1);
        } else {
            for (int i = 0; i < stage; i++) {
                result = result.multiply(new BigInteger("2"));
            }
            result = result.subtract(new BigInteger("1"));
            System.out.println(result);
        }

        if (stage <= 20) {
            hanoi(1, 3, stage);
        }
        System.out.println(stringBuilder.toString());
    }

    public static void hanoi(int start, int end, int stage) {
        if (stage == 1) {
            stringBuilder.append(start).append(" ").append(end).append("\n");
        } else {
            int rest = 6 - start - end;
            hanoi(start, rest, stage - 1);
            stringBuilder.append(start).append(" ").append(end).append("\n");
            hanoi(rest, end, stage - 1);
        }
    }
}