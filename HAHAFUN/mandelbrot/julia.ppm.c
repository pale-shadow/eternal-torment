#include <stdio.h>
#include <complex.h>

int main() {
    int width = 1920, height = 1080;
    int max_iter = 256;
    double complex c = -0.7 + 0.27015 * I; // The fractal constant

    FILE *fp = fopen("julia.ppm", "wb");
    // PPM Header: P6 (binary), dimensions, max color value (255)
    fprintf(fp, "P6\n%d %d\n255\n", width, height);

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            // Map pixel (x,y) to complex plane (-1.5 to 1.5)
            double complex z = (x - width / 2.0) * 3.0 / width + 
                               (y - height / 2.0) * 2.0 / height * I;
            int iter = 0;
            while (cabs(z) <= 2.0 && iter < max_iter) {
                z = z * z + c;
                iter++;
            }

            // Simple "Psychedelic" Color mapping
            unsigned char r = (iter % 8) * 32;
            unsigned char g = (iter % 16) * 16;
            unsigned char b = (iter % 32) * 8;

            if (iter == max_iter) r = g = b = 0; // Black for "inside"

            fputc(r, fp);
            fputc(g, fp);
            fputc(b, fp);
        }
    }

    fclose(fp);
    printf("Fractal saved to julia.ppm\n");
    return 0;
}