import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader reader;

    static int a, b, c;

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(reader.readLine());
        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int result = solve(a, b);
        System.out.println(result);

    }

    private static int solve(int a, int b) {
        if (b == 1) {
            return a % c;
        }

        long temp = solve(a, b / 2);
        temp = temp * temp % c;
        
        return (int) (b % 2 == 0 ? temp : temp * a % c);
    }
}
