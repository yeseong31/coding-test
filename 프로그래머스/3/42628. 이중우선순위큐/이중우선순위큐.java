import java.util.TreeMap;

class Solution {
    
    public int[] solution(String[] operations) {
        TreeMap<Integer, Integer> map = new TreeMap<>();

        for (String operation : operations) {
            String[] tokens = operation.split(" ");
            String command = tokens[0];
            int value = Integer.parseInt(tokens[1]);

            if (command.equals("I")) {
                map.put(value, map.getOrDefault(value, 0) + 1);
                continue;
            }
            if (!map.isEmpty()) {
                int key = (value == 1)
                        ? map.lastKey()
                        : map.firstKey();

                int count = map.get(key);

                if (count == 1) {
                    map.remove(key);
                } else {
                    map.put(key, count - 1);
                }
            }
        }

        if (map.isEmpty()) {
            return new int[]{0, 0};
        }

        return new int[]{map.lastKey(), map.firstKey()};
    }
}