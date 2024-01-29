import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

class Disk {

    private int requestTime;
    private int executionTime;

    private Disk(int requestTime, int executionTime) {
        this.requestTime = requestTime;
        this.executionTime = executionTime;
    }

    public static Disk of(int[] job) {
        return new Disk(job[0], job[1]);
    }

    public int getRequestTime() {
        return requestTime;
    }

    public int getExecutionTime() {
        return executionTime;
    }
}

class Solution {

    public static int solution(int[][] jobs) {
        int answer = 0;
        int currentTime = 0;
        int completionTime = 0;
        int index = 0;

        Arrays.sort(jobs, Comparator.comparingInt(job -> job[0]));
        
        PriorityQueue<Disk> waitingQueue = new PriorityQueue<>(
                Comparator.comparingInt(job -> job.getExecutionTime()));

        while (index < jobs.length || !waitingQueue.isEmpty()) {
            while (index < jobs.length && currentTime >= jobs[index][0]) {
                waitingQueue.add(Disk.of(jobs[index++]));
            }
            
            if (waitingQueue.isEmpty() || currentTime < waitingQueue.peek().getRequestTime()) {
                currentTime++;
                continue;
            }

            Disk target = waitingQueue.poll();
            completionTime = currentTime + target.getExecutionTime();
            answer += completionTime - target.getRequestTime();
            currentTime = completionTime;
        }

        return answer / jobs.length;
    }
}