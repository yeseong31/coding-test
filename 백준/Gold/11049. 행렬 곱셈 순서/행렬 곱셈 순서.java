import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        int n = Integer.parseInt(br.readLine());
        Node[][] dp = new Node[n][n];
        
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long r = Long.parseLong(st.nextToken());
            long c = Long.parseLong(st.nextToken());
            dp[0][i] = new Node(r, c, 0);
        }

        long answer = solution(dp);
        System.out.println(answer);
    }
    
    private static long solution(Node[][] dp) {
        int n = dp.length;

        for (int len = 1; len < n; len++) {
            for (int start = 0; start + len < n; start++) {

                long minCost = Long.MAX_VALUE;
                Node best = null;

                for (int k = 0; k < len; k++) {
                    Node left = dp[k][start];
                    Node right = dp[len - k - 1][start + k + 1];

                    long cost = left.k + right.k + left.r * left.c * right.c;

                    if (cost < minCost) {
                        minCost = cost;
                        best = new Node(left.r, right.c, cost);
                    }
                }

                dp[len][start] = best;
            }
        }

        return dp[n - 1][0].k;
    }
    
    private static class Node {
        final long r;
        final long c;
        final long k;
        
        Node(long r, long c, long k) {
            this.r = r;
            this.c = c;
            this.k = k;
        }
    }
}