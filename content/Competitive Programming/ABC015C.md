Title: ABC015C
Date: 2018-01-30 19:00
Category: Competitive programming
Tags: DFS, recursion, pruning, Java
Slug: ABC015C

I solved the problem with DFS using recursion, stack and stack with pruning.

Main part
```java
	import java.util.Scanner;
	import java.util.Stack;
	
	public class ABC015C {
	    static int n, k;
	    static int[][] field;
	    static boolean[][] visited;
	    public static void main(String args[]) {
	        Scanner sc = new Scanner(System.in);
	        n = sc.nextInt();
	        k = sc.nextInt();
	        int max = 0;
	        field = new int[n][k];
	        for (int i = 0; i < n; i++) {
	            for (int j = 0; j < k; j++) {
	                field[i][j] = sc.nextInt();
	                if (field[i][j] > max) max = field[i][j];
	            }
	        }
	        visited = new boolean[n + 1][(max + 1) * 2];
	        if (dfs(0,0)) System.out.println("Found");
	        else System.out.println("Nothing");
	    }
	
	    static class Tuple {
	        final int x;
	        final int y;
	        Tuple(int x, int y) {
	            this.x = x;
	            this.y = y;
	        }
	    }
	}
```

DFS using recursion
```java
    static boolean dfs(int numQ, int value) {
        if (numQ == n) return (value == 0);
        for (int i = 0; i < k; i++) {
            if (dfs(numQ + 1, value^field[numQ][i])) return true;
        }
        return false;
    }
```

DFS using stack
```
    static boolean dfs(int numQ, int value) {
        Stack<Tuple> s = new Stack<>();
        s.push(new Tuple(numQ, value));
        while (!s.empty()) {
            Tuple t = s.pop();
            for (int i = 0; i < k; i++) {
                if (t.x == n) {
                    if (t.y == 0) return true;
                    else continue;
                }
                s.push(new Tuple(t.x + 1, t.y ^ field[t.x][i]));
            }
        }
        return false;
    }
```

DFS using stack with pruning
```java
	static boolean dfs(int startQuestion, int value) {
	    Stack<Tuple> s = new Stack<>();
	    s.push(new Tuple(startQuestion, value));
	    while (!s.empty()) {
	        Tuple t = s.pop();
	        for (int i = 0; i < k; i++) {
	            if (t.x == n) {
	                if (t.y == 0) return true;
	                else continue;
	            }
	            int nextX = t.x + 1;
	            int nextY = t.y ^ field[t.x][i];
	            if (!visited[nextX][nextY]) {
	                visited[nextX][nextY] = true;
	                s.push(new Tuple(nextX, nextY));
	            }
	        }
	    }
	    return false;
	}
```