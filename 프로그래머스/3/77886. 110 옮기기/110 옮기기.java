import java.util.ArrayList;
import java.util.List;

class Solution {
    
    private String[] count(String x) {
        int res = 0;
        List<Character> stack = new ArrayList<>();

        for (int i = 0; i < x.length(); i++) {
            char c = x.charAt(i);

            if (c != '0' || stack.size() < 2 || stack.get(stack.size() - 1) != '1' || stack.get(stack.size() - 2) != '1') {
                stack.add(c);
                continue;
            }

            stack.remove(stack.size() - 1);
            stack.remove(stack.size() - 1);
            res++;
        }

        StringBuilder sb = new StringBuilder();
        for (char ch : stack) {
            sb.append(ch);
        }

        return new String[]{sb.toString(), String.valueOf(res)};
    }

    public String[] solution(String[] s) {
        String[] answer = new String[s.length];

        for (int idx = 0; idx < s.length; idx++) {
            String[] result = count(s[idx]);
            String trans = result[0];
            int cnt = Integer.parseInt(result[1]);

            boolean check = false;
            for (int i = trans.length() - 1; i >= 0; i--) {
                if (trans.charAt(i) == '0') {
                    StringBuilder sb = new StringBuilder();
                    sb.append(trans, 0, i + 1);
                    for (int j = 0; j < cnt; j++) {
                        sb.append("110");
                    }
                    sb.append(trans.substring(i + 1));
                    answer[idx] = sb.toString();
                    check = true;
                    break;
                }
            }

            if (!check) {
                StringBuilder sb = new StringBuilder();
                for (int j = 0; j < cnt; j++) {
                    sb.append("110");
                }
                sb.append(trans);
                answer[idx] = sb.toString();
            }
        }

        return answer;
    }
}