import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static final Map<String, Node> nodeMap = new HashMap<>();

    private static class Node {
        public final String value;
        public Node left;
        public Node right;

        public Node(String value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }

    private static void preOrderTraversal(Node node, List<String> result) {
        if (node == null || node.value.equals(".")) return;

        result.add(node.value);
        preOrderTraversal(node.left, result);
        preOrderTraversal(node.right, result);
    }

    private static void inOrderTraversal(Node node, List<String> result) {
        if (node == null || node.value.equals(".")) return;

        inOrderTraversal(node.left, result);
        result.add(node.value);
        inOrderTraversal(node.right, result);
    }

    private static void postOrderTraversal(Node node, List<String> result) {
        if (node == null || node.value.equals(".")) return;

        postOrderTraversal(node.left, result);
        postOrderTraversal(node.right, result);
        result.add(node.value);
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            String parent = st.nextToken();
            String left = st.nextToken();
            String right = st.nextToken();

            nodeMap.putIfAbsent(parent, new Node(parent));
            nodeMap.putIfAbsent(left, new Node(left));
            nodeMap.putIfAbsent(right, new Node(right));

            nodeMap.get(parent).left = nodeMap.get(left);
            nodeMap.get(parent).right = nodeMap.get(right);
        }

        Node root = nodeMap.get("A");

        List<String> preOrderList = new ArrayList<>();
        preOrderTraversal(root, preOrderList);
        sb.append(String.join("", preOrderList)).append("\n");

        List<String> inOrderList = new ArrayList<>();
        inOrderTraversal(root, inOrderList);
        sb.append(String.join("", inOrderList)).append("\n");

        List<String> postOrderList = new ArrayList<>();
        postOrderTraversal(root, postOrderList);
        sb.append(String.join("", postOrderList)).append("\n");

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}