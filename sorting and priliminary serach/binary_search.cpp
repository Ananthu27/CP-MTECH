#include <bits/stdc++.h>

using namespace std;

int binary_search(vector<int> a, int x){
    int p = 0, n=a.size();
    for (int i=n/2; i>=1; i/=2){
        while(p+i < n && a[p+i]<=x) p+=i;
        if (a[p]==x) break;
    }
    if (a[p]==x) return p;
    return -1;
}

int main() {
    vector<int> a = {4,2,1,3,6,7,8,13,24};
    sort(a.begin(),a.end());

    cout << binary_search(a,1);
}

// IMPORTANT REFER : cp cpp page 33-34.