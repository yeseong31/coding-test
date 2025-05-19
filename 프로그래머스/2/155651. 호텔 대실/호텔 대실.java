import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
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
        List<Time> times = new ArrayList<>();
        
        for (String[] time : book_time) {
            int start = convertTime(time[0]);
            int end = convertTime(time[1]);
            times.add(new Time(start, end));
        }
        
        Collections.sort(times);
        
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