import java.util.Arrays;
import java.util.List;
import java.lang.StringBuilder;


class Solution {
    public String solution(String s) {
        char[] array = s.toCharArray();
        Arrays.sort(array);
        return new StringBuilder(new String(array)).reverse().toString();
    }
}