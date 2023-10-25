class Solution {
    
    private static final int WAITING_ROOM_SIZE = 5;
    private static final int NEIGHBOR_CELL_SIZE = 8;
    
    private static final int[] dx = {0, 1, 1, 1, 0, -1, -1, -1};
    private static final int[] dy = {1, 1, 0, -1, -1, -1, 0, 1};
    
    public int[] solution(String[][] places) {
        
        int[] answer = new int[places.length];
        
        for (int i = 0; i < WAITING_ROOM_SIZE; i++) {
            
            String[] place = places[i];
            char[][] room = new char[place.length][];
            
            for (int j = 0; j < WAITING_ROOM_SIZE; j++) {
                room[j] = place[j].toCharArray();
            }
            
            answer[i] = checkDistanceCompliant(room);
        }
        
        return answer;
    }
    
    private int checkDistanceCompliant(char[][] room) {
        
        for (int x = 0; x < WAITING_ROOM_SIZE; x++) {
            for (int y = 0; y < WAITING_ROOM_SIZE; y++) {
                if (room[x][y] != 'P') {
                    continue;
                }
                
                for (int k = 0; k < NEIGHBOR_CELL_SIZE; k++) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];
                    
                    if (nx < 0 || nx >= WAITING_ROOM_SIZE || ny < 0 || ny >= WAITING_ROOM_SIZE) {
                        continue;
                    }
                    
                    if (k % 2 == 1) {
                        if (room[nx][ny] == 'P' && (room[x][ny] == 'O' || room[nx][y] == 'O')) {
                            return 0;
                        }
                        continue;
                    }
                    
                    if (room[nx][ny] == 'P') {
                        return 0;
                    }
                    
                    if (room[nx][ny] == 'O') {
                        nx += dx[k];
                        ny += dy[k];
                        
                        if (nx < 0 || nx >= WAITING_ROOM_SIZE || ny < 0 || ny >= WAITING_ROOM_SIZE) {
                            continue;
                        }
                        if (room[nx][ny] == 'P') {
                            return 0;
                        }
                    }
                }
            }
        }
        
        return 1;
    }
}