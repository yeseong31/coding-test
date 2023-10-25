class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        
        for (int x = 0; x < arr1.length; x++) {
            for (int y = 0; y < arr2[0].length; y++) {
                answer[x][y] = calculateMatrix(arr1, arr2, x, y);
            }
        }
        
        return answer;
    }
    
    private int calculateMatrix(int[][] arr1, int[][] arr2, int x, int y) {
        int result = 0;
        
        for (int k = 0; k < arr2.length; k++) {
            result += arr1[x][k] * arr2[k][y];
        }
        
        return result;
    }
}