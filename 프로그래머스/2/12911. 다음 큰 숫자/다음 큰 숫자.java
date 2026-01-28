class Solution {
    public int solution(int n) {
        int cnt = Integer.bitCount(n);

        for (int x = n + 1; x <= 1_000_000; x++) {
            if (Integer.bitCount(x) == cnt) {
                return x;
            }
        }
        return 0;
    }
}