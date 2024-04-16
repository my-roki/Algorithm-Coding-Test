import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader reader;

    static int[] arr = new int[100];

    int a, b, c;

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new java.io.InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(reader.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(reader.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            for (int j = n; j < m; j++) {
                arr[j]++;
            }
        }

        int result = 0;
        for (int i = 0; i < 100; i++) {
            if (arr[i] == 1) {
                result += a;
            } else if (arr[i] == 2) {
                result += b * 2;
            } else if (arr[i] == 3) {
                result += c * 3;
            }
        }
        System.out.println(result);
    }
}
