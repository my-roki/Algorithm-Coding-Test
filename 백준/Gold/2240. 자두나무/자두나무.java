import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader reader;
    static StringTokenizer st;

    static int[][][] dp = new int[1001][31][3];
    static int[] tree;

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(reader.readLine());

        int T = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        tree = new int[T + 1];
        for (int i = 1; i <= T; i++) {
            tree[i] = Integer.parseInt(reader.readLine());
        }

        // 초기값 설정(초기 위치는 1번 나무)
        if (tree[1] == 1) { // 1번째 자두가 떨어지는 나무가 1번 나무일 때
            dp[1][0][1] = 1; // 1초일 때 0번 움직이고 그대로 있어서(1) 자두를 받음
            dp[1][1][2] = 0; // 1초일 때 1번 움직이고 이동해서(1->2) 자두를 못 받음
        } else { // 1번째 자두가 떨어지는 나무가 2번 나무일 때
            dp[1][0][1] = 0; // 1초일 때 0번 움직이고 그대로 있어서(1) 자두를 못 받음
            dp[1][1][2] = 1; // 1초일 때 1번 움직이고 이동해서(1->2) 자두를 받음
        }

        for (int t = 2; t <= T; t++) {
            // w = 0일 때, 1번 나무에 있는 경우와 2번 나무에 있는 경우
            dp[t][0][1] = dp[t - 1][0][1] + (tree[t] == 1 ? 1 : 0);
            dp[t][0][2] = dp[t - 1][0][2] + (tree[t] == 2 ? 1 : 0);

            for (int w = 1; w <= W; w++) {
                if (tree[t] == 1) { // t번째 자두가 떨어지는 나무가 1번 나무일 때
                    dp[t][w][1] = Math.max(dp[t - 1][w][1], dp[t - 1][w - 1][2]) + 1;
                    dp[t][w][2] = Math.max(dp[t - 1][w][2], dp[t - 1][w - 1][1]);
                } else { // t번째 자두가 떨어지는 나무가 2번 나무일 때
                    dp[t][w][1] = Math.max(dp[t - 1][w][1], dp[t - 1][w - 1][2]);
                    dp[t][w][2] = Math.max(dp[t - 1][w][2], dp[t - 1][w - 1][1]) + 1;
                }
            }
        }

        int result = 0;
        for (int w = 0; w <= W; w++) {
            result = Math.max(result, Math.max(dp[T][w][1], dp[T][w][2]));
        }
        System.out.println(result);
    }
}