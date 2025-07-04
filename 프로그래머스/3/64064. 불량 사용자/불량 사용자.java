import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    private static final Map<String, Set<String>> bannedIdMap = new HashMap<>();
    
    private static void dfs(String[] banned_id, int seq, Set<String> current, Set<Set<String>> answer) {
        if (seq == banned_id.length) {
            if (current.size() == banned_id.length) {
                answer.add(new HashSet<>(current));
            }
            return;
        }
        
        for (String bid : bannedIdMap.get(banned_id[seq])) {
            if (current.contains(bid)) {
                continue;
            }

            current.add(bid);
            dfs(banned_id, seq + 1, current, answer);
            current.remove(bid);
        }
    }
    
    public int solution(String[] user_id, String[] banned_id) {
        for (String bid : banned_id) {
            String regex = bid.replace("*", ".");
            if (bannedIdMap.containsKey(regex)) {
                continue;
            }
            
            Set<String> matchedIds = new HashSet<>();
            for (String uid : user_id) {
                if (uid.matches(regex)) {
                    matchedIds.add(uid);
                }
            }
            
            bannedIdMap.put(bid, matchedIds);
        }
        
        Set<Set<String>> answer = new HashSet<>();
        dfs(banned_id, 0, new HashSet<>(), answer);
        
        return answer.size();
    }
}