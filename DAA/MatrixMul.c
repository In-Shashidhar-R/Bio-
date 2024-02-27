#include <stdio.h>

void display(int matrix[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

void matrixMultiply(int a[2][2], int b[2][2], int c[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            c[i][j] = 0;
            for (int k = 0; k < 2; k++) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}

int main() {
    int a[2][2] = {{52, 73}, {53, 69}};
    int b[2][2] = {{02, 56}, {62, 66}};
    int c[2][2];

    printf("Matrix A: \n");
    display(a);

    printf("Matrix B: \n");
    display(b);

    matrixMultiply(a, b, c);

    printf("Resultant Matrix C: \n");
    display(c);

    return 0;
}
