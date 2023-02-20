#include <iostream>

using namespace std;

int main()
{
    double radius;
    float area;
    const float pi = 3.14159;
    float circumference;
    
    cout << "Enter the value for radius" << endl;
    cin >> radius;
    
    area = pi*radius*radius;
    circumference = 2*radius*pi;
    
    cout << "The area of the cricle with a radius of " << radius << " is " << static_cast<int>(area) << endl;
    cout << "The circumference of the cricle with a radius of " << radius << " is " << circumference << endl;
    
    return 0;
}
