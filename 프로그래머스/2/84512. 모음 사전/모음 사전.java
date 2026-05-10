class Solution {
    
    public int solution(String word) {
        String v = "AEIOU";
        int[] weights = {781, 156, 31, 6, 1};
        int answer = word.length();

        for (int i = 0; i < word.length(); i++) {
            answer += v.indexOf(word.charAt(i)) * weights[i];
        }

        return answer;
    }
}