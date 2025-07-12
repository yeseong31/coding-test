import java.util.Arrays;

class Solution {
    private static final int[][] maxDp = new int[202][202];
    private static final int[][] minDp = new int[202][202];
    
    private static int max(int start, int end, String[] arr) {
        if (end - start == 1) {
            return Integer.parseInt(arr[start]);
        } 
        if (maxDp[start][end] > Integer.MIN_VALUE) {
            return maxDp[start][end];
        }
        
        for (int mid = start + 1; mid < end; mid += 2) {
            int v;
            
            if (arr[mid].equals("+")) {
                v = max(start, mid, arr) + max(mid + 1, end, arr);
            } else {
                v = max(start, mid, arr) - min(mid + 1, end, arr);
            }
            
            maxDp[start][end] = Math.max(maxDp[start][end], v);
        }
        
        return maxDp[start][end];
    }
    
    private static int min(int start, int end, String[] arr) {
        if (end - start == 1) {
            return Integer.parseInt(arr[start]);
        } 
        if (minDp[start][end] < Integer.MAX_VALUE) {
            return minDp[start][end];
        }
        
        for (int mid = start + 1; mid < end; mid += 2) {
            int v;

            if (arr[mid].equals("+")) {
                v = min(start, mid, arr) + min(mid + 1, end, arr);
            } else {
                v = min(start, mid, arr) - max(mid + 1, end, arr);
            }
            
            minDp[start][end] = Math.min(minDp[start][end], v);
        }

        return minDp[start][end];
    }
    
    public int solution(String arr[]) {
        for (int[] row : maxDp) Arrays.fill(row, Integer.MIN_VALUE);
        for (int[] row : minDp) Arrays.fill(row, Integer.MAX_VALUE);
        
        return max(0, arr.length, arr);
    }
}