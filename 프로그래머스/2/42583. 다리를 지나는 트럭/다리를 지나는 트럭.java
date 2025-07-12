import java.util.ArrayDeque;
import java.util.Deque;

class Truck {
    public final int seq;
    public final int weight;
    public final int exit_time;
    
    public Truck(int seq, int weight, int exit_time) {
        this.seq = seq;
        this.weight = weight;
        this.exit_time = exit_time;
    }
}

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<Truck> deque = new ArrayDeque<>();
        
        int n = truck_weights.length;
        int current_weight = 0;
        int seq = 0;
        int t = 0;
        
        while (seq < n) {
            if (!deque.isEmpty() && deque.peekFirst().exit_time == ++t) {
                Truck truck = deque.removeFirst();
                current_weight -= truck.weight;
            }
            
            if (current_weight + truck_weights[seq] <= weight) {
                deque.offerLast(new Truck(seq, truck_weights[seq], t + bridge_length));
                current_weight += truck_weights[seq++];
            }
        }
        
        while (!deque.isEmpty()) {
            if (deque.peekFirst().exit_time == ++t) {
                deque.removeFirst();
            }
        }
        
        return t + 1;
    }
}