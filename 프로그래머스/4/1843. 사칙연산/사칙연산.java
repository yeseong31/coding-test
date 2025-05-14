import java.util.Arrays;

class Solution {
    private final int[][] maxDp = new int[202][202];
    private final int[][] minDp = new int[202][202];
    private final int inf = 100_000_000;
    
    private int getMax(int start, int end, String[] arr) {
        if (maxDp[start][end] != -inf) {
            return maxDp[start][end];
        }
        if (end - start == 1) {
            return Integer.parseInt(arr[start]);
        }
        
        int result = -inf;
        int v;
        
        for (int opIndex = start + 1; opIndex < end; opIndex += 2) {
            if (arr[opIndex].equals("+")) {
                v = getMax(start, opIndex, arr) + getMax(opIndex + 1, end, arr);
            } else {
                v = getMax(start, opIndex, arr) - getMin(opIndex + 1, end, arr);
            }
            result = Math.max(result, v);
        }
        
        maxDp[start][end] = result;
        return result;
    }
    
    private int getMin(int start, int end, String[] arr) {
        if (minDp[start][end] != inf) {
            return minDp[start][end];
        }
        if (end - start == 1) {
            return Integer.parseInt(arr[start]);
        }
        
        int result = inf;
        int v;
        
        for (int opIndex = start + 1; opIndex < end; opIndex += 2) {
            if (arr[opIndex].equals("+")) {
                v = getMin(start, opIndex, arr) + getMin(opIndex + 1, end, arr);
            } else {
                v = getMin(start, opIndex, arr) - getMax(opIndex + 1, end, arr);
            }
            result = Math.min(result, v);
        }
        
        minDp[start][end] = result;
        return result;
    }
        
    public Solution() {
        for (int[] row : maxDp) {
            Arrays.fill(row, -inf);
        }
        for (int[] row : minDp) {
            Arrays.fill(row, inf);
        }
    }
        
    public int solution(String arr[]) {
        return getMax(0, arr.length, arr);
    }
}