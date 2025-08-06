import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class Main {

    private static final List<List<Integer>> graph = new ArrayList<>();

    private static int dfs(int node, int[] subtreeSize) {
        int size = 1;
        for (int child : graph.get(node)) {
            size += dfs(child, subtreeSize);
        }
        return subtreeSize[node] = size;
    }

    private static void preOrderDfs(int node, List<Integer> preOrderList) {
        preOrderList.add(node);
        for (int child : graph.get(node)) {
            preOrderDfs(child, preOrderList);
        }
    }

    private static List<Integer> solution(int n, int[][] commands, int root) {
        List<Integer> answer = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        int[] subtreeSize = new int[n + 1];
        dfs(root, subtreeSize);

        boolean[] toggled = new boolean[n + 1];
        Arrays.fill(toggled, false);

        List<Integer> preOrderList = new ArrayList<>();
        preOrderDfs(root, preOrderList);

        // 스택 초기화
        int seqIndex = 1;
        stack.push(preOrderList.get(1));

        // 명령어 수행
        for (int[] command : commands) {
            // toggle
            if (command[0] == 0) {
                int currNode = preOrderList.get(seqIndex);
                toggled[currNode] = !toggled[currNode];
                continue;
            }

            // move
            int move = command[1];
            if (move > 0) {
                while (move-- > 0 && seqIndex < n - 1) {
                    int prevNode = preOrderList.get(seqIndex);
                    if (toggled[prevNode]) {
                        seqIndex++;
                    } else {
                        if (seqIndex + subtreeSize[prevNode] < n) {
                            seqIndex += subtreeSize[prevNode];
                        }
                    }
                    if (seqIndex >= n) {
                        seqIndex = n - 1;
                    }
                    int currNode = preOrderList.get(seqIndex);
                    if (prevNode != currNode) {
                        stack.push(currNode);
                    }
                }
                answer.add(stack.peek());
            } else {
                while (move++ < 0 && stack.size() > 1) {
                    stack.pop();
                }
                int top = stack.peek();
                answer.add(top);
                seqIndex = preOrderList.indexOf(top);
            }
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int childCount = Integer.parseInt(st.nextToken());

            for (int j = 0; j < childCount; j++) {
                int child = Integer.parseInt(st.nextToken());
                graph.get(i).add(child);
            }
        }

        boolean[] isChild = new boolean[n + 1];
        for (int i = 1; i <= n; i++) {
            for (int child : graph.get(i)) {
                isChild[child] = true;
            }
        }

        int root = -1;
        for (int i = 1; i <= n; i++) {
            if (!isChild[i]) {
                root = i;
                break;
            }
        }

        int[][] commands = new int[q][2];
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());

            if (st.nextToken().equals("toggle")) {
                commands[i][0] = 0;
                commands[i][1] = 0;
            } else {
                commands[i][0] = 1;
                commands[i][1] = Integer.parseInt(st.nextToken());
            }
        }

        List<Integer> answer = solution(n, commands, root);
        for (int num : answer) {
            bw.write(num + "\n");
        }

        bw.flush();
        bw.close();
    }
}