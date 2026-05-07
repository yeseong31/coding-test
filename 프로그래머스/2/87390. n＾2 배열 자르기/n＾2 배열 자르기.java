import java.util.stream.LongStream;

class Solution {
    
    public int[] solution(int n, long left, long right) {
        return LongStream.rangeClosed(left, right)
                .mapToInt(v -> (int) Math.max(v / n, v % n) + 1)
                .toArray();
    }
}