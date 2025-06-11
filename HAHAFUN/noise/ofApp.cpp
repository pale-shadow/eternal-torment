#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup() {

	ofSetFrameRate(30);
	ofSetWindowTitle("openFrameworks");

	ofBackground(0);
	ofSetLineWidth(2);
	ofEnableDepthTest();
}

//--------------------------------------------------------------
void ofApp::update() {

	ofSeedRandom(39);
}

//--------------------------------------------------------------
void ofApp::draw() {

	int span = 15;
	for (int z = 0; z > -span; z -= span) {

		auto noise_seed = ofRandom(1000);
		for (int x = 0; x < 720; x += span) {

			for (int y = 0; y < 720; y += span) {

				ofPushMatrix();
				ofTranslate(x, y, z);

				auto noise_value = ofNoise(noise_seed, x * 0.0035, y * 0.0035, ofGetFrameNum() * 0.005);

				if (noise_value > 0.43 && noise_value <= 0.48) {
				
					auto power = ofMap(noise_value, 0.43, 0.48, 1, 0);
					ofRotateZ(ofRandom(1000) * power);
					ofRotateY(ofRandom(1000) * power);
					ofRotateX(ofRandom(1000) * power);

					ofSetColor(0);
					ofFill();
					ofDrawBox(ofMap(noise_value, 0.43, 0.48, 0, span));

					ofSetColor(255);
					ofNoFill();
					ofDrawBox(ofMap(noise_value, 0.43, 0.48, 0, span));
				}

				if (noise_value > 0.48 && noise_value < 0.52) {

					ofSetColor(0);
					ofFill();
					ofDrawBox(span);

					ofSetColor(255);
					ofNoFill();
					ofDrawBox(span);
				}

				if (noise_value > 0.52 && noise_value <= 0.57) {

					auto power = ofMap(noise_value, 0.52, 0.57, 0, 1);
					ofRotateZ(ofRandom(1000) * power);
					ofRotateY(ofRandom(1000) * power);
					ofRotateX(ofRandom(1000) * power);

					ofSetColor(0);
					ofFill();
					ofDrawBox(ofMap(noise_value, 0.57, 0.52, 0, span));

					ofSetColor(255);
					ofNoFill();
					ofDrawBox(ofMap(noise_value, 0.57, 0.52, 0, span));
				}

				ofPopMatrix();
			}
		}
	}
}

//--------------------------------------------------------------
int main() {

	ofSetupOpenGL(720, 720, OF_WINDOW);
	ofRunApp(new ofApp());
}
