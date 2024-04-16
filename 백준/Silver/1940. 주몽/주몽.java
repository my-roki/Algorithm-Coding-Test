import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader reader;

    static int left, right;
    static int sum;

    static int result = 0;

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(reader.readLine());
        int m = Integer.parseInt(reader.readLine());

        Integer[] arr = new Integer[n];
        StringTokenizer st = new StringTokenizer(reader.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        left = 0;
        right = n - 1;
        while (left < right) {
            sum = arr[left] + arr[right];
            if (sum == m) {
                // System.out.println(arr[left] + " " + arr[right]);
                left++;
                result++;
            } else if (sum < m) {
                left++;
            } else {
                right--;
            }
        }

        System.out.println(result);
    }
}
