#include <GL/glut.h>
#include <complex.h>
#include <math.h>

float alpha = 0;

void GetJuliaColor(float x, float y, float z, float time) {
    // Evolving constant c for the "Crystal Ball" look
    double complex c = (0.355534 - 0.1 * sin(time * 0.02)) + 
                       (0.33723 + 0.1 * cos(time * 0.01)) * I;
    
    // Map 3D sphere coordinates to 2D complex plane
    double complex jz = (x * 1.5) + (y * 1.5) * I;
    int iter = 0, max_iter = 50;

    while (cabs(jz) <= 2.0 && iter < max_iter) {
        jz = jz * jz + c;
        iter++;
    }

    if (iter == max_iter) {
        glColor4f(0.0, 0.0, 0.1, 0.8); // Deep core
    } else {
        float hue = (float)iter / max_iter;
        // Electric Blue/Magenta "Crystal" colors
        glColor4f(0.5 + 0.5 * sin(hue * 6.28 + time * 0.05), 
                  0.2, 
                  0.8 + 0.2 * cos(hue * 3.14), 0.6);
    }
}

void DrawCrystalBall() {
    int slices = 40, stacks = 40;
    float r = 1.5;

    // Manually drawing the sphere to apply fractal colors to each vertex
    for (int i = 0; i < stacks; i++) {
        float phi1 = M_PI * (float)i / stacks;
        float phi2 = M_PI * (float)(i + 1) / stacks;

        glBegin(GL_QUAD_STRIP);
        for (int j = 0; j <= slices; j++) {
            float theta = 2.0 * M_PI * (float)j / slices;

            for (int k = 0; k < 2; k++) {
                float p = (k == 0) ? phi1 : phi2;
                float x = r * sin(p) * cos(theta);
                float y = r * sin(p) * sin(theta);
                float z = r * cos(p);

                GetJuliaColor(x, y, z, alpha);
                glVertex3f(x, y, z);
            }
        }
        glEnd();
    }
}

void DisplayFunc(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    glTranslatef(0, 0, -8);
    glRotatef(alpha * 0.5, 0, 1, 0); // Slow rotation

    // Enable blending for a "glassy" transparent effect
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

    DrawCrystalBall();

    alpha += 0.8;
    glutSwapBuffers();
    glutPostRedisplay();
}

void ReshapeFunc(int width, int height) {
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(20, (float)width/height, 5, 15);
    glViewport(0, 0, width, height);
    glMatrixMode(GL_MODELVIEW);
}

void KeyboardFunc(unsigned char key, int x, int y) {
    if (key == 'q' || key == 'Q' || key == 27) exit(0);
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Fractal Julia Cube");
    glEnable(GL_DEPTH_TEST);
    glutDisplayFunc(DisplayFunc);
    glutReshapeFunc(ReshapeFunc);
    glutKeyboardFunc(KeyboardFunc);
    glutMainLoop();
    return 0;
}