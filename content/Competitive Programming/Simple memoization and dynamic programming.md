Title: Simple memoization and dynamic programming
Date: 2018-02-07 01:00
Category: Competitive Programming
Tags: Memoization, Dynamic Programming, Java
Slug: Simple memoization and dynamic programming

ABC040C is a nice example of the simplest form of memoization or dynamic programming.  
Using recursion without memoization cause TLE for this problem.

```java
	import java.util.Scanner;
	
	public class ABC040C {
	    static int n;
	    static int[] as;
	    static int[] costs;
	    public static void main(String args[]) {
	        Scanner sc = new Scanner(System.in);
	        n = sc.nextInt();
	        as = new int[n];
	        as[0] = sc.nextInt();
	        for (int i = 1; i < n; i++) {
	            as[i] = sc.nextInt() - as[0];
	        }
	        as[0] = 0;
	        costs = new int[n];
	        for (int i = 0; i < n; i++) costs[i] = Integer.MAX_VALUE;
	        //rec(n - 1);
	        dp();
	        System.out.println(costs[n - 1]);
	    }
	
	    // Memoization
	    static int rec(int i) {
	        if (i == 0) {
	            costs[0] = 0;
	            return costs[0];
	        }
	        if (i == 1) {
	            costs[1] = Math.abs(as[1] - as[0]);
	            return costs[1];
	        }
	        if (costs[i] < Integer.MAX_VALUE) return costs[i];
	        costs[i] = Math.min(Math.abs(as[i] - as[i - 1]) + rec(i - 1),
	                Math.abs(as[i] - as[i - 2]) + rec(i - 2));
	        return costs[i];
	    }
	
	    // Dynamic Programming
	    static void dp() {
	        costs[0] = 0;
	        costs[1] = Math.abs(as[1] - as[0]);
	        for (int i = 2; i < n; i++) {
	            costs[i] = Math.min(Math.abs(as[i] - as[i - 1]) + costs[i - 1],
	                    Math.abs(as[i] - as[i - 2]) + costs[i - 2]);
	        }
	    }
	}

```