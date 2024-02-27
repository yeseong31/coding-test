import java.util.Arrays;

class Solution {
    
    public int[] solution(int n, int[] info) {
        int[] answer = ryan(0, n, new int[11], info);
        
        if (answer == null) {
            return new int[] {-1};
        }
        
        return answer;
    }
    
    private int[] ryan(int index, int n, int[] hits, int[] apeach) {
        if (index == hits.length) {
            if (n > 0) {
                return null;
            }
            
            if (calculateScoreDiff(apeach, hits) <= 0) {
                return null;
            }
            
            return Arrays.copyOf(hits, hits.length);
        }
        
        int maxDiff = 0;
        int[] result = null;
        
        for (int hit = 0; hit <= n; hit++) {
            hits[index] = hit;
            int[] ryan = ryan(index + 1, n - hit, hits, apeach);
            
            if (ryan == null) {
                continue;
            }
            
            int diff = calculateScoreDiff(apeach, ryan);
            
            if (diff > maxDiff || (diff == maxDiff && isPriority(result, ryan))) {
                maxDiff = diff;
                result = ryan;
            } 
        }
        
        return result;
    }
    
    private boolean isPriority(int[] base, int[] comp) {
        for (int index = 10; index >= 0; index--) {
            if (comp[index] == base[index]) {
                continue;
            }
            
            return comp[index] > base[index];
        }
        return false;
    }
    
    private int calculateScoreDiff(int[] apeach, int[] ryan) {
        int result = 0;
        
        for (int index = 0; index < apeach.length; index++) {
            if (apeach[index] == 0 && ryan[index] == 0) {
                continue;
            }
            
            if (apeach[index] >= ryan[index]) {
                result -= 10 - index;
            } else {
                result += 10 - index;
            }
        }
        
        return result;
    }
}