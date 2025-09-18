class Solution {

    private static int n;
    private static int m;

    public boolean solution(int[][] key, int[][] lock) {
        n = lock.length;
        m = key.length;

        int size = n + 2 * (m - 1);
        int[][] board = new int[size][size];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[m - 1 + i][m - 1 + j] = lock[i][j];
            }
        }

        int[][][] keys = rotateAndSave(key);

        for (int i = 0; i < n + m - 1; i++) {
            for (int j = 0; j < n + m - 1; j++) {
                for (int r = 0; r < 4; r++) {
                    for (int x = 0; x < m; x++) {
                        for (int y = 0; y < m; y++) {
                            board[i + x][j + y] += keys[r][x][y];
                        }
                    }

                    if (isValid(board)) return true;

                    for (int x = 0; x < m; x++) {
                        for (int y = 0; y < m; y++) {
                            board[i + x][j + y] -= keys[r][x][y];
                        }
                    }
                }
            }
        }

        return false;
    }

    private static boolean isValid(int[][] board) {
        for (int i = m - 1; i < m - 1 + n; i++) {
            for (int j = m - 1; j < m - 1 + n; j++) {
                if (board[i][j] != 1) return false;
            }
        }
        
        return true;
    }

    private static int[][][] rotateAndSave(int[][] key) {
        int[][][] keys = new int[4][m][m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                keys[0][i][j] = key[i][j];
            }
        }

        for (int k = 1; k < 4; k++) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < m; j++) {
                    keys[k][i][j] = keys[k - 1][m - j - 1][i];
                }
            }
        }

        return keys;
    }
}