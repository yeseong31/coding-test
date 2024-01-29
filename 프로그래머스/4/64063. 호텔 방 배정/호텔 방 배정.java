import java.util.HashMap;
import java.util.Map;

class Solution {
    public long[] solution(long k, long[] room_number) {
        long[] answer = new long[room_number.length];
        
        Map<Long, Long> rooms = new HashMap<>();
        
        for (int index = 0; index < room_number.length; index++) {
            answer[index] = findRoomNumber(room_number[index], rooms);
        }
        
        return answer;
    }
    
    private long findRoomNumber(long number, Map<Long, Long> rooms) {
        if (!rooms.containsKey(number)) {
            rooms.put(number, number + 1);
            return number;
        }
        
        long emptyRoom = findRoomNumber(rooms.get(number), rooms);
        rooms.put(rooms.get(number), emptyRoom + 1);
        return emptyRoom;
    }
}