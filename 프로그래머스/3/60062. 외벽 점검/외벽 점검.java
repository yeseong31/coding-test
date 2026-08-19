import java.util.*;

class Solution {
    int answer;
    List<int[]> permutations = new ArrayList<>();

    public int solution(int n, int[] weak, int[] dist) {
        answer = dist.length + 1;
        int length = weak.length;

        int[] extendedWeak = new int[length * 2];
        for (int i = 0; i < length; i++) {
            extendedWeak[i] = weak[i];
            extendedWeak[i + length] = weak[i] + n;
        }

        makePermutations(dist, new boolean[dist.length], new int[dist.length], 0);

        for (int start = 0; start < length; start++) {
            for (int[] friends : permutations) {
                int count = 1;
                int coveredUntil = extendedWeak[start] + friends[0];

                for (int j = start; j < start + length; j++) {
                    if (coveredUntil < extendedWeak[j]) {
                        count++;

                        if (count > dist.length) {
                            break;
                        }

                        coveredUntil = extendedWeak[j] + friends[count - 1];
                    }
                }

                answer = Math.min(answer, count);
            }
        }

        return answer <= dist.length ? answer : -1;
    }

    private void makePermutations(int[] dist, boolean[] used, int[] selected, int depth) {
        if (depth == dist.length) {
            permutations.add(selected.clone());
            return;
        }

        for (int i = 0; i < dist.length; i++) {
            if (!used[i]) {
                used[i] = true;
                selected[depth] = dist[i];
                makePermutations(dist, used, selected, depth + 1);
                used[i] = false;
            }
        }
    }
}