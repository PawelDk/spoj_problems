# 3410, SAMER08F - Feynman
# It was added as c++ code (below) because Python was not available

N = []
i = 0
while True:  # input
    n = int(input())
    if n == 0:
        break
    N.append(n)
    i += 1

for j in N:  # calculations
    sum_of_all = 0
    for i in range(j):
        if i == 0:
            sum_of_this_units = j ** 2
        else:
            # sum_of_this_units = (j - i) ** 2
            sum_of_this_units = (j - i) * (j - i)
        sum_of_all += sum_of_this_units
    print(sum_of_all)

"""
#include <iostream>
using namespace std;

int main()
{

    int n;
    int N[1000];
    int i = 0;
    while (true) {
        cin >> n;
        if (n == 0) {
            break;
        }
        N[i]=n;
        i++;
    }
    
    for (int k=0;k<i;k++) {
        double sum_of_all = 0;
        double sum_of_this_units = 0;
        for (int m=0;m<N[k];m++) {
            if (m==0) {
                sum_of_this_units = N[k] * N[k];
            }
            else {
                sum_of_this_units = (N[k] - m) * (N[k] - m);
            }
            sum_of_all = sum_of_all + sum_of_this_units;
        }
        cout << sum_of_all << endl;
    }
    
    return 0;
}
"""
