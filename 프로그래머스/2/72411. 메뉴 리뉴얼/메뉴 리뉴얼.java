import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Course {
    
    private int maxValue;
    private final List<String> menus = new ArrayList<>();
    
    private Course() {
        maxValue = 0;
    }
    
    public static Course create() {
        return new Course();
    }
    
    public void update(Map.Entry<String, Integer> entry) {
        if (entry.getValue() < maxValue) {
            return;
        }
        if (entry.getValue() > maxValue) {
            maxValue = entry.getValue();
            menus.clear();
        }
        menus.add(entry.getKey());
    }
    
    public void addAll(List<String> result) {
        result.addAll(menus);
    }
}

class Solution {
    
    public String[] solution(String[] orders, int[] course) {
        Map<String, Integer> result = new HashMap<>();
        
        for (String order : orders) {
            String target = orderCourseName(order);
            List<String> combinations = createCombinations(target);
            count(combinations, result);
        }
        
        return select(check(result), course).stream()
                .sorted()
                .toArray(String[]::new);
    }
    
    private List<String> select(Course[] courses, int[] course) {
        List<String> result = new ArrayList<>();
        
        for (int n : course) {
            if (courses[n] != null) {
                courses[n].addAll(result);
            }
        }
        
        return result;
    }
    
    private Course[] check(Map<String, Integer> countCourses) {
        Course[] courses = new Course[11];
        
        for (Map.Entry<String, Integer> entry : countCourses.entrySet()) {
            int length = entry.getKey().length();
            
            if (entry.getValue().intValue() <= 1) {
                continue;
            }
            if (courses[length] == null) {
                courses[length] = Course.create();
            }
            
            courses[length].update(entry);
        }
        
        return courses;
    }
    
    private void count(List<String> combinations, Map<String, Integer> result) {
        for (String combination : combinations) {
            result.merge(combination, 1, (a, b) -> a + b);
        }
    }
    
    private List<String> createCombinations(String order) {
        List<String> result = new ArrayList<>();
        boolean[] visited = new boolean[order.length()];
        
        dfs("", 0, visited, order, result);
        
        return result;
    }
    
    private void dfs(String currentCombinations, int currentIndex, boolean[] visited, String order, List<String> result) {
        if (currentCombinations.length() >= 2) {
            result.add(currentCombinations);
        }
        
        for (int index = currentIndex; index < order.length(); index++) {
            if (visited[index]) {
                continue;
            }
            
            visited[index] = true;
            dfs(currentCombinations + order.charAt(index), index, visited, order, result);
            visited[index] = false;
        }
    }
    
    private String orderCourseName(String courseName) {
        return courseName.chars()
                    .sorted()
                    .collect(
                            StringBuilder::new,
                            StringBuilder::appendCodePoint,
                            StringBuilder::append)
                    .toString();
    }
}