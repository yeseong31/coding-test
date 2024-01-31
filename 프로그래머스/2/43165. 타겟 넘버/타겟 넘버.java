import java.util.LinkedList;
import java.util.Queue;

class State {
    
    private final int index;
    private final int acc;
    
    public State(int index, int acc) {
        this.index = index;
        this.acc = acc;
    }
    
    public int getIndex() {
        return index;
    }
    
    public int getAcc() {
        return acc;
    }
}

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Queue<State> queue = new LinkedList<>();
        queue.add(new State(0, 0));
        
        while (!queue.isEmpty()) {
            State state = queue.poll();
            int index = state.getIndex();
            int acc = state.getAcc();
            
            if (index == numbers.length) {
                if (acc == target) {
                    answer++;
                }
                continue;
            }
            
            queue.add(new State(index + 1, acc - numbers[index]));
            queue.add(new State(index + 1, acc + numbers[index]));
        }
        
        return answer;
    }
}