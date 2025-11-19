import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());  // 동시에 정차 가능한 버스 수
        int m = Integer.parseInt(st.nextToken());  // 영우가 타려는 버스까지의 버스 수

        int[][] times = new int[m][2];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            times[i][0] = Integer.parseInt(st.nextToken());  // 버스가 정류장에 도착하는 시간
            times[i][1] = Integer.parseInt(st.nextToken());  // 버스가 정류장에 정차하는 시간
        }

        int answer = solution(n, m, times);
        System.out.println(answer);
    }

    private static int solution(int n, int m, int[][] times) {
        int[] position = new int[m];

        int currTime = 0;    // 현재 시간
        int currCnt = 0;     // 현재 정류장에 정차 중인 버스 수
        int frontIdx = 0;    // 정류장에 가장 먼저 도착한 버스 인덱스
        int nextBusIdx = 0;  // 다음에 정차할 버스 인덱스

        // 시뮬레이션 수행
        while (nextBusIdx < m) {
            currTime++;

            // 정차 시간이 끝난 버스는 내보내기
            for (int i = frontIdx; i < frontIdx + currCnt; i++) {
                times[i][1]--;
                if (times[frontIdx][1] <= 0 && times[i][1] <= 0) {
                    frontIdx++;
                    currCnt--;
                }
            }

            // 새로운 버스 정차시키기
            while (currCnt < n && nextBusIdx < m && currTime >= times[nextBusIdx][0]) {
                // 마지막 버스가 n번 위치에 있으면 더 이상 들어올 수 없음
                int lastPos = (currCnt == 0) ? 0 : position[frontIdx + currCnt - 1];
                if (lastPos == n) {
                    break;
                }

                // 새로운 버스의 정차 위치 확인
                position[nextBusIdx++] = (currCnt++ == 0) ? 1 : lastPos + 1;
            }
        }

        return position[m - 1];
    }
}