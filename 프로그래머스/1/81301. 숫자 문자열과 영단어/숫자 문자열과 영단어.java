class Solution {
    
    private static final String[] NUMBER_WORDS = {
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    };

    public int solution(String s) {
        for (int i = 0; i < NUMBER_WORDS.length; i++) {
            s = s.replace(NUMBER_WORDS[i], String.valueOf(i));
        }
        return Integer.parseInt(s);
    }
}