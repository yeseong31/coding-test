import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;
        
        String[][] bannedList = Arrays.stream(banned_id)
                .map(bid -> bid.replace("*", "."))
                .map(bid -> Arrays.stream(user_id)
                        .filter(uid -> uid.matches(bid))
                        .toArray(String[]::new))
                .toArray(String[][]::new);
        
        Set<Set<String>> result = new HashSet<>();
        
        dfs(0, new HashSet<>(), bannedList, result);
        
        return result.size();
    }
    
    private void dfs(int currentIndex, Set<String> currentBanned, String[][] bannedList, Set<Set<String>> result) {
        if (currentIndex == bannedList.length) {
            result.add(new HashSet<>(currentBanned));
            return;
        }
        
        for (String bid : bannedList[currentIndex]) {
            if (currentBanned.contains(bid)) {
                continue;
            }
            
            currentBanned.add(bid);
            dfs(currentIndex + 1, currentBanned, bannedList, result);
            currentBanned.remove(bid);
        }
    }
}
