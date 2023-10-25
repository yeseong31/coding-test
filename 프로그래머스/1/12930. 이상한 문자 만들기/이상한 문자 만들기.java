class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        int index = 0;
        
        for (char c : s.toCharArray()) {
            if (!Character.isAlphabetic(c)) {
                index = 1;
            }
            
            answer.append(convertAlphabet(c, index));
            index++;
        }
        
        return answer.toString();
    }
    
    private char convertAlphabet(char c, int idx) {
        if (idx % 2 == 0) {
            return Character.toUpperCase(c);
        }
        return Character.toLowerCase(c);
    }
}