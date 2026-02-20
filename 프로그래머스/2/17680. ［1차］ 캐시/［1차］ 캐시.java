import java.util.*;

public class Solution {

    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        Deque<String> cache = new LinkedList<>();
        
        if (cacheSize == 0) {
            return cities.length * 5;
        }
        
        for (String city : cities) {
            city = city.toLowerCase();
            
            if (cache.contains(city)) {
                answer += 1;
                cache.remove(city);
                cache.addLast(city);
            } else {
                answer += 5;
                cache.addLast(city);
                
                if (cache.size() > cacheSize) {
                    cache.pollFirst();
                }
            }
        }
        
        return answer;
    }
}