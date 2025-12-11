#include <iostream>
using namespace std;

int main()
{
	int m, n, aux;
	cin >> m >> n;
	if(m>n)
	{
		aux = m;
		m = n;
		n = aux;
	}
	if(m%2==0)
	{
		m++;
	}
	while(m<=n)
	{
		m=m+2;
		cout << '*';
	}
	return 0;

}

