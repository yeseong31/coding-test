class Solution {
    
    public int[] solution(String[] wallpaper) {
        int lux = 51;
        int luy = 51;
        int rdx = -1;
        int rdy = -1;

        int n = wallpaper.length;
        int m = wallpaper[0].length();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (wallpaper[i].charAt(j) == '.') {
                    continue;
                }

                lux = Math.min(lux, i);
                luy = Math.min(luy, j);
                rdx = i + 1;
                rdy = Math.max(rdy, j + 1);
            }
        }

        return new int[]{lux, luy, rdx, rdy};
    }
}