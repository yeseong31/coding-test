class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        
        for (String skillTree : skill_trees) {
            String prefix = skillTree.replaceAll("[^" + skill + "]", "");
            if (skill.startsWith(prefix)) {
                answer++;
            }
        }
        
        return answer;
    }
}