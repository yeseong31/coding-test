class Solution {
    class BoxInfo {
        public int left;
        public int right;
        
        public BoxInfo(int left, int right) {
            this.left = left;
            this.right = right;
        }
    }
    
    private BoxInfo getBoxInfo(int w, int box, int floor) {
        int left = box - (w * floor);
        int right = w * (floor + 1) - (box + 1);
        
        if (floor % 2 == 1) {
            int tmp = left;
            left = right;
            right = tmp;
        }
        
        return new BoxInfo(left, right);
    }
    
    private int getNextBox(int box, int left, int right, int floor) {
        if (floor % 2 == 0) {
            return box + (2 * right + 1);
        } else {
            return box + (2 * left + 1);
        }
    }
    
    public int solution(int n, int w, int num) {
        int answer = 1;
        int box = num - 1;
        n--;
        
        int floor = box / w;
        BoxInfo info = getBoxInfo(w, box, floor);
        
        int left = info.left;
        int right = info.right;
        
        while (true) {
            int nextBox = getNextBox(box, left, right, floor);
            if (nextBox > n) {
                break;
            }
            
            box = nextBox;
            answer += 1;
            floor += 1;
        }
        
        return answer;
    }
}