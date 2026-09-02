class Solution {

    public int solution(String s) {
        if (s.length() % 2 == 1) {
            return 0;
        }

        char[] stack = new char[s.length()];
        int top = 0;

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (top > 0 && stack[top - 1] == current) {
                top--;
            } else {
                stack[top++] = current;
            }
        }

        return top == 0 ? 1 : 0;
    }
}