import java.util.PriorityQueue;

class DoublePriorityQueue {
    
    private final PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
    private final PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    private int size;
    
    public DoublePriorityQueue() {
    }
    
    public void add(int value) {
        maxHeap.add(value);
        minHeap.add(value);
        size++;
    }
    
    public void removeMaxValue() {
        if (size == 0) {
            return;
        }
        
        size--;
        maxHeap.poll();
        
        if (size == 0) {
            clearHeap();
        }
    }
    
    public void removeMinValue() {
        if (size == 0) {
            return;
        }
        
        size--;
        minHeap.poll();

        if (size == 0) {
            clearHeap();
        }
    }
    
    public int receiveMaxValue() {
        if (size == 0) {
            return 0;
        }
        return maxHeap.peek();
    }
    
    public int receiveMinValue() {
        if (size == 0) {
            return 0;
        }
        return minHeap.peek();
    }
    
    private void clearHeap() {
        maxHeap.clear();
        minHeap.clear();
    }
}

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {};
        DoublePriorityQueue doublePriorityQueue = new DoublePriorityQueue();
        
        for (String operation : operations) {
            String[] tokens = operation.split(" ");
            int value = Integer.parseInt(tokens[1]);
            
            if (tokens[0].equals("I")) {
                doublePriorityQueue.add(value);
                continue;
            }
            
            if (value < 0) {
                doublePriorityQueue.removeMinValue();
            } else {
                doublePriorityQueue.removeMaxValue();
            }
        }
        
        return new int[] {
            doublePriorityQueue.receiveMaxValue(),
            doublePriorityQueue.receiveMinValue()
        };
    }
}