import java.util.HashMap;
import java.util.Map;

class Node {
	public final Map<Character, Node> children;
	public boolean isEnd;
    public int count;
    
	public Node() {
		this.children = new HashMap<>();
		this.isEnd = false;
        this.count = 0;
	}
}

class Trie {
	public final Node root;

	public Trie() {
		this.root = new Node();
	}

	private int countWildcardMatches(Node node, String suffix) {
		if (suffix.isEmpty()) {
			return node.isEnd ? 1 : 0;
		}

		char c = suffix.charAt(0);
		int count = 0;

		if (c == '?') {
			for (Node child : node.children.values()) {
				count += countWildcardMatches(child, suffix.substring(1));
			}
            return count;
		}
        
        if (!node.children.containsKey(c)) {
            return 0;
        }
        
        count += countWildcardMatches(node.children.get(c), suffix.substring(1));
		return count;
	}

	public void insert(String word) {
		Node node = root;
        root.count++;
		
        for (char c : word.toCharArray()) {
			node.children.putIfAbsent(c, new Node());
			node = node.children.get(c);
            node.count++;
		}
        
		node.isEnd = true;
	}

	public int search(String word) {
		Node node = root;
        
		for (int i = 0; i < word.length(); i++) {
			char c = word.charAt(i);
            
			if (c == '?') {
                return node.count;
			}
			if (!node.children.containsKey(c)) {
				return 0;
			}
            
			node = node.children.get(c);
		}
        
		return node.isEnd ? 1 : 0;
	}
}

class DoubleTrie {
    private final Map<Integer, Trie> trieMap;
    private final Map<Integer, Trie> reverseTrieMap;
    
    public DoubleTrie() {
        this.trieMap = new HashMap<>();
        this.reverseTrieMap = new HashMap<>();
    }
    
    public void insert(String word) {
        int n = word.length();
        String reversed = new StringBuilder(word).reverse().toString();
        
        this.trieMap.putIfAbsent(n, new Trie());
        this.trieMap.get(n).insert(word);
        
        this.reverseTrieMap.putIfAbsent(n, new Trie());
        this.reverseTrieMap.get(n).insert(reversed);
    }
    
    public int search(String word) {
        int n = word.length();
        
        if (!this.trieMap.containsKey(n)) {
            return 0;
        }
        if (word.charAt(0) == '?') {
            String reversed = new StringBuilder(word).reverse().toString();
            return this.reverseTrieMap.get(n).search(reversed);
        }
        
        return this.trieMap.get(n).search(word);
    }
}

class Solution {
	public int[] solution(String[] words, String[] queries) {
        int n = queries.length;
		int[] answer = new int[n];
        
        DoubleTrie dt = new DoubleTrie();
        for (String word : words) {
            dt.insert(word);
        }
        
        for (int i = 0; i < n; i++) {
            answer[i] = dt.search(queries[i]);
        }
        
		return answer;
	}
}