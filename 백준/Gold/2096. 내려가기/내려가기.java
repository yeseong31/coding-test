import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int xMax = Integer.parseInt(st.nextToken());
        int yMax = Integer.parseInt(st.nextToken());
        int zMax = Integer.parseInt(st.nextToken());

        int xMin = xMax;
        int yMin = yMax;
        int zMin = zMax;

        for (int i = 1; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            int nextXMax = a + Math.max(xMax, yMax);
            int nextYMax = b + Math.max(Math.max(xMax, yMax), zMax);
            int nextZMax = c + Math.max(yMax, zMax);

            xMax = nextXMax;
            yMax = nextYMax;
            zMax = nextZMax;

            int nextXMin = a + Math.min(xMin, yMin);
            int nextYMin = b + Math.min(Math.min(xMin, yMin), zMin);
            int nextZMin = c + Math.min(yMin, zMin);

            xMin = nextXMin;
            yMin = nextYMin;
            zMin = nextZMin;
        }

        int maxResult = Math.max(xMax, Math.max(yMax, zMax));
        int minResult = Math.min(xMin, Math.min(yMin, zMin));

        sb.append(maxResult).append(" ").append(minResult);
        
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}