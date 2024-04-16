import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    static BufferedReader reader;

    static String[] poketmonName;
    static HashMap<String, Integer> poketmonIndex;

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(reader.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        poketmonName = new String[N + 1];
        poketmonIndex = new HashMap<>();

        for (int i = 1; i <= N; i++) {
            String name = reader.readLine();
            poketmonName[i] = name;
            poketmonIndex.put(name, i);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            String query = reader.readLine();
            if (Character.isDigit(query.charAt(0))) {
                int index = Integer.parseInt(query);
                sb.append(poketmonName[index]).append("\n");
            } else {
                sb.append(poketmonIndex.get(query)).append("\n");
            }
        }
        System.out.println(sb);
    }
}
