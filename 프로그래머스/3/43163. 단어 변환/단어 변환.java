import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    class Element {
        private final Set<String> checked = new HashSet<>();
        
        public String word;
        public int seq;
        
        public Element(String word, int seq) {
            this.word = word;
            this.seq = seq;
        }
        
        public boolean isChecked(String word) {
            return checked.contains(word);
        }
        
        public void check(String word) {
            checked.add(word);
        }
    }
    
    public int solution(String begin, String target, String[] words) {
        if (!List.of(words).contains(target)) {
            return 0;
        }
        
        int answer = words.length + 1;
        
        Deque<Element> queue = new ArrayDeque<>();
        queue.add(new Element(begin, 0));
        
        int seq;
        String word;
        
        while (!queue.isEmpty()) {
            Element e = queue.pollFirst();
            seq = e.seq;
            word = e.word;
            
            if (seq > words.length) {
                continue;
            }
            if (word.equals(target)) {
                return seq;
            }
                
            for (String next : words) {
                if (e.isChecked(next)) {
                    continue;
                }
                
                int count = 0;
                for (int i = 0; i < word.length(); i++) {
                    if (word.charAt(i) == next.charAt(i)) {
                        count++;
                    }
                }
                
                if (count == word.length() - 1) {
                    e.check(next);
                    queue.offerLast(new Element(next, seq + 1));
                }
            }
        }
        
        return 0;
    }
}