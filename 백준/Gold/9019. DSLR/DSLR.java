import java.io.*;
import java.util.*;

public class Main {

    static boolean[] visited = new boolean[10000];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());
        
        while (t-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            Arrays.fill(visited, false);
            bw.write(bfs(a, b) + "\n");
        }

        bw.flush();
        bw.close();
    }

    private static String bfs(int start, int target) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(start, ""));
        visited[start] = true;

        while (!queue.isEmpty()) {
            Node current = queue.poll();

            if (current.value == target) {
                return current.commands;
            }

            // D
            int d = D(current.value);
            if (!visited[d]) {
                visited[d] = true;
                queue.add(new Node(d, current.commands + "D"));
            }

            // S
            int s = S(current.value);
            if (!visited[s]) {
                visited[s] = true;
                queue.add(new Node(s, current.commands + "S"));
            }

            // L
            int l = L(current.value);
            if (!visited[l]) {
                visited[l] = true;
                queue.add(new Node(l, current.commands + "L"));
            }

            // R
            int r = R(current.value);
            if (!visited[r]) {
                visited[r] = true;
                queue.add(new Node(r, current.commands + "R"));
            }
        }

        return "";
    }

    private static int D(int n) {
        return (2 * n) % 10000;
    }

    private static int S(int n) {
        return (n == 0) ? 9999 : n - 1;
    }

    private static int L(int n) {
        return (n % 1000) * 10 + n / 1000;
    }

    private static int R(int n) {
        return (n % 10) * 1000 + n / 10;
    }

    static class Node {
        int value;
        String commands;

        Node(int value, String commands) {
            this.value = value;
            this.commands = commands;
        }
    }
}