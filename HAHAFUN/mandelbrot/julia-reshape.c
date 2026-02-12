#include <GL/glut.h>
#include <complex.h>
#include <math.h>
#include <stdlib.h>

float alpha = 0;

// This function now takes 'time' (alpha) to evolve the fractal constant
void JuliaColor(float x, float y, float z, float time) {
    // Morph the constant 'c' over time using sine/cosine
    // real part swings between -0.8 and -0.4, imag part between 0.1 and 0.3
    double complex c = (-0.7 + 0.1 * sin(time * 0.05)) + 
                       (0.27015 + 0.1 * cos(time * 0.03)) * I;
    
    // Use x and y for the complex starting point
    double complex jz = (x * 1.2) + (y * 1.2) * I; 
    int iter = 0;
    int max_iter = 40;

    while (cabs(jz) <= 2.0 && iter < max_iter) {
        jz = jz * jz + c;
        iter++;
    }

    if (iter == max_iter) {
        glColor3f(0.0, 0.0, 0.1); // Dark blue for the set interior
    } else {
        // Create a shifting color palette
        float r = (float)iter / max_iter;
        float g = 0.5 + 0.5 * sin(time * 0.1 + r);
        float b = 0.8;
        glColor3f(r, g, b);
    }
}

void DisplayFunc(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    glTranslatef(0, 0, -10);
    glRotatef(30, 1, 0, 0);
    glRotatef(alpha, 0, 1, 0);

    float v[8][3] = {
        {-1,-1,-1}, {1,-1,-1}, {1,1,-1}, {-1,1,-1},
        {-1,-1,1},  {1,-1,1},  {1,1,1},  {-1,1,1}
    };

    glBegin(GL_QUADS);
    // Define faces by vertex indices
    int faces[6][4] = {
        {0,1,2,3}, {4,5,6,7}, {0,4,7,3}, 
        {1,5,6,2}, {3,2,6,7}, {0,1,5,4}
    };

    for(int i = 0; i < 6; i++) {
        for(int j = 0; j < 4; j++) {
            int idx = faces[i][j];
            // Pass alpha so the color changes every frame
            JuliaColor(v[idx][0], v[idx][1], v[idx][2], alpha);
            glVertex3f(v[idx][0], v[idx][1], v[idx][2]);
        }
    }
    glEnd();

    alpha += 0.5; // Increase speed of rotation and evolution
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