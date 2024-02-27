public class MatrixMul {
    public static void main(String[] args) {
        int[][] a = { { 52, 73 }, { 53, 69 } };
        int[][] b = { { 02, 56 }, { 62, 66 } };
        int[][] c;

        System.out.println("Matrix A: ");
        display(a);

        System.out.println("Matrix B: ");
        display(b);

        c = MatrixMultiply(a, b);

        System.out.println("Resultant Matrix C: ");
        display(c);
    }

    static int[][] MatrixMultiply(int[][] a, int[][] b) {
        int n = a.length;
        int[][] c = new int[n][n];
        int i, j, k;

        for (i = 0; i < n; i++) {
            for (j = 0; j < n; j++) {
                for (k = 0; k < n; k++) {
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }

        return c;
    }

    static void display(int[][] a) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a[i].length; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println("");
        }
    }
}
