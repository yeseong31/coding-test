import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class State {
    
    private final int depth;
    private final String word;
    
    public State(int depth, String word) {
        this.depth = depth;
        this.word = word;
    }
    
    public int getDepth() {
        return depth;
    }
    
    public String getWord() {
        return word;
    }
}

class Solution {
    
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) {
            return 0;
        }
        
        Queue<State> queue = new LinkedList<>();
        queue.add(new State(0, begin));
        
        while (!queue.isEmpty()) {
            State state = queue.poll();
            
            if (state.getWord().equals(target)) {
                return state.getDepth();
            }
            if (state.getDepth() > words.length) {
                return 0;
            }
            
            for (String word : words) {
                if (isOneCharDiff(word, state.getWord())) {
                    queue.add(new State(state.getDepth() + 1, word));
                }
            }
        }
        
        return 0;
    }
    
    private boolean isOneCharDiff(String wordA, String wordB) {
        int count = 0;
        
        for (int index = 0; index < wordA.length(); index++) {
            if (wordA.charAt(index) == wordB.charAt(index)) {
                count++;
            }
        }
        
        return count == wordA.length() - 1;
    }
}