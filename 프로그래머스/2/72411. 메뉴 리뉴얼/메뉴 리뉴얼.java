import java.lang.StringBuilder;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.TreeMap;


class Solution {

    static class Menu {

        private final List<String> menus;
        private int maxValue;

        public Menu() {
            menus = new ArrayList<>();
            maxValue = 0;
        }

        public void add(Entry<String, Integer> entry) {
            if (entry.getValue() < maxValue) {
                return;
            }
            if (entry.getValue() > maxValue) {
                maxValue = entry.getValue();
                menus.clear();
            }
            menus.add(entry.getKey());
        }

        public void receive(List<String> answer) {
            answer.addAll(menus);
        }
    }
    
    public static String[] solution(String[] orders, int[] course) {
        Map<String, Integer> counter = new TreeMap<>();

        for (String order : orders) {
            String newOrder = receiveSortedOrder(order);
            generateSubOrder(newOrder, counter);
        }

        List<Map.Entry<String, Integer>> entries = new ArrayList<>(counter.entrySet());
        entries.sort((entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue()));

        Menu[] target = new Menu[11];

        for (Entry<String, Integer> entry : entries) {
            int count = entry.getValue();
            int length = entry.getKey().length();

            if (count <= 1) {
                continue;
            }
            if (target[length] == null) {
                target[length] = new Menu();
            }
            target[length].add(entry);
        }

        List<String> answer = new ArrayList<>();
        for (int number : course) {
            if (target[number] != null) {
                target[number].receive(answer);
            }
        }

        Collections.sort(answer);
        return answer.toArray(String[]::new);
    }

    private static String receiveSortedOrder(String order) {
        char[] chars = order.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }

    private static void generateSubOrder(String order, Map<String, Integer> answer) {
        int n = order.length();

        for (int mask = 0; mask < (1 << n); mask++) {
            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) > 0) {
                    sb.append(order.charAt(i));
                }
            }

            String key = sb.toString();
            answer.put(
                    key,
                    answer.getOrDefault(key, 0) + 1);
        }
    }
}