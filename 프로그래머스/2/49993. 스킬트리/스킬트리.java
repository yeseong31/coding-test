import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.List;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        return (int) Arrays.stream(skill_trees)
                .filter(skill_tree -> {
                    String regex = "[^" + Pattern.quote(skill) + "]";
                    String target = skill_tree.replaceAll(regex, "");
                    return skill.startsWith(target);
                })
                .count();
    }
}