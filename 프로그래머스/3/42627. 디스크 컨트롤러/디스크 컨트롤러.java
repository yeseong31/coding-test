import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    private class Process {
        private final int start;
        private final int duration;
        
        public Process(int start, int duration) {
            this.start = start;
            this.duration = duration;
        }
        
        public int getStart() {
            return start;
        }
        
        public int getDuration() {
            return duration;
        }
    }
    
    public int solution(int[][] jobs) {
        Process[] processes = new Process[jobs.length];
        
        for (int i = 0; i < jobs.length; i++) {
            processes[i] = new Process(jobs[i][0], jobs[i][1]);
        }
        
        Arrays.sort(processes, Comparator.comparingInt(process -> process.getStart()));
        
        Queue<Process> q = new LinkedList<>(Arrays.asList(processes));
        PriorityQueue<Process> pq = new PriorityQueue<>(Comparator.comparingInt(process -> process.getDuration()));
        
        int exec = 0;
        int time = 0;
        
        while (!q.isEmpty() || !pq.isEmpty()) {
            while (!q.isEmpty() && q.peek().getStart() <= time) {
                pq.add(q.poll());
            }
            
            if (pq.isEmpty()) {
                time = q.peek().getStart();
                continue;
            }
            
            Process process = pq.poll();
            time += process.getDuration();
            exec += time - process.getStart();
        }
        
        return exec / jobs.length;
    }
}