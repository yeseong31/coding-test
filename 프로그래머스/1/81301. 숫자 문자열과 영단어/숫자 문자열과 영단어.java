class Solution {
    
    private static final String[] numbers = {"zero", "one", "two", "three" ,"four", "five", "six", "seven", "eight", "nine"};
    
    public int solution(String s) {
        for (int index = 0; index < 10; index++) {
            s = s.replace(numbers[index], Integer.toString(index));
        }
        return Integer.parseInt(s);
    }
}
