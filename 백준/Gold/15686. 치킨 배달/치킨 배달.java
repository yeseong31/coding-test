import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static List<int[]> houses = new ArrayList<>();
    static List<int[]> chickens = new ArrayList<>();
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int value = Integer.parseInt(st.nextToken());
                if (value == 1) {
                    houses.add(new int[]{i, j});
                } else if (value == 2) {
                    chickens.add(new int[]{i, j});
                }
            }
        }

        combination(0, 0, new ArrayList<>());
        System.out.println(answer);
    }

    static void combination(int start, int count, List<int[]> selected) {
        if (count == m) {
            int totalDistance = 0;

            for (int[] house : houses) {
                int minDistance = Integer.MAX_VALUE;
                for (int[] chicken : selected) {
                    int distance = Math.abs(house[0] - chicken[0]) + Math.abs(house[1] - chicken[1]);
                    minDistance = Math.min(minDistance, distance);
                }
                totalDistance += minDistance;
            }

            answer = Math.min(answer, totalDistance);
            return;
        }

        for (int i = start; i < chickens.size(); i++) {
            selected.add(chickens.get(i));
            combination(i + 1, count + 1, selected);
            selected.remove(selected.size() - 1);
        }
    }
}