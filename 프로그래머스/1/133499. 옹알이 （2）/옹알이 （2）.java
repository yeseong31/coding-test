class Solution {
    
    public int solution(String[] babbling) {
        String[] check = {"aya", "ye", "woo", "ma"};
        int answer = 0;

        for (String v : babbling) {
            String temp = v;

            for (String c : check) {
                if (!temp.contains(c + c)) {
                    temp = temp.replace(c, " ");
                }
            }

            if (temp.trim().isEmpty()) {
                answer++;
            }
        }

        return answer;
    }
}