import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long n = Long.parseLong(br.readLine());
        Map<Long, Long> map = new HashMap<>((int) n);

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());

            long g = gcd(a, b);
            a /= g;
            b /= g;

            if (b < 0) {
                a = -a;
                b = -b;
            }

            long key = (a << 32) ^ (b & 0xffffffffL);
            map.put(key, map.getOrDefault(key, 0L) + 1);
        }

        long sumSq = 0;
        for (long v : map.values()) {
            sumSq += v * v;
        }
        System.out.println((n * n - sumSq) / 2);
    }

    private static long gcd(long a, long b) {
        a = Math.abs(a);
        b = Math.abs(b);

        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }

        return a;
    }
}