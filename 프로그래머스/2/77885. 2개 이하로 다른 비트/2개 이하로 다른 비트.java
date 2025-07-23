import java.util.*;

public class Solution {

    public static List<Long> solution(long[] numbers) {
        List<Long> answer = new ArrayList<>();
        for (long number : numbers) {
            answer.add(findResult(number));
        }
        return answer;
    }

    private static long findResult(long x) {
        if (x % 2 == 0) {
            return x + 1;
        }

        String binary = "0" + Long.toBinaryString(x);
        int idx = binary.lastIndexOf('0');

        StringBuilder sb = new StringBuilder(binary);
        sb.setCharAt(idx, '1');
        sb.setCharAt(idx + 1, '0');

        return Long.parseLong(sb.toString(), 2);
    }
}