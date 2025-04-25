class Solution {
    public int[] solution(long n) {
        String s = Long.toString(n);
        String reversed = new StringBuilder(s).reverse().toString();
        
        int[] answer = new int[reversed.length()];
        for (int i = 0; i < reversed.length(); i++) {
            answer[i] = Character.getNumericValue(reversed.charAt(i));
        }
        return answer;
    }
}