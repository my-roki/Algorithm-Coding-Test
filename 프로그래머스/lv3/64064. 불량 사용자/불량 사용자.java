import java.util.Arrays;
import java.util.HashSet;

public class Solution {
    private boolean[] check;  // 방문 배열
    private HashSet<String> set;  // 경우의 수를 담기위한 HashSet

    public int solution(String[] user_id, String[] banned_id) {
        check = new boolean[user_id.length];
        set = new HashSet<String>();

        // 정규식표현을 위해 '*'를 '.'로 바꾼다.
        // 정규식표현에서 '.'은 해당 위치의 모든 문자를 대변한다.
        for (int i = 0; i < banned_id.length; i++)
            banned_id[i] = banned_id[i].replace('*', '.');

        back(0, "", banned_id, user_id);  // 조합

        return set.size();
    }

    private void back(int depth, String res, String[] banned_id, String[] user_id) {
        if (depth == banned_id.length) {  // 불량유저 id 개수만큼 조합이 만들질때 종료
            // 조합된 아아디 배열에 담고 정렬
            String[] arr = res.split(" ");
            Arrays.sort(arr);

            String str = "";
            for (String s : arr)
                str += s;  // 정렬된 id들을 하나의 문자열로 추가
            set.add(str);  // 중복되는 경우의수는 HashSet로 하나만 남음.

            return;
        }

        for (int i = 0; i < user_id.length; i++) {  // 유저 id 조합
            // 이미 쓴 유저 id or 불량 id중 '.'을 제외하고 유저 id랑 다른 부분이 있으면 탐색안함.
            if (check[i] || !user_id[i].matches(banned_id[depth]))
                continue;
            check[i] = true;
            back(depth + 1, user_id[i] + " " + res, banned_id, user_id);
            check[i] = false;
        }
    }
}