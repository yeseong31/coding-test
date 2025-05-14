import java.util.Stack;


class Price {
    private int t;
    private int price;
    
    public Price(int t, int price) {
        this.t = t;
        this.price = price;
    }
    
    public int getT() {
        return t;
    }
    
    public int getPrice() {
        return price;
    }
}


class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<Price> stack = new Stack<>();
        
        for (int t = 0; t < prices.length; t++) {
            while (!stack.isEmpty() && stack.peek().getPrice() > prices[t]) {
                Price price = stack.pop();
                answer[price.getT()] = t - price.getT();
            }
            
            stack.add(new Price(t, prices[t]));
        }
        
        while (!stack.isEmpty()) {
            Price price = stack.pop();
            answer[price.getT()] = answer.length - 1 - price.getT();
        }
        
        return answer;
    }
}