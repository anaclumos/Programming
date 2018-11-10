#include <iostream>
using namespace std;

int main(){
    int trial;
    cin>>trial;

    string answers[trial];

    int map[40][2];
    map[0][0] = 1; map[0][1] = 0;
    map[1][0] = 0; map[1][1] = 1;

    for(int a = 2; a < 40; a++) {
        map[a][0] = map[a-1][0] + map[a-2][0];
        map[a][1] = map[a-1][1] + map[a-2][1];
    }

    for(int k = 0; k < trial; k++) {
        int x; cin>>x;
        answers[k] = to_string(map[x][0]) + " " + to_string(map[x][1]);
    }

    for(int k = 0; k < trial; k++) {
        cout<<answers[k]<<endl;
    }
    return 0;
}