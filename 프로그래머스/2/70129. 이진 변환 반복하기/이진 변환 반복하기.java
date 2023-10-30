class Solution {
    public int[] solution(String s) {
        int count = 0;
        int removedZero = 0;
        int target;

        while (!s.equals("1")) {
            count++;
            target = countZero(s);
            removedZero += target;
            s = Integer.toString(s.length() - target, 2);
        }

        return new int[]{count, removedZero};
    }

    private int countZero(String s) {
        long count = s.chars()
                .filter(c -> c == '0')
                .count();
        
        return Long.valueOf(count)
                .intValue();
    }
}