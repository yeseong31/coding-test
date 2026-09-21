class Solution {
    
    public long solution(int w, int h) {
        long gcd = gcd(w, h);
        return (long) w * h - (w + (long) h - gcd);
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = a % b;
            a = b;
            b = temp;
        }

        return a;
    }
}