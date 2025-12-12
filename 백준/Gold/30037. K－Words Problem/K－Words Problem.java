import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
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
        List<String> words = new ArrayList<>();

        // === "XXX of Korea" 처리 ===
        while (st.hasMoreTokens()) {
            String token = st.nextToken();
            words.add(token);

            if (words.size() < 3) {
                continue;
            }

            int size = words.size();
            String lastToken = words.get(size - 1);
            String midToken = words.get(size - 2);
            String firstToken = words.get(size - 3);

            if (!isKoreanSuffixToken(lastToken)) {
                continue;
            }
            if (!midToken.equals("of")) {
                continue;
            }
            if (!Character.isAlphabetic(firstToken.charAt(firstToken.length() - 1))) {
                continue;
            }

            words.remove(size - 1);
            words.remove(size - 2);
            words.remove(size - 3);

            StringBuilder sb = new StringBuilder();
            sb.append("K-").append(toCapitalCase(firstToken));
            if (!lastToken.equals("Korea")) {
                sb.append(lastToken.charAt(lastToken.length() - 1));
            }
            words.add(sb.toString());
        }

        // === Korea XXX 처리 ===
        for (int i = words.size() - 2; i >= 0; i--) {
            if (words.get(i).equals("Korea")) {
                words.set(i, "K-");
                words.set(i + 1, toCapitalCase(words.get(i + 1)));
            }
        }

        // === 결과 문자열 조합 ===
        StringBuilder sb = new StringBuilder();
        for (int i = words.size() - 1; i >= 0; i--) {
            String token = words.get(i);

            if (!token.endsWith("K-")) {
                sb.insert(0, token + " ");
                continue;
            }

            int spaceIdx = sb.indexOf(" ");
            String nextWord = sb.substring(0, spaceIdx);

            sb.delete(0, spaceIdx + 1);
            sb.insert(0, token + nextWord + " ");
        }

        return sb.toString();
    }

    private static boolean isKoreanSuffixToken(String token) {
        return token.equals("Korea") || (token.length() == 6 && "!?,.".indexOf(token.charAt(5)) >= 0);
    }

    private static String toCapitalCase(String word) {
        return word.substring(0, 1).toUpperCase() + word.substring(1);
    }
}