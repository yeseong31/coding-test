import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    private static List<Node>[] graph;

    private static int root;
    private static int pillarLen;
    private static int branchLen;
    private static int gigaNode;
    private static int gigaParent;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        root = Integer.parseInt(st.nextToken());

        if (n == 1) {
            System.out.println("0 0");
            return;
        }

        graph = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            graph[a].add(new Node(b, d));
            graph[b].add(new Node(a, d));
        }

        findGigaNode();

        if (graph[gigaNode].size() == 1) {
            branchLen = 0;
        } else {
            bfs(gigaNode, gigaParent);
        }

        System.out.println(pillarLen + " " + branchLen);
    }

    private static void findGigaNode() {
        int cur = root;
        int parent = 0;
        int len = 0;

        while (true) {
            int deg = graph[cur].size();

            if (cur == root) {
                if (deg != 1) {
                    gigaNode = cur;
                    pillarLen = 0;
                    gigaParent = parent;
                    return;
                }
            } else {
                if (deg != 2) {
                    gigaNode = cur;
                    pillarLen = len;
                    gigaParent = parent;
                    return;
                }
            }

            int nextTo = 0;
            int nextCost = 0;

            for (Node e : graph[cur]) {
                if (e.to != parent) {
                    nextTo = e.to;
                    nextCost = e.cost;
                    break;
                }
            }

            len += nextCost;
            parent = cur;
            cur = nextTo;
        }
    }

    private static void bfs(int start, int parent) {
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{start, parent, 0});

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int node = cur[0];
            int par = cur[1];
            int dist = cur[2];

            boolean isLeaf = true;
            for (Node next : graph[node]) {
                if (next.to != par) {
                    isLeaf = false;
                    stack.push(new int[]{next.to, node, dist + next.cost});
                }
            }
            if (isLeaf && dist > branchLen) {
                branchLen = dist;
            }
        }
    }

    private static class Node {
        final int to;
        final int cost;

        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }
}