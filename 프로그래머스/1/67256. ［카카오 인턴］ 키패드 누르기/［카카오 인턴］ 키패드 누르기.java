class Point {
    public int x;
    public int y;
    public char hand;
    
    public Point(int number, char hand) {
        this.x = (number + 2) / 3;
        this.y = (number + 2) % 3;
        this.hand = hand;
    }
    
    public char moveTo(int number) {
        x = (number + 2) / 3;
        y = (number + 2) % 3;
        return hand;
    }
    
    public int getDistance(int number) {
        if (number == 0) {
            number = 11;
        }
        
        int x = (number + 2) / 3;
        int y = (number + 2) % 3;
        
        return Math.abs(this.x - x) + Math.abs(this.y - y);
    }
}

class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder sb = new StringBuilder();
        Point left = new Point(10, 'L');
        Point right = new Point(12, 'R');
        
        for (int n : numbers) {
            if (n == 0) {
                n = 11;
            }
            if ((n + 2) % 3 == 0) {
                sb.append(left.moveTo(n));
                continue;
            }
            if ((n + 2) % 3 == 2) {
                sb.append(right.moveTo(n));
                continue;
            }
            
            int leftDist = left.getDistance(n);
            int rightDist = right.getDistance(n);
            
            if (leftDist == rightDist) {
                if (hand.equals("left")) {
                    sb.append(left.moveTo(n));
                } else {
                    sb.append(right.moveTo(n));
                }
            } else if (leftDist < rightDist) {
                sb.append(left.moveTo(n));
            } else {
                sb.append(right.moveTo(n));
            }
        }
        
        return sb.toString();
    }
}