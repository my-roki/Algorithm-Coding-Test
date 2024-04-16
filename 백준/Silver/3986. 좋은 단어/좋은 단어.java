import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader reader;

    static String[] arr;
    static int result = 0;

    static Stack<String> stack = new Stack<>();

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(reader.readLine());

        for (int i = 0; i < n; i++) {
            arr = new StringTokenizer(reader.readLine()).nextToken().split("");

            for (String s : arr) {
                if (stack.isEmpty()) {
                    stack.push(s);
                } else {
                    if (stack.peek().equals(s)) {
                        stack.pop();
                    } else {
                        stack.push(s);
                    }
                }
            }

            if (stack.isEmpty()) {
                result++;
            }
            stack.clear();
        }

        System.out.println(result);
    }
}
