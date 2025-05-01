import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for (int x = 0; x < commands.length; x++) {
            int[] command = commands[x];
            
            int i = command[0] - 1;
            int j = command[1];
            int k = command[2] - 1;
            
            int[] subArray = Arrays.copyOfRange(array, i, j);
            Arrays.sort(subArray);
            answer[x] = subArray[k];
        }
        
        return answer;
    }
}