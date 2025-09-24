import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[][] solution(int n, int[][] build_frame) {
        boolean[][] pillars = new boolean[n + 1][n + 1];
        boolean[][] beams = new boolean[n + 1][n + 1];
        
        for (int[] row : build_frame) {
            int x = row[0];
            int y = row[1];
            int a = row[2];
            int b = row[3];
            
            if (b == 1) {
                if (a == 0) {
                    pillars[x][y] = true;
                    if (!isValid(pillars, beams, n)) {
                        pillars[x][y] = false;
                    }
                } else {
                    beams[x][y] = true;
                    if (!isValid(pillars, beams, n)) {
                        beams[x][y] = false;
                    }
                }
            } else {
                if (a == 0) {
                    pillars[x][y] = false;
                    if (!isValid(pillars, beams, n)) {
                        pillars[x][y] = true;
                    }
                } else {
                    beams[x][y] = false;
                    if (!isValid(pillars, beams, n)) {
                        beams[x][y] = true;
                    }
                }
            }
        }
        
        List<int[]> result = new ArrayList<>();
        for (int x = 0; x <= n; x++) {
            for (int y = 0; y <= n; y++) {
                if (pillars[x][y]) {
                    result.add(new int[]{x, y, 0});
                }
                if (beams[x][y]) {
                    result.add(new int[]{x, y, 1});
                }
            }
        }
        
        return result.toArray(new int[result.size()][]);
    }
    
    private static boolean isValid(boolean[][] pillars, boolean[][] beams, int n) {
        for (int x = 0; x <= n; x++) {
            for (int y = 0; y <= n; y++) {
                if (pillars[x][y]) {
                    if (y == 0) continue;
                    if (y > 0 && pillars[x][y - 1]) continue;
                    if (beams[x][y]) continue;
                    if (x > 0 && beams[x - 1][y]) continue;
                    return false;
                }
            }
        }
        
        for (int x = 0; x <= n; x++) {
            for (int y = 0; y <= n; y++) {
                if (beams[x][y]) {
                    boolean leftPillar = (y > 0 && pillars[x][y - 1]);
                    boolean rightPillar = (y > 0 && x + 1 <= n && pillars[x + 1][y - 1]);
                    boolean leftBeam = (x > 0 && beams[x - 1][y]);
                    boolean rightBeam = (x + 1 <= n && beams[x + 1][y]);
                    
                    if (leftPillar || rightPillar) continue;
                    if (leftBeam && rightBeam) continue;
                    return false;
                }
            }
        }
        
        return true;
    }
}