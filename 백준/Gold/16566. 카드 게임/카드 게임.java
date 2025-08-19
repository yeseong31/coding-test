import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    private static int find(int[] parents, int x) {
        if (parents[x] != x) {
            parents[x] = find(parents, parents[x]);
        }
        return parents[x];
    }

    private static void union(int[] parents, int a, int b) {
        a = find(parents, a);
        b = find(parents, b);

        if (a > b) {
            parents[b] = a;
        } else {
            parents[a] = b;
        }
    }

    private static int binarySearch(int[] cards, int x) {
        int left = 0;
        int right = cards.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (cards[mid] <= x) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return left;
    }

    private static int[] solution(int n, int m, int k, int[] cards, int[] rivals) {
        int[] answer = new int[k];

        int[] parents = new int[m + 1];
        for (int i = 0; i <= m; i++) {
            parents[i] = i;
        }

        Arrays.sort(cards);

        for (int i = 0; i < k; i++) {
            int index = binarySearch(cards, rivals[i]);
            index = find(parents, index);
            answer[i] = cards[index];
            union(parents, index, index + 1);
        }

        return answer;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] cards = new int[m];
        int[] rivals = new int[k];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            rivals[i] = Integer.parseInt(st.nextToken());
        }

        int[] answer = solution(n, m, k, cards, rivals);
        for (int x : answer) {
            sb.append(x).append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}