import java.util.HashMap;
import java.util.Map;

class Solution {
    
    private static long findEmptyRoom(Map<Long, Long> reserved, long current) {
        if (!reserved.containsKey(current)) {
            reserved.put(current, current + 1);
            return current;
        }
        
        long next = findEmptyRoom(reserved, reserved.get(current));
        reserved.put(current, next);
        return next;
    }
    
    public long[] solution(long k, long[] room_number) {
        long[] answer = new long[room_number.length];
        Map<Long, Long> reserved = new HashMap<>();
        
        for (int i = 0; i < room_number.length; i++) {
            answer[i] = findEmptyRoom(reserved, room_number[i]);
        }
        
        return answer;
    }
}