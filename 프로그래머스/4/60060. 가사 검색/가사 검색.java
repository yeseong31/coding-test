import java.lang.StringBuilder;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Trie {
    
    private final List<String> words = new ArrayList<>();
    
    public void add(String word) {
        words.add(word);
    }
    
    public void sort() {
        Collections.sort(words);
    }
    
    public int bisectLeft(String query) {
        int index = Collections.binarySearch(words, query);
        
        if (index < 0) {
            return -index - 1;
        }
        
        return index;
    }
    
    public int bisectRight(String query) {
        int index = Collections.binarySearch(words, query);
        
        if (index < 0) {
            return -index - 1;
        }
        
        return index + 1;
    }
}

class DoubleTrie {
    
    private static final int WORD_LENGTH = 10_001;
    
    private final Trie[] trie = new Trie[WORD_LENGTH];
    private final Trie[] reversedTrie = new Trie[WORD_LENGTH];
    private final Set<Integer> checked = new HashSet<>();
    
    public void add(String word) {
        int length = word.length();
        
        if (!checked.contains(length)) {
            trie[length] = new Trie();
            reversedTrie[length] = new Trie();
        }
        
        checked.add(length);
        trie[length].add(word);
        reversedTrie[length].add(reverse(word));
    }
    
    public void sort() {
        for (int index : checked) {
            trie[index].sort();
            reversedTrie[index].sort();
        }
    }
    
    public int search(String query) {
        int length = query.length();
        
        if (!checked.contains(length)) {
            return 0;
        }
        
        String firstQuery = query.replace('?', 'a');
        String lastQuery = query.replace('?', 'z');
        Trie target;
        
        if (query.charAt(0) != '?') {
            target = trie[length];
        } else {
            target = reversedTrie[length];
            firstQuery = reverse(firstQuery);
            lastQuery = reverse(lastQuery);
        }
        
        return target.bisectRight(lastQuery) - target.bisectLeft(firstQuery);
    }
    
    private String reverse(String word) {
        return new StringBuilder(word).reverse().toString();
    }
}

class Solution {
    
    public int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];
        DoubleTrie doubleTrie = new DoubleTrie();
        
        for (String word : words) {
            doubleTrie.add(word);
        }
        
        doubleTrie.sort();
        
        for (int index = 0; index < queries.length; index++) {
            answer[index] = doubleTrie.search(queries[index]);;
        }
        
        return answer;
    }
}