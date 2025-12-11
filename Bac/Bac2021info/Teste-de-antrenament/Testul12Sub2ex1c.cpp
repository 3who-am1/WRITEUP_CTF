#include <iostream>
using namespace std;

int main()
{
	int n, k, t, i, j;
	cin >> n >> k;
	t = 1;
	for(i=1; i<=n/k; i++)
	{
		for(j=1; j<=k; j++)
		{
			cout << 2*t << ' ';
		}
		t++;
	}
	for(i=n%k; i>=1; i--)
	{
		cout << 3*t << ' ';
	}

	return 0;

}

			
