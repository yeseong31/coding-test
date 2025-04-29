class Solution {
    public int[] solution(int brown, int yellow) {
        int area = brown + yellow;
        for (int height = 3; height < (int) Math.sqrt(area) + 1; height++) {
            if (area % height != 0) {
                continue;
            }
            int width = area / height;
            if (area - (width - 2) * (height - 2) == brown) {
                return new int[] {width, height};
            }
        }
        return null;
    }
}