import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine());

        long answer = 0;
        long base = 1;

        while (n > 0) {
            if ((n & 1) == 1) {
                answer += base;
            }
            base *= 3;
            n >>= 1;
        }

        System.out.println(answer);
    }
}