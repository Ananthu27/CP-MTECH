#include <bits/stdc++.h>
using namespace std;

void display(vector<int> a){
    for (auto item : a){
        cout << item << " ";
    }
    cout << "\n";
}

void display_array(int a[],int size){
    for (int i=0;i<size;i++){
        cout << a[i] << " ";
    }
    cout << "\n";
}

bool comp(int a, int b){
    return a>b;
}

int main(){

    // SORTING ARRAY OF INT
    int  a[] = {10,2,2,4,7,6,4,3,1};
    int size = (sizeof(a)/sizeof(a[0]));
    display_array(a,size);
    sort(a+1,a+size-1);
    // USER DEFINED COMPARISON 
    sort(a,a+size,comp);
    display_array(a,size);

    cout << endl;

    // SORTING VECTOR<INT>
    vector<int> v={10,2,2,4,7,6,4,3,1};
    display(v);
    sort(v.begin(),v.end());
    display(v);
    sort(v.rbegin(),v.rend());
    display(v);

    cout << endl;

    // SORTING WITHIN A STRING 
    string s = "monkEY";
    sort(s.begin(),s.end());
    cout << s << endl;
    cout << endl;

    // SORTING A VECTOR OF PAIRS
    vector<pair<int,int>> vp = {{2,1},{1,2},{1,0},{1,-1}};
    for(auto item:vp){
        cout << "(" << item.first << "," << item.second << ") ";
    }
    cout << endl;
    sort(vp.begin(), vp.end());
    // sort(vp.rbegin(),vp.rend());
    for(auto item:vp){
        cout << "(" << item.first << "," << item.second << ") ";
    }
    cout <<endl;


    cout <<endl;
    // SORTING A VECTOR OF tuples
    vector<tuple<int,int,int>> vt = {{2,1,4},{1,2,4},{1,0,10},{1,0,2}};
    for(auto item:vt){
        cout << "(" << get<0>(item) << "," << get<1>(item) << "," << get<2>(item) << ") ";
    }
    cout << endl;
    sort(vt.begin(), vt.end());
    // sort(vp.rbegin(),vp.rend());
    for(auto item:vt){
        cout << "(" << get<0>(item) << "," << get<1>(item) << "," << get<2>(item) << ") ";
    }
    cout << endl;
    return 0;
}