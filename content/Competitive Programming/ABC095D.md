Title: ABC095D
Date: 2018-01-30 19:00
Category: Competitive programming
Tags: Java
Slug: ABC095D

To solve this problem and get full score, O(N) algorithm is needed.
Naive solution takes O(N^3) time, however, by calculating information that is independent from the variable we loop through, we get O(N^2) and O(N) algorithms.

O(N^3)
```java

	public class ABC095D {
	    int n;
	    long c;
	    long[] xs, vs;
	
	    public static void main(String args[]) {
	        new ABC095D().run();
	    }
	
	    void run() {
	        Scanner sc = new FastReader();
	        n = sc.nextInt();
	        c = sc.nextLong();
	        xs = new long[n + 2];
	        vs = new long[n + 2];
	        for (int i = 1; i <= n; i++) {
	            xs[i] = sc.nextLong();
	            vs[i] = sc.nextLong();
	        }
	        xs[n + 1] = c;
	        solve();
	    }
	
	    void solve() {
	        long maxCal = 0;
	        for (int i = 0; i <= n; i++) {
	            for (int j = i + 1; j <= n + 1; j++) {
	                long tempMaxCal = 0;
	                for (int k = 1; k <= i; k++) {
	                    tempMaxCal += vs[k];
	                }
	                for (int k = n; k >= j; k--) {
	                    tempMaxCal += vs[k];
	                }
	                if (xs[i] > c - xs[j]) {
	                    tempMaxCal -= xs[i] + 2 * (c - xs[j]);
	                } else {
	                    tempMaxCal -= 2 * xs[i] + c - xs[j];
	                }
	                maxCal = Math.max(maxCal, tempMaxCal);
	            }
	        }
	        System.out.println(maxCal);
	    }
	}
```

O(N^2)
```java

    void solve() {
        long[] vSumToI = new long[n + 1];
        long[] vSumToJ = new long[n + 2];
        for (int i = 1; i <= n; i++) {
            vSumToI[i] = vSumToI[i - 1] + vs[i];
        }
        for (int i = n; i >= 1; i--) {
            vSumToJ[i] = vSumToJ[i + 1] + vs[i];
        }
        long maxCal = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = i + 1; j <= n + 1; j++) {
                long tempMaxCal = 0;
                tempMaxCal += vSumToI[i];
                tempMaxCal += vSumToJ[j];
                if (xs[i] > c - xs[j]) {
                    tempMaxCal -= xs[i] + 2 * (c - xs[j]);
                } else {
                    tempMaxCal -= 2 * xs[i] + c - xs[j];
                }
                maxCal = Math.max(maxCal, tempMaxCal);
            }
        }
        System.out.println(maxCal);
    }
```

O(N)
```java

    void solve() {
        long[] vSumToI = new long[n + 1];
        long[] vSumToI2 = new long[n + 1];
        long[] vSumToJ = new long[n + 2];
        long[] maxVSumForJ = new long[n + 1];
        long[] maxVSumForJ2 = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            vSumToI[i] = vSumToI[i - 1] + vs[i];
            vSumToI2[i] = vSumToI2[i - 1]+ vs[i];
        }
        for (int i = n; i >= 1; i--) {
            vSumToJ[i] = vSumToJ[i + 1] + vs[i];
        }
        for (int i = 1; i <= n; i++) {
            maxVSumForJ[i] = Math.max(maxVSumForJ[i - 1],
                    vSumToI[i] - xs[i]);
            maxVSumForJ2[i] = Math.max(maxVSumForJ2[i - 1],
                    vSumToI[i] - 2 * xs[i]);
        }
        long maxCal = 0;
        for (int i = 1; i <= n + 1; i++) {
            long tempMaxCal = maxVSumForJ[i - 1] +
                    vSumToJ[i] - 2 * (c - xs[i]);
            maxCal = Math.max(maxCal, tempMaxCal);
            long tempMaxCal2 = maxVSumForJ2[i - 1] + vSumToJ[i] - c + xs[i];
            maxCal = Math.max(maxCal, tempMaxCal2);
        }
        System.out.println(maxCal);
    }
```