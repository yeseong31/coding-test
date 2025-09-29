import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {

    private static final List<List<Integer>> COMBINATIONS = new ArrayList<>();

    private static int[][] DICE;
    private static int N;

    public static List<Integer> solution(int[][] dice) {
        DICE = dice;
        N = dice.length;

        int MAX_WIN = 0;
        List<Integer> BEST = new ArrayList<>();

        // n개 중 n/2개 조합 구하기
        combine(0, new ArrayList<>());

        for (List<Integer> aGroup : COMBINATIONS) {
            List<Integer> bGroup = new ArrayList<>();
            for (int i = 0; i < N; i++) if (!aGroup.contains(i)) bGroup.add(i);

            List<Integer> aScores = getScores(aGroup);
            List<Integer> bScores = getScores(bGroup);
            Collections.sort(bScores);

            int aWins = 0;
            for (int a : aScores) {
                aWins += binarySearch(bScores, a);
            }

            if (aWins > MAX_WIN) {
                MAX_WIN = aWins;
                BEST = new ArrayList<>();
                for (int idx : aGroup) BEST.add(idx + 1);
            }
        }

        return BEST;
    }

    private static List<Integer> getScores(List<Integer> group) {
        List<Integer> scores = new ArrayList<>();
        dfs(group, 0, 0, scores);
        return scores;
    }

    private static void dfs(List<Integer> group, int depth, int sum, List<Integer> scores) {
        if (depth == group.size()) {
            scores.add(sum);
            return;
        }

        for (int face : DICE[group.get(depth)]) {
            dfs(group, depth + 1, sum + face, scores);
        }
    }

    private static void combine(int start, List<Integer> curr) {
        if (curr.size() == N / 2) {
            COMBINATIONS.add(new ArrayList<>(curr));
            return;
        }

        for (int i = start; i < N; i++) {
            curr.add(i);
            combine(i + 1, curr);
            curr.remove(curr.size() - 1);
        }
    }

    private static int binarySearch(List<Integer> list, int target) {
        int l = 0, r = list.size();

        while (l < r) {
            int m = l + (r - l) / 2;
            if (list.get(m) < target) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        return l;
    }
}