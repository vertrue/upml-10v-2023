#include <iostream>

using namespace std;

int main()
{
    // розмір масиву
    int n;
    cin >> n;
    
    // створення масиву
    int a[n];
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    
    // сума елементів на непарних місцях (нумерація з 0)
    int summa = 0;
    for(int i = 0; i < n; i++)
    {
        if(i % 2 == 1)
        {
            summa += a[i];
        }
    }
    
    // виведення суми 
    cout << summa << endl;
}
