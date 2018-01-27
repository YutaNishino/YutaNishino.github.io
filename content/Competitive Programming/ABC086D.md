Title: ABC086D
Date: 2018-01-27 17:00
Category: Competitive programming
Tags: imos, Java
Slug: ABC086D

First, we can treat x and y as x modulo 2K and y modulo 2K.

I used imos method [https://imoz.jp/algorithms/imos_method.html](https://imoz.jp/algorithms/imos_method.html) to count up the number in the array.
After that, the array is folded back so that the cases where x >= 2*K and y >= 2*K hold are added up.

```java
    import java.util.Scanner;

	public class ABC086D {
	    public static void main(String args[]) {
	        Scanner sc = new Scanner(System.in);
	        int n = sc.nextInt();
	        int k = sc.nextInt();
	        int[][] count = new int[4 * k + 1][4 * k + 1];
	
	        for (int i = 0; i < n; i++) {
	            int x = sc.nextInt();
	            int y = sc.nextInt();
	            char c = sc.next().charAt(0);
	            // convert white into black to regard every wish to be black
	            if (c == 'W') y += k;
	
	            // want (x, y) to be black
	            x %= 2 * k;
	            y %= 2 * k;
	
	            count[x][y]++;
	            count[x][y + k]--;
	            count[x + k][y]--;
	            count[x + k][y + k] += 2;
	            count[x + 2 * k][y + k]--;
	            count[x + k][y + 2 * k]--;
	            count[x + 2 * k][y + 2 * k]++;
	        }
	
	        for (int row = 0; row < count.length; row++) {
	            for (int col = 1; col < count[0].length; col++) {
	                count[col][row] += count[col - 1][row];
	            }
	        }
	        for (int col = 0; col < count[0].length; col++) {
	            for(int row = 1; row < count.length; row++) {
	                count[col][row] += count[col][row - 1];
	            }
	        }
	
	        for (int i = 0; i < count.length; i++) {
	            for (int j = 0; j < count[0].length; j++) {
	                if ( j < 2 * k && i < 2 * k) continue;
	                count[i % (2 * k)][j % (2 * k)] += count[i][j];
	            }
	        }
	
	        int ans = 0;
	        for (int row = 0; row < count.length; row++) {
	            for (int col = 0; col < count[0].length; col++) {
	                //System.out.printf("%d ", count[col][row]);
	                ans = Math.max(ans, count[col][row]);
	            }
	            //System.out.println();
	        }
	        System.out.println(ans);
	    }
	}
```
