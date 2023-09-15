import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> count = new HashMap<>();
        for (String[] clothe : clothes) {
            String clothType = clothe[1];
            if (count.containsKey(clothType)) {
                count.put(clothType, count.get(clothType) + 1);
            } else {
                count.put(clothType, 1);
            }
        }

        int answer = 1;
        for (String key : count.keySet()) {
            answer *= (count.get(key) + 1);
        }

        return answer - 1;
    }
}