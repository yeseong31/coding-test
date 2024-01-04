class Count {
    
    private final int zero;
    private final int one;
    
    private Count(final int zero, final int one) {
        this.zero = zero;
        this.one = one;
    }
    
    public static Count of(final int zero, final int one) {
        return new Count(zero, one);
    }
    
    public int addZero(final int zero) {
        return this.zero + zero;
    }
    
    public int addOne(final int one) {
        return this.one + one;
    }
    
    public Count add(final Count other) {
        return new Count(other.addZero(zero), other.addOne(one));
    }
    
    public int[] receiveResult() {
        return new int[] {zero, one};
    }
}


class Solution {
    public int[] solution(int[][] arr) {
        return count(0, 0, arr.length, arr).receiveResult();
    }
    
    private Count count(final int x, final int y, final int size, final int[][] arr) {
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (arr[i][j] != arr[x][y]) {
                    int h = size / 2;
                    return count(x, y, h, arr)
                            .add(count(x + h, y, h, arr))
                            .add(count(x, y + h, h, arr))
                            .add(count(x + h, y + h, h, arr));
                }
            }
        }
        
        if (arr[x][y] == 1) {
            return Count.of(0, 1);
        }
        return Count.of(1, 0);
    }
}
