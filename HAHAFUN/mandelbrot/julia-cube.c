#include <GL/glut.h>
#include <complex.h>
#include <math.h>

float alpha = 0;

// Function to map a 3D coordinate to a color based on the Julia Set
void JuliaColor(float x, float y, float z) {
    // We use two coordinates (e.g., x and y) to pick a point in the complex plane
    double complex c = -0.7 + 0.27015 * I;
    double complex jz = (x * 1.5) + (y * 1.5) * I; 
    int iter = 0;
    int max_iter = 32;

    while (cabs(jz) <= 2.0 && iter < max_iter) {
        jz = jz * jz + c;
        iter++;
    }

    if (iter == max_iter) {
        glColor3f(0, 0, 0); // Interior is black
    } else {
        // Color based on escape speed
        glColor3f((float)iter/max_iter, 0.2, 1.0 - (float)iter/max_iter);
    }
}

void DisplayFunc(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    glTranslatef(0, 0, -10);
    glRotatef(30, 1, 0, 0);
    glRotatef(alpha, 0, 1, 0);

    glBegin(GL_QUADS);
    float coords[6][4][3] = {
        {{-1,-1,-1}, {-1,-1, 1}, {-1, 1, 1}, {-1, 1,-1}}, // Left
        {{ 1,-1,-1}, { 1,-1, 1}, { 1, 1, 1}, { 1, 1,-1}}, // Right
        {{-1,-1,-1}, {-1,-1, 1}, { 1,-1, 1}, { 1,-1,-1}}, // Bottom
        {{-1, 1,-1}, {-1, 1, 1}, { 1, 1, 1}, { 1, 1,-1}}, // Top
        {{-1,-1,-1}, {-1, 1,-1}, { 1, 1,-1}, { 1,-1,-1}}, // Back
        {{-1,-1, 1}, {-1, 1, 1}, { 1, 1, 1}, { 1,-1, 1}}  // Front
    };

    for(int i=0; i<6; i++) {
        for(int j=0; j<4; j++) {
            JuliaColor(coords[i][j][0], coords[i][j][1], coords[i][j][2]);
            glVertex3f(coords[i][j][0], coords[i][j][1], coords[i][j][2]);
        }
    }
    glEnd();

    alpha += 0.5;
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

