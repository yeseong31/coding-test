import java.util.HashMap;
import java.util.Map;

class Solution {

    static class Node {
        int count;
        Map<Character, Node> children = new HashMap<>();
    }

    static class Trie {
        private final Node root = new Node();

        public void insert(String word) {
            Node node = root;

            for (char ch : word.toCharArray()) {
                node.children.putIfAbsent(ch, new Node());
                node = node.children.get(ch);
                node.count++;
            }
        }

        public int find(String word) {
            Node node = root;

            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);
                node = node.children.get(ch);

                if (node.count == 1) {
                    return i + 1;
                }
            }

            return word.length();
        }
    }

    public int solution(String[] words) {
        Trie trie = new Trie();

        for (String word : words) {
            trie.insert(word);
        }

        int answer = 0;

        for (String word : words) {
            answer += trie.find(word);
        }

        return answer;
    }
}