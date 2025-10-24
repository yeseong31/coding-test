class Solution {
    public int solution(String name) {
        int n = name.length();
        int count = 0;

        for (int i = 0; i < n; i++) {
            char ch = name.charAt(i);
            count += Math.min(ch - 'A', 'Z' - ch + 1);
        }

        int minStep = n - 1;

        for (int i = 0; i < n; i++) {
            int next = i + 1;
            
            while (next < n && name.charAt(next) == 'A') {
                next++;
            }
            
            minStep = Math.min(minStep, Math.min(2 * i + (n - next), i + 2 * (n - next)));
        }

        return count + minStep;
    }
}