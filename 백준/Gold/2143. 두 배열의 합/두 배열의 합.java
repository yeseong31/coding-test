class Main {

    public static void main(String[] args) throws Exception {
        final int H_MAX = ~(-1 << 20);
        final int STEP = 31;

        int[] hash = new int[H_MAX + 1];
        int[] data = new int[H_MAX + 1];

        int T = read();
        int n = read();

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = read();
        }

        int m = read();

        int[] b = new int[m];
        for (int i = 0; i < m; i++) {
            b[i] = read();
        }

        for (int i = 0; i < n; i++) {
            int currentSum = 0;

            for (int j = i; j < n; j++) {
                currentSum += a[j];
                int hashKey = currentSum & H_MAX;

                while (hash[hashKey] > 0 && data[hashKey] != currentSum) {
                    hashKey = (hashKey + STEP) & H_MAX;
                }

                hash[hashKey]++;
                data[hashKey] = currentSum;
            }
        }

        long count = 0;

        for (int i = 0; i < m; i++) {
            int currentSum = 0;

            for (int j = i; j < m; j++) {
                currentSum += b[j];
                int required = T - currentSum;
                int hashKey = required & H_MAX;

                while (hash[hashKey] > 0 && data[hashKey] != required) {
                    hashKey = (hashKey + STEP) & H_MAX;
                }
                if (hash[hashKey] > 0 && data[hashKey] == required) {
                    count += hash[hashKey];
                }
            }
        }

        System.out.print(count);
    }

    private static int read() throws Exception {
        int c = System.in.read();
        int n = c & 15;
        boolean neg = n == 13;

        if (neg) {
            n = System.in.read() & 15;
        }
        while ((c = System.in.read()) > 32) {
            n = (n << 3) + (n << 1) + (c & 15);
        }
        
        return neg ? ~n + 1 : n;
    }
}