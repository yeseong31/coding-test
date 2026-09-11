import java.util.Arrays;

class Solution {
    
    public int solution(int[] citations) {
        Arrays.sort(citations);

        int n = citations.length;

        for (int i = 0; i < n; i++) {
            int citation = citations[n - 1 - i];
            int paperCount = i + 1;

            if (citation < paperCount) {
                return i;
            }
        }

        return n;
    }
}