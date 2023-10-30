import java.util.*;


class Solution {

    static class HanoiGame {

        private static final List<Hanoi> result = new ArrayList<>();

        private HanoiGame() {
        }

        public static HanoiGame of() {
            return new HanoiGame();
        }

        public int[][] process() {
            List<List<Integer>> info = new ArrayList<>();

            for (Hanoi hanoi : result) {
                info.add(hanoi.receiveInfo());
            }

            int r = info.size();
            int c = info.get(0).size();
            int[][] answer = new int[r][c];

            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    answer[i][j] = info.get(i).get(j);
                }
            }
            
            return answer;
        }

        public void execute(int n, int start, int mid, int end) {
            if (n == 1) {
                result.add(Hanoi.of(start, mid, end));
                return;
            }

            execute(n - 1, start, end, mid);
            execute(1, start, mid, end);
            execute(n - 1, mid, start, end);
        }
    }

    static class Hanoi {

        private final int start;
        private final int mid;
        private final int end;

        private Hanoi(int start, int mid, int end) {
            this.start = start;
            this.mid = mid;
            this.end = end;
        }

        public static Hanoi of(int start, int mid, int end) {
            return new Hanoi(start, mid, end);
        }

        public List<Integer> receiveInfo() {
            List<Integer> tmp = new ArrayList<>();
            tmp.add(start);
            tmp.add(end);
            return tmp;
        }
    }

    public int[][] solution(int n) {
        HanoiGame hanoiGame = HanoiGame.of();
        hanoiGame.execute(n, 1, 2, 3);
        return hanoiGame.process();
    }
}