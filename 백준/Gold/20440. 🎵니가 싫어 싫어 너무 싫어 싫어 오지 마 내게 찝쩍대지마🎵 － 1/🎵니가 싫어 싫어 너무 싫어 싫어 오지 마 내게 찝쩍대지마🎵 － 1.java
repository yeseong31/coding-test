import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Map<Integer, Integer> timeline = new HashMap<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int te = Integer.parseInt(st.nextToken());
            int tx = Integer.parseInt(st.nextToken());
            timeline.put(te, timeline.getOrDefault(te, 0) + 1);
            timeline.put(tx, timeline.getOrDefault(tx, 0) - 1);
        }

        List<Integer> keys = new ArrayList<>(timeline.keySet());
        Collections.sort(keys);

        int currCount = 0;
        int maxCount = 0;
        int start = 0;
        int end = 0;
        boolean ongoing = false;

        for (int key : keys) {
            currCount += timeline.get(key);
            if (currCount > maxCount) {
                ongoing = true;
                maxCount = currCount;
                start = key;
            }
            if (currCount < maxCount && ongoing) {
                ongoing = false;
                end = key;
            }
        }

        System.out.println(maxCount);
        System.out.println(start + " " + end);
    }
}