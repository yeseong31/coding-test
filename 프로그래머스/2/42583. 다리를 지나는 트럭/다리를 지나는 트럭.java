import java.util.ArrayDeque;
import java.util.Deque;

class Truck {
    public int seq;
    public int outTime;
    
    public Truck(int seq, int outTime) {
        this.seq = seq;
        this.outTime = outTime;
    }
}

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Truck> q = new ArrayDeque<>();
        
        int time = 0;
        int seq = 0;
        int currentWeight = 0;
        
        while (seq != truck_weights.length) {
            time++;
            
            if (!q.isEmpty() && q.peekFirst().outTime == time) {
                Truck truck = q.pollFirst();
                currentWeight -= truck_weights[truck.seq];
            }
            
            if (currentWeight + truck_weights[seq] <= weight) {
                q.offerLast(new Truck(seq, time + bridge_length));
                currentWeight += truck_weights[seq++];
            }
        }
        
        while (!q.isEmpty()) {
            if (q.peekFirst().outTime == ++time) {
                q.pollFirst();
            }
        }
        
        return time;
    }
}