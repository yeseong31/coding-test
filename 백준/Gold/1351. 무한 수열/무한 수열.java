import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    private static final HashMap<Long, Long> memo = new HashMap<>();

    private static long n;
    private static long p;
    private static long q;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Long.parseLong(st.nextToken());
        p = Long.parseLong(st.nextToken());
        q = Long.parseLong(st.nextToken());

        memo.put(0L, 1L);
        
        System.out.println(dfs(n));
    }
    
    private static long dfs(long x) {
        if (memo.containsKey(x)) {
            return memo.get(x);
        }

        long value = dfs(x / p) + dfs(x / q);
        memo.put(x, value);
        return value;
    }
}