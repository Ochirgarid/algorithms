/**
    @file    sum_of_2_solution1.cpp
    @author  Altantur Bayarsaikhan (altantur)
    @purpose Find sum of 2 integers
    @version 1.0 25/10/17 
*/
#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream test_file;
    int m = 0, n = 0;
    long prod = 1;

    // Read from test files
    test_file.open ("../test/test1.txt");
    test_file >> m;
    test_file >> n;
    test_file.close();

    // Calculating production of range
    for(int i = m; i <= n; i++){
        prod = prod * i;
    }

    cout << "Product of range : " << prod << endl;
    return 0;
}

