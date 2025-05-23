import java.util.Arrays;

class Solution {
    public int solution(int[] number) {
        Arrays.sort(number);
        int answer = 0;
        int result;
        
        for (int i = 0; i < number.length - 2; i++) {
            for (int j = i + 1; j < number.length - 1; j++) {
                for (int k = j + 1; k < number.length; k++) {
                    result = number[i] + number[j] + number[k];
                    if (result == 0) {
                        answer++;
                    } else if (result > 0) {
                        break;
                    }
                }
            }
        }
        
        return answer;
    }
}