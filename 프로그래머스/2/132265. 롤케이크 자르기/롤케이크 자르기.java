class Solution {
    
    public int solution(int[] topping) {
        int answer = 0;

        int max = 10000;
        int[] count = new int[max + 1];

        int rightKinds = 0;
        for (int t : topping) {
            if (count[t]++ == 0) rightKinds++;
        }

        boolean[] leftVisited = new boolean[max + 1];
        int leftKinds = 0;

        for (int t : topping) {
            if (leftVisited[t] == false) {
                leftVisited[t] = true;
                leftKinds++;
            }

            if (--count[t] == 0) {
                rightKinds--;
            }

            if (leftKinds == rightKinds) {
                answer++;
            }
        }

        return answer;
    }
}