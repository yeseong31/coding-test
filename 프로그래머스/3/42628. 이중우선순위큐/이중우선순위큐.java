import java.util.Iterator;
import java.util.PriorityQueue;

class Solution {
    private final PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
    private final PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    
    public int[] solution(String[] operations) {
        for (String operation : operations) {
            String[] tokens = operation.split(" ");
            String op = tokens[0];
            String numStr = tokens[1];
            
            switch (op) {
                case "I" -> {
                    int number = Integer.parseInt(numStr);
                    maxHeap.add(number);
                    minHeap.add(number);
                }
                case "D" -> {
                    if (maxHeap.size() == 0) {
                        continue;
                    }
                    if (numStr.equals("-1")) {
                        minHeap.poll();
                        maxHeap.clear();
                        
                        Iterator<Integer> iter = minHeap.iterator();
                        while (iter.hasNext()) {
                            maxHeap.add(iter.next());
                        }
                    } else {
                        maxHeap.poll();
                        minHeap.clear();
                        
                        Iterator<Integer> iter = maxHeap.iterator();
                        while (iter.hasNext()) {
                            minHeap.add(iter.next());
                        }
                    }
                }
            }
        }
        
        if (maxHeap.size() == 0 || minHeap.size() == 0) {
            return new int[] {0, 0};
        }
        return new int[] {maxHeap.peek(), minHeap.peek()};
    }
}