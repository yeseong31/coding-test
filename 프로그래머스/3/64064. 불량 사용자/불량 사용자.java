import java.util.*;

class Solution {
    
    private final Set<Integer> result = new HashSet<>();
    private final List<List<Integer>> candidates = new ArrayList<>();

    public int solution(String[] userId, String[] bannedId) {
        result.clear();
        candidates.clear();

        for (String banned : bannedId) {
            List<Integer> matchedUsers = new ArrayList<>();
            String regex = banned.replace('*', '.');

            for (int i = 0; i < userId.length; i++) {
                if (userId[i].matches(regex)) {
                    matchedUsers.add(i);
                }
            }

            candidates.add(matchedUsers);
        }

        dfs(0, 0);
        return result.size();
    }

    private void dfs(int depth, int usedMask) {
        if (depth == candidates.size()) {
            result.add(usedMask);
            return;
        }

        for (int userIndex : candidates.get(depth)) {
            int userBit = 1 << userIndex;

            if ((usedMask & userBit) != 0) {
                continue;
            }

            dfs(depth + 1, usedMask | userBit);
        }
    }
}