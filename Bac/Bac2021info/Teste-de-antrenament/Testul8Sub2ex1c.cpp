#include <iostream>
using namespace std;

int main()
{
	int n, x, i;
	cin >> n;
	x = 0;
	for(i=1; i<=n; i++)
	{
		if(i%2==0)
		{
			x=x+i*i;
		}
		else
		{
			x=x+(i+1)*(i+1);
		}
	}
	cout << x;
	return 0;
}
