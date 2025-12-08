import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

    private static final int[] dx = {-1, 1, 0, 0};
    private static final int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Map<Integer, Set<Integer>> map = new LinkedHashMap<>();

        for (int i = 0; i < n * n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int target = Integer.parseInt(st.nextToken());

            Set<Integer> likes = new HashSet<>(4);
            for (int j = 0; j < 4; j++) {
                likes.add(Integer.parseInt(st.nextToken()));
            }

            map.put(target, likes);
        }

        int score = 0;
        int[][] seating = solution(n, map);

        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                int count = 0;

                for (int d = 0; d < 4; d++) {
                    int nx = x + dx[d];
                    int ny = y + dy[d];

                    if (0 <= nx && nx < n && 0 <= ny && ny < n && map.get(seating[x][y]).contains(seating[nx][ny])) {
                        count++;
                    }
                }

                if (count == 1) {
                    score++;
                } else if (count == 2) {
                    score += 10;
                } else if (count == 3) {
                    score += 100;
                } else if (count == 4) {
                    score += 1000;
                }
            }
        }

        System.out.println(score);
    }

    private static int[][] solution(int n, Map<Integer, Set<Integer>> map) {
        int[][] seating = new int[n][n];

        for (Map.Entry<Integer, Set<Integer>> entry : map.entrySet()) {
            int student = entry.getKey();
            Set<Integer> targets = entry.getValue();

            SeatOption best = null;

            for (int x = 0; x < n; x++) {
                for (int y = 0; y < n; y++) {
                    if (seating[x][y] != 0) {
                        continue;
                    }

                    int likeCount = 0;
                    int blankCount = 0;

                    for (int d = 0; d < 4; d++) {
                        int nx = x + dx[d];
                        int ny = y + dy[d];

                        if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                            continue;
                        }

                        if (seating[nx][ny] == 0) {
                            blankCount++;
                        } else if (isLiked(targets, seating[nx][ny])) {
                            likeCount++;
                        }
                    }

                    SeatOption option = new SeatOption(x, y, likeCount, blankCount);
                    if (best == null || option.isBetterThan(best)) {
                        best = option;
                    }
                }
            }

            seating[best.x][best.y] = student;
        }

        return seating;
    }

    private static boolean isLiked(Set<Integer> targets, int seating) {
        for (int target : targets) {
            if (target == seating) {
                return true;
            }
        }
        return false;
    }

    private static class SeatOption {
        final int x;
        final int y;
        final int likeCount;
        final int blankCount;

        SeatOption(int x, int y, int likeCount, int blankCount) {
            this.x = x;
            this.y = y;
            this.likeCount = likeCount;
            this.blankCount = blankCount;
        }

        boolean isBetterThan(SeatOption other) {
            if (other == null) {
                return true;
            }
            if (this.likeCount != other.likeCount) {
                return this.likeCount > other.likeCount;
            }
            if (this.blankCount != other.blankCount) {
                return this.blankCount > other.blankCount;
            }
            if (this.x != other.x) {
                return this.x < other.x;
            }
            return this.y < other.y;
        }
    }
}