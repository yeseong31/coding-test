import java.util.Arrays;

public class Solution {

    public String solution(long n, String[] bans) {
        Arrays.sort(bans, (a, b) -> {
            if (a.length() == b.length()) return a.compareTo(b);
            return Integer.compare(a.length(), b.length());
        });

        for (String ban : bans) {
            if (n < toNum(ban)) break;
            n++;
        }

        return toAlpha(n);
    }

    private static String toAlpha(long num) {
        StringBuilder sb = new StringBuilder();
        
        while (num > 0) {
            long mod = (num - 1) % 26;
            sb.append((char) (mod + 'a'));
            num = (num - 1) / 26;
        }

        return sb.reverse().toString();
    }

    private static long toNum(String s) {
        long num = 0;
        
        for (int i = 0; i < s.length(); i++) {
            num = num * 26 + (s.charAt(i) - 'a' + 1);
        }
        
        return num;
    }
}