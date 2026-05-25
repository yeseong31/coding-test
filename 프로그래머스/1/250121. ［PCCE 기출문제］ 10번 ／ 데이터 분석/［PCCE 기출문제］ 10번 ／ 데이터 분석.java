import java.util.*;

class Solution {
    
    private static final Map<String, Integer> COLUMN_MAP = Map.of(
        "code", 0,
        "date", 1,
        "maximum", 2,
        "remain", 3
    );

    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        int extIdx = COLUMN_MAP.get(ext);
        int sortIdx = COLUMN_MAP.get(sort_by);

        return Arrays.stream(data)
            .filter(d -> d[extIdx] < val_ext)
            .sorted(Comparator.comparingInt(d -> d[sortIdx]))
            .toArray(int[][]::new);
    }
}