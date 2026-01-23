import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int m, int n, String[] board) {
        List<List<Character>> newBoard = rotate(board);
        int[][] visited = new int[n][m];
        int answer = 0;

        while (true) {
            int cnt = 0;

            for (int a = 0; a < n - 1; a++) {
                for (int b = 0; b < m - 1; b++) {
                    if (check(a, b, newBoard, visited)) {
                        cnt++;
                    }
                }
            }

            if (cnt <= 0) {
                break;
            }

            answer += delete(m, n, newBoard, visited);
        }

        return answer;
    }

    private List<List<Character>> rotate(String[] board) {
        int row = board.length;
        int col = board[0].length();

        char[][] a = new char[row][col];
        for (int i = 0; i < row; i++) {
            a[i] = board[i].toCharArray();
        }

        List<List<Character>> result = new ArrayList<>();
        for (int c = 0; c < col; c++) {
            List<Character> list = new ArrayList<>();
            for (int r = 0; r < row; r++) {
                list.add(a[row - 1 - r][c]);
            }
            result.add(list);
        }
        return result;
    }

    private boolean check(int x, int y, List<List<Character>> b, int[][] v) {
        char cur = b.get(x).get(y);
        if (cur != '0'
                && cur == b.get(x + 1).get(y)
                && cur == b.get(x).get(y + 1)
                && cur == b.get(x + 1).get(y + 1)) {
            v[x][y] = 1;
            v[x + 1][y] = 1;
            v[x][y + 1] = 1;
            v[x + 1][y + 1] = 1;
            return true;
        }
        return false;
    }

    private int delete(int m, int n, List<List<Character>> b, int[][] v) {
        int c = 0;

        for (int i = 0; i < n; i++) {
            for (int j = m - 1; j >= 0; j--) {
                if (v[i][j] == 1) {
                    v[i][j] = 0;
                    b.get(i).remove(j);
                    b.get(i).add('0');
                    c++;
                }
            }
        }

        return c;
    }
}