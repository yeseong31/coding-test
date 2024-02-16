import java.util.stream.Collectors;
import java.util.HashMap;
import java.util.Map;

class Solution {
    
    public int[] solution(int[] fees, String[] records) {
        Map<String, Integer> accumulateTimes = calculateAccumulateTimes(records);
        Map<String, Integer> totalFees = calculateTotalFees(accumulateTimes, fees);
        
        return totalFees.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByKey())
                .mapToInt(Map.Entry::getValue)
                .toArray();
    }
    
    private Map<String, Integer> calculateTotalFees(Map<String, Integer> accumulateTimes, int[] fees) {
        Map<String, Integer> totalFees = new HashMap<>();
        
        for (String carNumber : accumulateTimes.keySet()) {
            totalFees.put(
                    carNumber,
                    calculateFee(accumulateTimes.getOrDefault(carNumber, 0), fees));
        }
            
        return totalFees;
    }
    
    private int calculateFee(int duration, int[] fees) {
        if (duration <= fees[0]) {
            return fees[1];
        }
        
        return fees[1] + (int) Math.ceil((double) (duration - fees[0]) / fees[2]) * fees[3];
    }
    
    private Map<String, Integer> calculateAccumulateTimes(String[] records) {
        Map<String, Integer> history = new HashMap<>();
        Map<String, Integer> accumulateTimes = new HashMap<>();
        
        int closeTime = convertTime("23:59");
        
        for (String record : records) {
            String[] target = record.split(" ");
            
            int time = convertTime(target[0]);
            String carNumber = target[1];
            
            if (target[2].equals("IN")) {
                history.put(carNumber, time);
                continue;
            }
            
            accumulateTimes.put(
                    target[1], 
                    accumulateTimes.getOrDefault(carNumber, 0) + time - history.get(carNumber));
            
            history.remove(carNumber);
        }
        
        for (String carNumber : history.keySet()) {
            accumulateTimes.put(
                    carNumber, 
                    accumulateTimes.getOrDefault(carNumber, 0) + closeTime - history.get(carNumber));
        }
        
        return accumulateTimes;
    }
    
    private int convertTime(String time) {
        String hour = time.substring(0, 2);
        String minute = time.substring(3, 5);
        
        return Integer.parseInt(hour) * 60 + Integer.parseInt(minute);
    }
}