import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public String solution(int[] numbers) {
        return Arrays.stream(numbers)
                .boxed()
                .map(String::valueOf)
                .sorted((v1, v2) -> {
                    Integer n1 = Integer.parseInt(v1 + v2);
                    Integer n2 = Integer.parseInt(v2 + v1);
                    return n2 - n1;
                })
                .collect(Collectors.joining(""))
                .replaceAll("^0+", "0");
    }
}