import java.util.*;

class Solution {

    private int n;
    private boolean[][] pillars;
    private boolean[][] beams;

    public int[][] solution(int n, int[][] buildFrame) {
        this.n = n;
        pillars = new boolean[n + 2][n + 2];
        beams = new boolean[n + 2][n + 2];

        for (int[] row : buildFrame) {
            int x = row[0], y = row[1], a = row[2], b = row[3];
            boolean[][] target = (a == 0) ? pillars : beams;

            target[x][y] = (b == 1);
            if (!isFrameValid()) target[x][y] = (b == 0);
        }

        List<int[]> result = new ArrayList<>();
        for (int x = 0; x <= n; x++) {
            for (int y = 0; y <= n; y++) {
                if (pillars[x][y]) result.add(new int[]{x, y, 0});
                if (beams[x][y]) result.add(new int[]{x, y, 1});
            }
        }

        return result.toArray(new int[0][]);
    }

    private boolean isFrameValid() {
        for (int x = 0; x <= n; x++) {
            for (int y = 0; y <= n; y++) {
                if (pillars[x][y] && !isPillarValid(x, y)) return false;
                if (beams[x][y] && !isBeamValid(x, y)) return false;
            }
        }
        return true;
    }

    private boolean isPillarValid(int x, int y) {
        return y == 0
                || pillars[x][y - 1]
                || hasBeam(x, y)
                || hasBeam(x - 1, y);
    }

    private boolean isBeamValid(int x, int y) {
        return hasPillar(x, y - 1)
                || hasPillar(x + 1, y - 1)
                || (hasBeam(x - 1, y) && hasBeam(x + 1, y));
    }

    private boolean hasPillar(int x, int y) {
        return x >= 0 && x <= n && y >= 0 && y <= n && pillars[x][y];
    }

    private boolean hasBeam(int x, int y) {
        return x >= 0 && x <= n && y >= 0 && y <= n && beams[x][y];
    }
}