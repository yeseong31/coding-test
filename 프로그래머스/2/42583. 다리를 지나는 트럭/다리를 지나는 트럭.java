import java.util.LinkedList;
import java.util.Queue;

class Truck {
    
    private int load;
    private int enteringTime;
    
    public Truck(int load, int enteringTime) {
        this.load = load;
        this.enteringTime = enteringTime;
    }
    
    public int getLoad() {
        return load;
    }
    
    public int getEnteringTime() {
        return enteringTime;
    }
}

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int seconds = 0;
        int index = 0;
        int finished = 0;
        int load = 0;
        
        Queue<Truck> bridgeQueue = new LinkedList<>();
        
        while (finished != truck_weights.length) {
            Truck truck = bridgeQueue.peek();
            
            if (hasCrossedBridge(seconds, bridge_length, truck, bridgeQueue)) {
                bridgeQueue.poll();
                load -= truck.getLoad();
                finished++;
            }
            
            if (isSpaceAvailableOnBridge(bridge_length, bridgeQueue) && isWeightAllowedForTruck(index, weight, load, truck_weights)) {
                bridgeQueue.add(new Truck(truck_weights[index], seconds));
                load += truck_weights[index];
                index++;
            }
            
            seconds++;
        }
        
        return seconds;
    }
    
    private boolean isWeightAllowedForTruck(int index, int weight, int load, int[] truck_weights) {
        return index < truck_weights.length && load + truck_weights[index] <= weight;
    }
    
    private boolean isSpaceAvailableOnBridge(int bridge_length, Queue<Truck> bridgeQueue) {
        return bridgeQueue.size() < bridge_length;
    }
    
    private boolean hasCrossedBridge(int seconds, int bridge_length, Truck truck, Queue<Truck> bridgeQueue) {
        return truck != null && seconds - truck.getEnteringTime() == bridge_length;
    }
}
