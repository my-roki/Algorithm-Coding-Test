import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader reader;

    static String[] arr;

    int a, b, c;

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new java.io.InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(reader.readLine());
        arr = st.nextToken().split("");

        int half = arr.length / 2;
        for (int i = 0; i < half; i++) {
            if (!arr[i].equals(arr[arr.length - i - 1])) {
                System.out.println("0");
                return;
            }
        }
        System.out.println("1");
    }
}
