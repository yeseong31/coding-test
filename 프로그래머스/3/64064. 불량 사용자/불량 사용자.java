import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;


class Solution {
    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;
        
        String[][] bans = Arrays.stream(banned_id)
                .map(bid -> bid.replace("*", "."))
                .map(bid -> Arrays.stream(user_id)
                        .filter(uid -> uid.matches(bid))
                        .toArray(String[]::new))
                .toArray(String[][]::new);
        
        Set<Set<String>> checkedBan = new HashSet<>();
        count(0, new HashSet<>(), bans, checkedBan);
        return checkedBan.size();
    }
    
    private void count(int index, Set<String> banned, String[][] bans, Set<Set<String>> checkedBan) {
        if (index == bans.length) {
            checkedBan.add(new HashSet<>(banned));
            return;
        }
        
        for (String id : bans[index]) {
            if (banned.contains(id)) {
                continue;
            }
            banned.add(id);
            count(index + 1, banned, bans, checkedBan);
            banned.remove(id);
        }
    }
}