import java.util.Arrays;

class Solution {
    public double solution(int[] arr) {
        double sumValue = Arrays.stream(arr).sum();
        return sumValue / arr.length;
    }
}