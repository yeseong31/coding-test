import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    class Time implements Comparable<Time>{
        public int start;
        public int end;
        
        public Time(int start, int end) {
            this.start = start;
            this.end = end;
        }
        
        @Override
        public int compareTo(Time other) {
            return this.start != other.start 
                ? Integer.compare(this.start, other.start) 
                : Integer.compare(this.end, other.end);
        }
    }
    
    private int convertTime(String time) {
        int minute = Integer.parseInt(time.substring(0, 2));
        int second = Integer.parseInt(time.substring(3, time.length()));
        return minute * 60 + second;
    }
    
    public int solution(String[][] book_time) {
        int answer = 1;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        Time[] times = new Time[book_time.length];
        
        for (int i = 0; i < book_time.length; i++) {
            int start = convertTime(book_time[i][0]);
            int end = convertTime(book_time[i][1]);
            times[i] = new Time(start, end);
        }
        
        Arrays.sort(times);
        
        for (Time t : times) {
            if (pq.isEmpty()) {
                pq.offer(t.end);
                continue;
            }
            
            if (pq.peek() <= t.start) {
                pq.poll();
            } else {
                answer++;
            }
            
            pq.offer(t.end + 10);
        }
        
        return answer;
    }
}