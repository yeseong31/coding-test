class Solution {
    
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        int[] students = new int[n + 2];
        
        for (int l : lost) {
            students[l]--;
        }
        for (int r : reserve) {
            students[r]++;
        }
        
        for (int index = 1; index <= n; index++) {
            if (students[index] != -1) {
                continue;
            }
            if (students[index - 1] == 1) {
                students[index - 1]--;
                students[index]++;
                continue;
            }
            if (students[index + 1] == 1) {
                students[index + 1]--;
                students[index]++;
                continue;
            }
            answer--;
        }
        
        return answer;
    }
}