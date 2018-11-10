#include <iostream>
#include <cmath>
#include <string>

using namespace std;
 
int main(){

    // Initial Variables
    int x1,x2,y1,y2,r1,r2;
    double distance;
    int cases;
    
    cin >> cases;

    while(cases>0){

        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        distance = sqrt(pow(x1-x2,2) + pow(y1-y2,2));

        if(x1 == x2 && y1 == y2 && r1 == r2) {
            //Infinite
            cout<<"-1"<<endl;
        }

        else if ( r1 + r2 == distance || r1 + distance == r2 || r2 + distance == r1 ) {
            //Touches
            cout<<"1"<<endl;
        }

        else if ( r1 + r2 < distance || r1 + distance < r2 || r2 + distance < r1 ) {
            //Can't Touch
            cout<<"0"<<endl;
        }

        else{
            cout<<"2"<<endl;
        }
        cases--;
    }
}