import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader reader;

    static int[] arr = new int[26];

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(reader.readLine());
        for (int i = 0; i < n; i++) {
            String st = new StringTokenizer(reader.readLine()).nextToken();
            char c = st.charAt(0);
            arr[c - 'a']++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            if (arr[i] >= 5) {
                sb.append((char) (i + 'a'));
            }
        }
        System.out.println(sb.length() == 0 ? "PREDAJA" : sb.toString());
    }
}
