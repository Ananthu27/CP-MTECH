#include<bits/stdc++.h>

using namespace std ;
int main(){

    vector<int> a = {1,2,2,3,4,5,6,3,2,3,2};
    sort(a.begin(),a.end());
    for (auto item : a){
        cout << item << " ";
    }
    cout << endl;
    
    auto i = lower_bound(a.begin(),a.end(),2)-a.begin();
    auto j = upper_bound(a.begin(),a.end(),2)-a.begin();
    cout << "first occurence of 2 at index "<< i <<endl;
    cout << "last occurence of 2 at index " << j-1 << endl;
    cout << "there are a total of ";
    cout << upper_bound(a.begin(),a.end(),2) - lower_bound(a.begin(),a.end(),2);
    cout << " 2's in the vector" << endl;
    return 0;
}