import java.lang.StringBuilder;
import java.util.ArrayList;
import java.util.List;

class Point {
    
    private final int x;
    private final int y;
    
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    public int getX() {
        return x;
    }
    
    public int getY() {
        return y;
    }
}

class Solution {
    
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        List<Point> keypads = generateKeypads();
        
        int lx = 3;
        int ly = 0;
        int rx = 3;
        int ry = 2;
        
        for (int number : numbers) {
            Point keypad = keypads.get(number);
            
            if ((number - 1) % 3 == 0) {
                answer.append("L");
                lx = keypad.getX();
                ly = keypad.getY();
                continue;
            }
            
            if ((number - 1) % 3 == 2) {
                answer.append("R");
                rx = keypad.getX();
                ry = keypad.getY();
                continue;
            }
            
            int distance = findDistance(keypad, lx, ly, rx, ry);
            
            if ((distance == 0 && hand.equals("left")) || distance < 0) {
                answer.append("L");
                lx = keypad.getX();
                ly = keypad.getY();
            } else {
                answer.append("R");
                rx = keypad.getX();
                ry = keypad.getY();
            }
        }
        
        return answer.toString();
    }
    
    private int findDistance(Point keypad, int lx, int ly, int rx, int ry) {
        int x = keypad.getX();
        int y = keypad.getY();
        
        int distanceFromLeft = Math.abs(x - lx) + Math.abs(y - ly);
        int distanceFromRight = Math.abs(x - rx) + Math.abs(y - ry);
        
        return distanceFromLeft - distanceFromRight;
    }
    
    private List<Point> generateKeypads() {
        List<Point> keypads = new ArrayList<>();
        
        keypads.add(new Point(3, 1));
        for (int number = 1; number <= 9; number++) {
            int x = (number - 1) / 3;
            int y = (number - 1) % 3;
            keypads.add(new Point(x, y));
        }
        
        return keypads;
    }
}