import java.util.*;

class Solution {
    
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int s : section) {
            stack.addLast(s);
        }
        
        while (!stack.isEmpty()) {
            answer++;
            int point = stack.removeLast();
            
            while (!stack.isEmpty() && stack.peekLast() > point - m) {
                stack.removeLast();
            }
        }
        
        return answer;
    }
}