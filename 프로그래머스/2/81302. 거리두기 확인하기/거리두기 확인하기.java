class Solution {
    
    private static final int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    private static final int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
    private static final int PLACE_SIZE = 5;
    private static final int CHECK_AREA = 8;
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        
        for (int i = 0; i < places.length; i++) {
            if (check(places[i])) {
                answer[i] = 1;
            }
        }
        
        return answer;
    }
    
    private boolean check(final String[] place) {
        char[][] board = new char[PLACE_SIZE][];
        for (int i = 0; i < PLACE_SIZE; i++) {
            board[i] = place[i].toCharArray();
        }
        
        for (int i = 0; i < PLACE_SIZE; i++) {
            for (int j = 0; j < PLACE_SIZE; j++) {
                if (board[i][j] != 'P') {
                    continue;
                }
                if (!availableSeat(board, i, j)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean availableSeat(final char[][] board, final int x, final int y) {
        for (int i = 0; i < CHECK_AREA; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx < 0 || nx >= PLACE_SIZE || ny < 0 || ny >= PLACE_SIZE) {
                continue;
            }
            
            if (i % 2 == 0) {
                if (board[nx][ny] == 'P') {
                    return false;
                }
                continue;
            }
            
            if (board[nx][ny] != 'P') {
                continue;
            }
            
            int lnx = x + dx[(i - 1) % CHECK_AREA];
            int lny = y + dy[(i - 1) % CHECK_AREA];
            int rnx = x + dx[(i + 1) % CHECK_AREA];
            int rny = y + dy[(i + 1) % CHECK_AREA];
            
            if (board[lnx][lny] == 'O' || board[rnx][rny] == 'O') {
                return false;
            }
            if (board[lnx][lny] == 'P' || board[rnx][rny] == 'P') {
                return false;
            }
        }
        
        for (int i = 0; i < CHECK_AREA; i += 2) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            int dnx = x + dx[i] * 2;
            int dny = y + dy[i] * 2;
            
            if (dnx < 0 || dnx >= PLACE_SIZE || dny < 0 || dny >= PLACE_SIZE || board[dnx][dny] != 'P') {
                continue;
            }
            
            if (board[nx][ny] != 'X') {
                return false;
            }
        }
        
        return true;
    }
}