class Solution {
    
    private static final int[][] lines = {{0, 1, 2, 3}, {0, 2, 1, 3}, {0, 3, 1, 2}};
    
    public int solution(int[][] dots) {
        for (int[] line : lines) {
            double lineA = receiveSlope(dots[line[0]], dots[line[1]]);
            double lineB = receiveSlope(dots[line[2]], dots[line[3]]);
            
            if (lineA == lineB) {
                return 1;
            }
        }
        
        return 0;
    }
    
    private double receiveSlope(int[] dotA, int[] dotB) {
        return (double) (dotA[1] - dotB[1]) / (dotA[0] - dotB[0]);
    }
}