#include <iostream>
using namespace std;

int main()
{
	int a,b,x,aux;
	
	cout << "a= ";
	cin >> a;
	cout << "b= ";
	cin >> b;

	if(a<b)
	{
		aux=a;
		a=b;
		b=aux;
	}
	for(x=a; x>=b; x--)
	{
		if(x%2!=0)
		{
			cout << x << " ";
		}
	}
	return 0;
}
