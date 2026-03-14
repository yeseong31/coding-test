import java.util.*;

public class Solution {
    
    public long solution(int n, int[] works) {
        Arrays.sort(works);
        int len = works.length;

        for (int i = 0; i < len / 2; i++) {
            int temp = works[i];
            works[i] = works[len - 1 - i];
            works[len - 1 - i] = temp;
        }

        while (n > 0) {
            for (int i = 0; i < works.length; i++) {
                works[i] -= 1;
                n -= 1;

                if (n == 0) {
                    long sum = 0;
                    for (int x : works) {
                        if (x > 0) sum += (long) x * x;
                    }
                    return sum;
                }

                if (i < works.length - 1 && works[i] >= works[i + 1]) {
                    break;
                }
            }
        }

        return 0;
    }
}