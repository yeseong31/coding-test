import java.util.*;

class Solution {
    
    public static List<Integer> getScores(List<int[]> diceGroup) {
        List<Integer> scores = new ArrayList<>();
        generateScores(diceGroup, 0, 0, scores);
        return scores;
    }

    private static void generateScores(List<int[]> diceGroup, int depth, int sum, List<Integer> scores) {
        if (depth == diceGroup.size()) {
            scores.add(sum);
            return;
        }

        for (int face : diceGroup.get(depth)) {
            generateScores(diceGroup, depth + 1, sum + face, scores);
        }
    }

    public static void combine(int n, int r, int start, List<Integer> current, List<List<Integer>> result) {
        if (current.size() == r) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i < n; i++) {
            current.add(i);
            combine(n, r, i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }
    
    public static int countLessThan(List<Integer> sortedList, int target) {
        int left = 0, right = sortedList.size();
        while (left < right) {
            int mid = (left + right) / 2;
            if (sortedList.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public static List<Integer> solution(int[][] dice) {
        int n = dice.length;
        int maxWin = 0;
        List<Integer> answer = new ArrayList<>();

        List<List<Integer>> combinations = new ArrayList<>();
        combine(n, n / 2, 0, new ArrayList<>(), combinations);

        for (List<Integer> aGroup : combinations) {
            Set<Integer> aSet = new HashSet<>(aGroup);
            List<Integer> bGroup = new ArrayList<>();
            
            for (int i = 0; i < n; i++) {
                if (!aSet.contains(i)) bGroup.add(i);
            }

            List<int[]> aDice = new ArrayList<>();
            for (int idx : aGroup) aDice.add(dice[idx]);

            List<int[]> bDice = new ArrayList<>();
            for (int idx : bGroup) bDice.add(dice[idx]);

            List<Integer> aScores = getScores(aDice);
            List<Integer> bScores = getScores(bDice);
            
            Collections.sort(bScores);

            int aWins = 0;
            for (int aScore : aScores) {
                aWins += countLessThan(bScores, aScore);
            }

            if (aWins > maxWin) {
                maxWin = aWins;
                answer = new ArrayList<>();
                
                for (int idx : aGroup) {
                    answer.add(idx + 1);
                }
            }
        }

        return answer;
    }
}