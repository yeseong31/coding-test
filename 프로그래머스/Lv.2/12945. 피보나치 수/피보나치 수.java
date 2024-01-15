class Solution {
    public int solution(int n) {
        int left = 0;
        int right = 1;
        
        for (int index = 3; index < n + 1; index++) {
            int temp = (left + right) % 1_234_567;
            left = right;
            right = temp;
        }
        
        return (left + right) % 1_234_567;
    }
}