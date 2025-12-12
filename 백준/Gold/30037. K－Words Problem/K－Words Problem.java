import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        while (n-- > 0) {
            System.out.println(convert(br.readLine()));
        }
    }

    private static String convert(String s) {
        StringTokenizer st = new StringTokenizer(s);
        Deque<String> dq = new ArrayDeque<>();

        while (st.hasMoreTokens()) {
            dq.addLast(st.nextToken());

            if (dq.size() < 3) {
                continue;
            }

            String last = dq.removeLast();
            String mid = dq.removeLast();
            String first = dq.removeLast();

            boolean canMerge = isKoreaSuffixToken(last)
                    && mid.equals("of")
                    && Character.isAlphabetic(first.charAt(first.length() - 1));

            if (!canMerge) {
                dq.addLast(first);
                dq.addLast(mid);
                dq.addLast(last);
                continue;
            }

            String merged = "K-" + toCapitalCase(first);
            if (!last.equals("Korea")) {
                merged += last.charAt(last.length() - 1);
            }
            dq.addLast(merged);
        }

        Deque<String> tmp = new ArrayDeque<>();
        while (!dq.isEmpty()) {
            String cur = dq.removeLast();
            
            if (cur.equals("Korea") && !tmp.isEmpty()) {
                String next = tmp.removeLast();
                tmp.addLast("K-" + toCapitalCase(next));
            } else {
                tmp.addLast(cur);
            }
        }
        while (!tmp.isEmpty()) {
            dq.addLast(tmp.removeLast());
        }
        
        StringBuilder result = new StringBuilder();
        while (!dq.isEmpty()) {
            result.append(dq.removeFirst());
            if (!dq.isEmpty()) {
                result.append(" ");
            }
        }

        return result.toString();
    }

    private static boolean isKoreaSuffixToken(String token) {
        if (token.equals("Korea")) {
            return true;
        }
        if (token.length() != 6) {
            return false;
        }
        char c = token.charAt(5);
        return c == '!' || c == '?' || c == ',' || c == '.';
    }

    private static String toCapitalCase(String word) {
        return word.substring(0, 1).toUpperCase() + word.substring(1);
    }
}