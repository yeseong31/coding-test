class Solution {

    public int solution(int[] diffs, int[] times, long limit) {
        int minLevel = 1, maxLevel = 0;
        for (int d : diffs) maxLevel = Math.max(maxLevel, d);

        int answer = maxLevel;

        while (minLevel <= maxLevel) {
            int level = (minLevel + maxLevel) / 2;

            if (canSolve(diffs, times, limit, level)) {
                answer = level;
                maxLevel = level - 1;
            } else {
                minLevel = level + 1;
            }
        }

        return answer;
    }

    private boolean canSolve(int[] diffs, int[] times, long limit, int level) {
        long spendTime = 0;
        int timePrev = 0;

        for (int i = 0; i < diffs.length; i++) {
            spendTime += times[i];
            if (diffs[i] > level) {
                spendTime += (long)(timePrev + times[i]) * (diffs[i] - level);
            }
            timePrev = times[i];
            if (spendTime > limit) return false;
        }

        return true;
    }
}