class Solution {
    
    public int solution(int[][] signals) {
        int n = signals.length;

        int[] cycles = new int[n];
        for (int i = 0; i < n; i++) {
            int g = signals[i][0];
            int y = signals[i][1];
            int r = signals[i][2];
            cycles[i] = g + y + r;
        }
        
        int limit = cycles[0];
        for (int i = 1; i < n; i++) {
            limit = lcm(limit, cycles[i]);
        }
        
        for (int time = 1; time <= limit; time++) {
            boolean flag = true;
            
            for (int i = 0; i < n; i++) {
                int g = signals[i][0];
                int y = signals[i][1];
                int r = signals[i][2];
                
                int cycle = cycles[i];
                int timeInCycle = (time - 1) % cycle + 1;

                if (!(timeInCycle > g && timeInCycle <= g + y)) {
                    flag = false;
                    break;
                }
            }
            
            if (flag) return time;
        }
        
        return -1;
    }
    
    private int gcd(int x, int y) {
        return y == 0 ? x : gcd(y, x % y);
    }

    private int lcm(int x, int y) {
        return x / gcd(x, y) * y;
    }
}