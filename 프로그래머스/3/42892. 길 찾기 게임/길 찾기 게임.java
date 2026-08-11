import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

class Solution {
    
    static class Node {
        final int x, y, v;
        Node left, right;
        Node(int x, int y, int v) {
            this.x = x;
            this.y = y;
            this.v = v;
        }
    }

    private static void insert(Node root, Node node) {
        Node cur = root;
        while (true) {
            if (node.x < cur.x) {
                if (cur.left == null) {
                    cur.left = node;
                    return;
                }
                cur = cur.left;
            } else {
                if (cur.right == null) {
                    cur.right = node;
                    return;
                }
                cur = cur.right;
            }
        }
    }

    private static void preOrder(Node root, List<Integer> result) {
        if (root == null) return;
        Deque<Node> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            result.add(node.v);
            if (node.right != null) stack.push(node.right);
            if (node.left != null) stack.push(node.left);
        }
    }

    private static void postOrder(Node root, List<Integer> result) {
        if (root == null) return;
        Deque<Node> stack = new ArrayDeque<>();
        LinkedList<Integer> output = new LinkedList<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            Node node = stack.pop();
            output.addFirst(node.v);
            if (node.left != null) stack.push(node.left);
            if (node.right != null) stack.push(node.right);
        }
        result.addAll(output);
    }

    public int[][] solution(int[][] nodeinfo) {
        Node[] nodes = new Node[nodeinfo.length];
        for (int v = 0; v < nodeinfo.length; v++) {
            nodes[v] = new Node(nodeinfo[v][0], nodeinfo[v][1], v + 1);
        }

        Arrays.sort(nodes, (n1, n2) ->
                n1.y != n2.y ? n2.y - n1.y : n1.x - n2.x);

        Node root = nodes[0];
        for (int i = 1; i < nodes.length; i++) {
            insert(root, nodes[i]);
        }

        List<Integer> preResult = new ArrayList<>();
        List<Integer> postResult = new ArrayList<>();
        preOrder(root, preResult);
        postOrder(root, postResult);

        return new int[][] {
                preResult.stream().mapToInt(v -> v).toArray(),
                postResult.stream().mapToInt(v -> v).toArray()
        };
    }
}