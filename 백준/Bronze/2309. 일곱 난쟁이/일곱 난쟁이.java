import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static BufferedReader reader;

    static int[] heights;
    static List<Integer> selectedHeights;
    static int sum;

    public static void main(String[] args) throws Exception {
        reader = new BufferedReader(new InputStreamReader(System.in));

        int n = 9;
        heights = new int[n];
        for (int i = 0; i < n; i++) {
            heights[i] = Integer.parseInt(reader.readLine());
            sum += heights[i];
        }

        // 9명 중 2명을 뽑아 sum에서 뺀 값이 100이 되는 경우를 찾는다.
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (sum - heights[i] - heights[j] == 100) {

                    // 2명을 제외한 나머지 7명의 키를 저장한다.
                    selectedHeights = new ArrayList<>();
                    for (int k = 0; k < n; k++) {
                        if (k != i && k != j) {
                            selectedHeights.add(heights[k]);
                        }
                    }
                    break;
                }
            }
        }

        // 오름차순 정렬
        Collections.sort(selectedHeights);

        StringBuilder result = new StringBuilder();
        for (int height : selectedHeights) {
            result.append(height).append("\n");
        }
        System.out.println(result.toString());
    }
}
