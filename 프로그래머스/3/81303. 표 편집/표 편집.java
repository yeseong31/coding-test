import java.util.*;

class Solution {

    private int[] left;
    private int[] right;
    private Deque<Integer> removed;
    private int k;
    private int n;

    public String solution(int n, int k, String[] cmd) {
        this.n = n;
        this.k = k;
        left = new int[n];
        right = new int[n];
        removed = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            left[i] = i - 1;
            right[i] = i + 1;
        }

        for (String target : cmd) {
            char c = target.charAt(0);
            if (c == 'C') {
                delete();
            } else if (c == 'Z') {
                restore();
            } else {
                int x = Integer.parseInt(target.substring(2));
                if (c == 'U') up(x);
                else down(x);
            }
        }

        return getResult();
    }

    private void up(int x) {
        for (int i = 0; i < x; i++) k = left[k];
    }

    private void down(int x) {
        for (int i = 0; i < x; i++) k = right[k];
    }

    private void delete() {
        removed.push(k);
        int l = left[k];
        int r = right[k];
        if (l >= 0) right[l] = r;
        if (r < n) left[r] = l;
        k = (r < n) ? r : l;
    }

    private void restore() {
        int node = removed.pop();
        int l = left[node];
        int r = right[node];
        if (l >= 0) right[l] = node;
        if (r < n) left[r] = node;
    }

    private String getResult() {
        boolean[] isRemoved = new boolean[n];
        for (int node : removed) isRemoved[node] = true;

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(isRemoved[i] ? 'X' : 'O');
        }
        return sb.toString();
    }
}