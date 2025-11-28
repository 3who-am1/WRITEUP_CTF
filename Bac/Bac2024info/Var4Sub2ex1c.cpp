#include <iostream>
using namespace std;

int main()
{
	int n,i,m;
	cin >> n;
	i = 1;
	while(i<=n)
	{
		m=i;
		while(m%2==0)
		{
			m=m/2;
		}
		if(m!=i)
		{
			cout << m << " ";
		}
		i++;
	}
	return 0;
}
