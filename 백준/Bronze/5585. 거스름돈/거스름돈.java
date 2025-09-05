import java.io.*;

public class Main {

    private static final int[] changes = {500, 100, 50, 10, 5, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int amount = 1000 - Integer.parseInt(br.readLine());
        int answer = 0;

        for (int change : changes) {
            answer += amount / change;
            amount %= change;
        }

        sb.append(answer);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}