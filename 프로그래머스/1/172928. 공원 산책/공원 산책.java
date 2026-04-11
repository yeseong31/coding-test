import java.util.*;

class Solution {
    
    public int[] solution(String[] park, String[] routes) {
        Map<Character, int[]> direction = new HashMap<>();
        direction.put('E', new int[]{0, 1});
        direction.put('S', new int[]{1, 0});
        direction.put('W', new int[]{0, -1});
        direction.put('N', new int[]{-1, 0});
        
        int x = 0, y = 0;
        
        for (int i = 0; i < park.length; i++) {
            for (int j = 0; j < park[0].length(); j++) {
                if (park[i].charAt(j) == 'S') {
                    x = i;
                    y = j;
                    break;
                }
            }
        }
        
        for (String route : routes) {
            String[] parts = route.split(" ");
            char d = parts[0].charAt(0);
            int v = Integer.parseInt(parts[1]);
            
            int nx = x;
            int ny = y;
            boolean check = false;
            
            for (int i = 0; i < v; i++) {
                nx += direction.get(d)[0];
                ny += direction.get(d)[1];
                
                if (nx < 0 || nx >= park.length ||
                    ny < 0 || ny >= park[0].length() ||
                    park[nx].charAt(ny) == 'X') {
                    check = true;
                    break;
                }
            }
            
            if (!check) {
                x = nx;
                y = ny;
            }
        }
        
        return new int[]{x, y};
    }
}