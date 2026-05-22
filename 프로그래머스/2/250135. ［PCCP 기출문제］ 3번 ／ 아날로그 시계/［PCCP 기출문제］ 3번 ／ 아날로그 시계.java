public class Solution {
    
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        return getCount(h2, m2, s2) - getCount(h1, m1, s1) + (s1 == 0 && m1 == 0 && (h1 % 12) == 0 ? 1 : (s1 == 0 && m1 == 0 ? 1 : 0));
    }

    private int getCount(int h, int m, int s) {
        int mCount = h * 59 + m;
        int hCount = h * 60 + m;
        int result = -1;

        double curMDegree = m * 6.0;
        double curHDegree = 30.0 * (h % 12) + 0.5 * m + (1.0 / 120.0) * s;

        if (curMDegree <= 5.9 * s) {
            mCount++;
        }

        if (curHDegree <= (6.0 - 1.0 / 120.0) * s) {
            hCount++;
        }

        if (h >= 12) {
            hCount--;
            result--;
        }

        return result + mCount + hCount;
    }
}