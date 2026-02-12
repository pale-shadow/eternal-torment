#include <stdio.h>
#include <complex.h>

int main() {
    int width = 80, height = 40;
    int max_iter = 100;

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            // Map pixel coordinates to the complex plane (-2 to 1 for real, -1 to 1 for imaginary)
            double complex c = (x - width / 1.5) * 3.5 / width + 
                               (y - height / 2.0) * 2.0 / height * I;
            double complex z = 0;
            int iter = 0;

            // Mandelbrot iteration: z = z^2 + c
            while (cabs(z) <= 2.0 && iter < max_iter) {
                z = z * z + c;
                iter++;
            }

            // Print character based on how long it took to "escape"
            if (iter == max_iter) printf("#"); // Point is inside the set
            else if (iter > 10)   printf("*"); 
            else if (iter > 5)    printf(".");
            else                  printf(" ");
        }
        printf("\n");
    }
    return 0;
}

