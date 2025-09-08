import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Jewel[] jewels = new Jewel[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            jewels[i] = new Jewel(m, v);
        }

        long[] knapsacks = new long[k];
        for (int i = 0; i < k; i++) {
            knapsacks[i] = Long.parseLong(br.readLine());
        }

        Arrays.sort(jewels, Comparator.comparingInt(j -> j.weight));
        Arrays.sort(knapsacks);

        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());

        long answer = 0;
        int index = 0;

        for (long knapsack : knapsacks) {
            while (index < n && jewels[index].weight <= knapsack) {
                pq.offer(jewels[index++].value);
            }

            if (!pq.isEmpty()) answer += pq.poll();
        }

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

    private static class Jewel {
        final int weight;
        final int value;

        Jewel(int weight, int value) {
            this.weight = weight;
            this.value = value;
        }
    }
}