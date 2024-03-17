#include <bits/stdc++.h>
using namespace std;
int main (){
    vector<int> a = {1,3,8,2,9,2,5,6};
    for(int i=0;i<a.size();i++){
        for(int j=i+1;j<a.size();j++){
            if (a[i]>a[j]){
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }

    for (auto item : a){
        cout << item << " ";
    }
    cout << "\n";
    return 0;
}