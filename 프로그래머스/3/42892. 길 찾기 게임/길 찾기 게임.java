import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Node {
    public int x;
    public int y;
    public int v;
    public Node left;
    public Node right;
    
    public Node(int x, int y, int v) {
        this.x = x;
        this.y = y;
        this.v = v;
    }
}

class Tree {
    private Node root;
    
    public boolean insert(int x, int y, int v) {
        root = _insert(root, x, y, v);
        return root != null;
    }
    
    private Node _insert(Node node, int x, int y, int v) {
        if (node == null) {
            return new Node(x, y, v);
        }
        if (x < node.x) {
            node.left = _insert(node.left, x, y, v);
        } else {
            node.right = _insert(node.right, x, y, v);
        }
        return node;
    }
    
    public int[] preorder() {
        return _preorder(root, new ArrayList<>());
    }
    
    private int[] _preorder(Node node, List<Integer> result) {
        if (node != null) {
            result.add(node.v);
            _preorder(node.left, result);
            _preorder(node.right, result);
        }
        return result.stream().mapToInt(Integer::valueOf).toArray();
    }
    
    public int[] postorder() {
        return _postorder(root, new ArrayList<>());
    }
    
    private int[] _postorder(Node node, List<Integer> result) {
        if (node != null) {
            _postorder(node.left, result);
            _postorder(node.right, result);
            result.add(node.v);
        }
        return result.stream().mapToInt(Integer::valueOf).toArray();
    }
}

class Solution {
    public int[][] solution(int[][] nodeinfo) {
        Tree tree = new Tree();
        List<int[]> nodes = new ArrayList<>();

        for (int i = 0; i < nodeinfo.length; i++) {
            int x = nodeinfo[i][0];
            int y = nodeinfo[i][1];
            int k = i + 1;
            nodes.add(new int[] { x, y, k });
        }

        nodes.sort((a, b) -> {
            if (b[1] != a[1]) {
                return b[1] - a[1];
            }
            return a[0] - b[0];
        });

        for (int[] node : nodes) {
            tree.insert(node[0], node[1], node[2]);
        }

        return new int[][] { 
            tree.preorder(), 
            tree.postorder() 
        };
    }
}