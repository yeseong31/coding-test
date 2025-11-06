import java.util.*;

class Solution {
    
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        
        Map<String, Integer> names = new HashMap<>();
        names.put("code", 0);
        names.put("date", 1);
        names.put("maximum", 2);
        names.put("remain", 3);

        int extIdx = names.get(ext);
        int sortIdx = names.get(sort_by);

        List<int[]> filtered = new ArrayList<>();

        for (int[] d : data) {
            if (d[extIdx] < val_ext) {
                filtered.add(d);
            }
        }

        filtered.sort(Comparator.comparingInt(o -> o[sortIdx]));

        return filtered.toArray(new int[0][]);
    }
}