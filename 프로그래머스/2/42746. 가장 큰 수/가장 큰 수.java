import java.util.Arrays;


class Solution {
    public String solution(int[] numbers) {
        return Arrays.stream(numbers)
                .mapToObj(String::valueOf)
                .sorted((x, y) -> (y + x).compareTo(x + y))
                .reduce((x, y) -> x + y)
                .filter(s -> !s.startsWith("0"))
                .orElse("0");
    }
}