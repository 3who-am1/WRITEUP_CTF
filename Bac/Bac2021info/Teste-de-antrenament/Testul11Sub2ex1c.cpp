#include <iostream>
using namespace std;

int main()
{
	int m, n, aux;
	cin >> m >> n;
	if(m>n)
	{
		aux = n;
		n = m;
		m = aux;
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
