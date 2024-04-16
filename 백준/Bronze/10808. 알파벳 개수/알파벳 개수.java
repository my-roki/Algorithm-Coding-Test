import java.io.BufferedReader;

public class Main {
    static BufferedReader reader;

    static int[] arr = new int[26];

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new java.io.InputStreamReader(System.in));

        char[] input = reader.readLine().toCharArray();
        for (char s : input) {
            byte num = (byte) s;
            arr[num - 97]++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]).append(" ");
        }
        System.out.println(sb.toString());
    }
}