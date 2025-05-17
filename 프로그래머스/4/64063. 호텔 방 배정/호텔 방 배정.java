import java.util.HashMap;
import java.util.Map;

class Solution {
    private long findEmptyRoom(Map<Long, Long> rooms, long room) {
        if (!rooms.containsKey(room)) {
            rooms.put(room, room + 1);
            return room;
        }

        long next = findEmptyRoom(rooms, rooms.get(room));
        rooms.put(room, next);
        return next;
    }

    public long[] solution(long k, long[] room_number) {
        long[] answer = new long[room_number.length];
        Map<Long, Long> rooms = new HashMap<>();

        for (int i = 0; i < room_number.length; i++) {
            answer[i] = findEmptyRoom(rooms, room_number[i]);
        }

        return answer;
    }
}