#include <stdio.h>
#include <complex.h>

int main() {
    int width = 80, height = 40;
    int max_iter = 100;

    // Interesting Julia constants to try:
    // c = -0.7 + 0.27015i (Classic "swirls")
    // c = 0.35 + 0.35i    (Disconnected "dust")
    // c = -0.8 + 0.156i   (Symmetric "clouds")
    double complex c = -0.7 + 0.27015 * I; 

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            // z starts as the pixel coordinate
            double complex z = (x - width / 2.0) * 3.0 / width + 
                               (y - height / 2.0) * 2.0 / height * I;
            int iter = 0;

            while (cabs(z) <= 2.0 && iter < max_iter) {
                z = z * z + c;
                iter++;
            }

            // Simple ASCII shading
            if (iter == max_iter) printf("@"); 
            else if (iter > 20)   printf("#"); 
            else if (iter > 10)   printf("*");
            else if (iter > 5)    printf(".");
            else                  printf(" ");
        }
        printf("\n");
    }
    return 0;
}
