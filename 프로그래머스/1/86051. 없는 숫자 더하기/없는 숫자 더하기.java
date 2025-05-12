import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] numbers) {
        int answer = 45;
        for (int n : numbers) {
            answer -= n;
        }
        return answer;
    }
}