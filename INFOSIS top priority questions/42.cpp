#include <iostream>
#include <vector>
using namespace std;

int reverse(vector<int> &v){

    int s = 0;
    int e = v.size()-1;

    for(int i=0;i<v.size();i++){
        while(s<e){
            swap(v[s],v[e]);
            s++;
            e--;
        }
    }
  return v;
}

int main(){
     cout << "Enter the size of the array" << endl;

     int n;

     cin>>n;

    vector<int> arr(n);

    cout << "Enter the elements of an array : " << endl;

    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    int result = reverse(arr);

    cout << "The reverse of the array : " << result <<endl;

return 0;
}