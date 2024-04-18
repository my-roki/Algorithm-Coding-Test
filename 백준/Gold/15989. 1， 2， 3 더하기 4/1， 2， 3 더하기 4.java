import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader reader;
    static StringTokenizer st;

    static int[][] dp = new int[10001][4];

    private static void init() throws Exception {
        reader = new BufferedReader(new InputStreamReader(System.in));
    }

    public static void main(String[] args) throws Exception {
        init();

        int T = Integer.parseInt(reader.readLine());

        dp[1][1] = dp[2][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1;

        for (int i = 4; i <= 10000; i++) {
            dp[i][1] = dp[i - 1][1];
            dp[i][2] = dp[i - 2][1] + dp[i - 2][2];
            dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3];
        }

        StringBuilder sb = new StringBuilder();
        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(reader.readLine());
            sb.append(dp[n][1] + dp[n][2] + dp[n][3] + "\n");
        }

        System.out.println(sb);
    }
}