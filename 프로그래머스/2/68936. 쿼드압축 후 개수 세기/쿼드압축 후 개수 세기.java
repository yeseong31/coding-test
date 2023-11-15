class Solution {
    
    static class Count {
        
        private final int zero;
        private final int one;
        
        private Count(int zero, int one) {
            this.zero = zero;
            this.one = one;
        }
        
        public static Count of(int zero, int one) {
            return new Count(zero, one);
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
    
    public int[] solution(int[][] arr) {
        Count count = calculate(0, 0, arr.length, arr);
        return new int[] {count.getZero(), count.getOne()};
    }
    
    public Count calculate(int sx, int sy, int size, int[][] arr) {
        int h = size / 2;

        for (int x = sx; x < sx + size; x++) {
            for (int y = sy; y < sy + size; y++) {
                if (arr[x][y] != arr[sx][sy]) {
                    return calculate(sx, sy, h, arr)
                            .add(calculate(sx, sy + h, h, arr))
                            .add(calculate(sx + h, sy, h, arr))
                            .add(calculate(sx + h, sy + h, h, arr));
                }
            }
        }

        if (arr[sx][sy] == 0) {
            return Count.of(1, 0);
        }
        return Count.of(0, 1);
    }
}