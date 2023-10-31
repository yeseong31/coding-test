import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


class Solution {
    public int[] solution(int brown, int yellow) {
        int area = brown + yellow;
        
        List<Integer> dividors = getDividors(area);
        for (int height : dividors) {
            int width = area / height;
            if ((width - 2) * (height - 2) == yellow) {
                return new int[] {width, height};
            }
        }
        
        return null;
    }
    
    private List<Integer> getDividors(final int area) {
        List<Integer> result = new ArrayList<>();
        
        for (int i = 1; i <= Math.sqrt(area); i++) {
            if (area % i == 0) {
                result.add(i);
            }
        }
        
        return Collections.unmodifiableList(result);
    }
}