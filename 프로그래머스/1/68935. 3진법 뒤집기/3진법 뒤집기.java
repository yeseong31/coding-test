class Solution {
    public int solution(int n) {
        String converted = Integer.toString(n, 3);
        String reversed = new StringBuilder(converted)
                .reverse()
                .toString();
        return Integer.parseInt(reversed, 3);
    }
}