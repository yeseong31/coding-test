import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Node {
    
    private final int x;
    private final int y;
    private final int v;
    
    private Node left;
    private Node right;
    
    private Node(int x, int y, int v) {
        this.x = x;
        this.y = y;
        this.v = v;
    }
    
    public static Node of(int x, int y, int v) {
        return new Node(x, y, v);
    }
    
    public int getX() {
        return x;
    }
    
    public int getY() {
        return y;
    }
    
    public Node getLeft() {
        return left;
    }
    
    public Node getRight() {
        return right;
    }
    
    public int getV() {
        return v;
    }
    
    public void insert(Node node) {
        if (node.getX() < x) {
            if (left == null) {
                left = node;
            } else {
                left.insert(node);
            }
        } else {
            if (right == null) {
                right = node;
            } else {
                right.insert(node);
            }
        }
    }
}

class Solution {
    
    public int[][] solution(int[][] nodeinfo) {
        Node[] nodes = new Node[nodeinfo.length];
        
        for (int index = 0; index < nodeinfo.length; index++) {
            int x = nodeinfo[index][0];
            int y = nodeinfo[index][1];
            nodes[index] = Node.of(x, y, index + 1);
        }
        
        Arrays.sort(nodes, (a, b) -> b.getY() - a.getY());
        
        Node root = construct(nodes);
        
        List<Integer> preOrderResult = new ArrayList<>();
        preOrder(root, preOrderResult);
        
        List<Integer> postOrderResult = new ArrayList<>();
        postOrder(root, postOrderResult);
        
        return new int[][] {
            preOrderResult.stream().mapToInt(Integer::intValue).toArray(),
            postOrderResult.stream().mapToInt(Integer::intValue).toArray(),
        };
    }    
    
    private Node construct(Node[] nodes) {
        for (int index = 1; index < nodes.length; index++) {
            nodes[0].insert(nodes[index]);
        }
        
        return nodes[0];
    }
    
    private void preOrder(Node node, List<Integer> result) {
        if (node == null) {
            return;
        }
        
        result.add(node.getV());
        preOrder(node.getLeft(), result);
        preOrder(node.getRight(), result);
    }
    
    private void postOrder(Node node, List<Integer> result) {
        if (node == null) {
            return;
        }
        
        postOrder(node.getLeft(), result);
        postOrder(node.getRight(), result);
        result.add(node.getV());
    }
}