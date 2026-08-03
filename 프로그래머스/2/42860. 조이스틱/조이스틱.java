class Solution {

    public int solution(String name) {
        int upDownCost = calculateUpDownCost(name);
        int leftRightCost = calculateMinLeftRightCost(name);
        return upDownCost + leftRightCost;
    }

    private int calculateUpDownCost(String name) {
        int cost = 0;
        for (char ch : name.toCharArray()) {
            cost += Math.min(ch - 'A', 'Z' - ch + 1);
        }
        return cost;
    }

    private int calculateMinLeftRightCost(String name) {
        int n = name.length();
        int minStep = n - 1;

        for (int i = 0; i < n; i++) {
            int next = findNextNonA(name, i + 1);

            int goRightFirst = 2 * i + (n - next);
            int goLeftFirst = i + 2 * (n - next);

            minStep = Math.min(minStep, Math.min(goRightFirst, goLeftFirst));
        }
        return minStep;
    }

    private int findNextNonA(String name, int index) {
        int n = name.length();
        while (index < n && name.charAt(index) == 'A') {
            index++;
        }
        return index;
    }
}