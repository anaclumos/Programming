#include <iostream>
#include <vector>
#include <math.h>

int checkPrime(int i, std::vector<int> v) {
    int searchscope = (int)sqrt(i);
    for(int idx = 0; idx < v.size(); idx++) {
        if(i%v[idx]==0) return false;
        if(v[idx] >= searchscope) break;
    }
    return true;
}

int main() {
    int input;
    std::vector<int> v;
    v.push_back(2);
    int iterator = 3;

    printf("Find prime number of order ... : ");
    scanf("%d", &input);

    while(v.size() < input) {
        if(checkPrime(iterator, v)) v.push_back(iterator);
        iterator += 2;
    }

    for(int i=0; i<v.size(); ++i)
        std::cout << v[i] << ", ";
    printf("\nRequested value is %d.\n", v.back());
    return 0;
}