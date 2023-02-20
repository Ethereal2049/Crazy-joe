#include <iostream>

using namespace std;

int main()
{
    int number1, number2, sum, difference;
    float quotient;
    
    cout << "Enter The First Number And The Second Number : ";
    cin >> number1 >> number2;
    
    sum = number1 + number2;
    difference = number1 - number2;
    
    cout <<"The Sum Of "<<number1<<" And "<<number2<<" is "<<sum<<endl;
    cout <<"The Difference Of "<<number1<<" And "<<number2<<" is "<<difference<<endl;
    
    if (number2 == 0)
    {
        cout<<"Can not divided by 0"<<endl;
    }
    else
    {
        quotient = static_cast<float>(number1) / number2;
        cout <<"The Quotient Of "<<number1<<" And "<<number2<<" is "<<quotient<<endl;
    }

    return 0;
}

