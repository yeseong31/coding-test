import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;

        Integer[] arr = Arrays.stream(score).boxed().toArray(Integer[]::new);
        Arrays.sort(arr, Collections.reverseOrder());

        for (int i = 0; i < arr.length; i++) {
            if (i % m == 0 && i + m <= arr.length) {
                int min = arr[i];
                for (int j = i; j < i + m; j++) {
                    min = Math.min(min, arr[j]);
                }
                answer += min;
            }
        }

        return answer * m;
    }
}