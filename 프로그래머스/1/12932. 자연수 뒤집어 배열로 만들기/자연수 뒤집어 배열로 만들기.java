class Solution {
    public int[] solution(long n) {
        
        String s = Long.toString(n);
        char[] arr = new StringBuilder(s).reverse()
                .toString()
                .toCharArray();
        
        int[] answer = new int[arr.length];
        
        for (int i = 0; i < arr.length; i++) {
            answer[i] = Character.getNumericValue(arr[i]);
        }
            
        return answer;
    }
}