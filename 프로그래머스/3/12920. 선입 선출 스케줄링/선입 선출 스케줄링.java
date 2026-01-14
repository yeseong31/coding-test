import java.util.*;

class Solution {

    public int solution(int n, int[] cores) {
        int m = cores.length;

        if (n <= m) return n;

        int remain = n - m;
        long left = 1;
        long right = (long) Arrays.stream(cores).max().getAsInt() * remain;

        while (left < right) {
            long mid = (left + right) / 2;
            long done = 0;
            for (int c : cores) done += mid / c;

            if (done >= remain) right = mid;
            else left = mid + 1;
        }

        long targetTime = left;
        long doneBefore = 0;
        
        for (int c : cores) doneBefore += (targetTime - 1) / c;

        long need = remain - doneBefore;

        for (int i = 0; i < m; i++) {
            if (targetTime % cores[i] == 0) {
                need--;
                if (need == 0) return i + 1; 
            }
        }

        return -1;
    }
}