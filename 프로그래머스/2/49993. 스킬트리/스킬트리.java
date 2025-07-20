import java.util.Arrays;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        return (int) Arrays.stream(skill_trees)
                .map(v -> v.replaceAll("[^" + skill + "]", ""))
                .filter(v -> skill.startsWith(v))
                .count();
    }
}