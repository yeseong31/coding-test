import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};

    private static int n;
    private static int[][] seating;
    private static int[][] likes;
    private static int[] order;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        seating = new int[n][n];
        likes = new int[n * n + 1][4];
        order = new int[n * n];

        for (int i = 0; i < n * n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int student = Integer.parseInt(st.nextToken());
            order[i] = student;
            for (int j = 0; j < 4; j++) {
                likes[student][j] = Integer.parseInt(st.nextToken());
            }
        }

        seatStudents();
        System.out.println(calcScore());
    }

    private static void seatStudents() {
        for (int student : order) {
            int bestX = 0, bestY = 0;
            int bestLike = -1, bestBlank = -1;

            for (int x = 0; x < n; x++) {
                for (int y = 0; y < n; y++) {

                    if (seating[x][y] != 0) {
                        continue; // 이미 자리 있음
                    }

                    int likeCnt = 0;
                    int blankCnt = 0;

                    for (int d = 0; d < 4; d++) {
                        int nx = x + dx[d];
                        int ny = y + dy[d];

                        if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                            continue;
                        }

                        if (seating[nx][ny] == 0) {
                            blankCnt++;
                        } else {
                            for (int like : likes[student]) {
                                if (like == seating[nx][ny]) {
                                    likeCnt++;
                                }
                            }
                        }
                    }

                    if (likeCnt > bestLike ||
                            (likeCnt == bestLike && blankCnt > bestBlank) ||
                            (likeCnt == bestLike && blankCnt == bestBlank && (x < bestX ||
                                    (x == bestX && y < bestY)))) {

                        bestLike = likeCnt;
                        bestBlank = blankCnt;
                        bestX = x;
                        bestY = y;
                    }
                }
            }
            seating[bestX][bestY] = student;
        }
    }

    private static int calcScore() {
        int score = 0;

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                int student = seating[x][y];
                int likeCount = 0;

                for (int d = 0; d < 4; d++) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                        continue;
                    }

                    for (int like : likes[student]) {
                        if (like == seating[nx][ny]) {
                            likeCount++;
                        }
                    }
                }

                if (likeCount > 0) {
                    score += (int) Math.pow(10, likeCount - 1);
                }
            }
        }
        return score;
    }
}