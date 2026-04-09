import java.util.*;

class Solution {
    
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> ranks = new HashMap<>();
        
        for (int i = 0; i < players.length; i++) {
            ranks.put(players[i], i);
        }
        
        for (String call : callings) {
            int i = ranks.get(call);
            
            ranks.put(call, i - 1);
            ranks.put(players[i - 1], i);
            
            String temp = players[i - 1];
            players[i - 1] = players[i];
            players[i] = temp;
        }
        
        return players;
    }
}