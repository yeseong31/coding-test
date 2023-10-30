class Solution {

    static class Counts {

        private final int[][] arr;

        private Counts(final int[][] arr) {
            this.arr = arr;
        }

        public static Counts of(final int[][] arr) {
            return new Counts(arr);
        }

        public Count dfs(final int x, final int y, final int size) {
            int w = size / 2;

            for (int i = x; i < x + size; i++) {
                for (int j = y; j < y + size; j++) {
                    if (arr[i][j] != arr[x][y]) {
                        return dfs(x, y, w)
                                .add(dfs(x + w, y, w))
                                .add(dfs(x, y + w, w))
                                .add(dfs(x + w, y + w, w));
                    }
                }
            }

            if (arr[x][y] == 0) {
                return new Count(1, 0);
            }
            return new Count(0, 1);
        }
    }

    static class Count {

        private final int zero;
        private final int one;

        public Count(final int zero, final int one) {
            this.zero = zero;
            this.one = one;
        }

        public int getZero() {
            return zero;
        }

        public int getOne() {
            return one;
        }

        public Count add(Count other) {
            return new Count(zero + other.getZero(), one + other.getOne());
        }
    }

    public int[] solution(final int[][] arr) {
        Count count =  Counts.of(arr)
                .dfs(0, 0, arr.length);

        return new int[] {count.getZero(), count.getOne()};
    }
}