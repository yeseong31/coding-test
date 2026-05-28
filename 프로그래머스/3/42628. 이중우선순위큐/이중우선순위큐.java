import java.util.TreeMap;

class Solution {
    public int[] solution(String[] operations) {
        TreeMap<Integer, Integer> map = new TreeMap<>();
        
        for (String op : operations) {
            String[] tokens = op.split(" ");
            String cmd = tokens[0];
            int val = Integer.parseInt(tokens[1]);
            
            if (cmd.equals("I")) {
                map.put(val, map.getOrDefault(val, 0) + 1);
            } else if (!map.isEmpty()) {
                int key = (val == 1) ? map.lastKey() : map.firstKey();
                if (map.put(key, map.get(key) - 1) == 1) {
                    map.remove(key);
                }
            }
        }
        
        if (map.isEmpty()) {
            return new int[] {0, 0};
        }
        return new int[] {map.lastKey(), map.firstKey()};
    }
}