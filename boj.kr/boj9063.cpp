#include <iostream>

using namespace std;

int main() {

	int testcase;
	int dotNum;
	int maxY, maxX, minY, minX;
	int tempX, tempY;

	cin>>testcase;
	for(int loop = 0; loop < testcase; loop++) {
		cin>>dotNum;
		for(int dot=0; dot < dotNum; dot++) {
			cin>>tempX>>tempY;
			if(dot==0) {
				maxX = minX = tempX;
				maxY = minY = tempY;
			}
			if(tempX > maxX) {maxX = tempX;}
			if(tempY > maxY) {maxY = tempY;}
			if(tempX < minX) {minX = tempX;}
			if(tempY < minY) {minY = tempY;}
		}
		int Area = (maxX-minX)*(maxY-minY);
		cout<<Area<<endl;
	}
}