#include <iostream>
using namespace std;

int main()
{
	int n, s, d, p;
	cin >> n;
	s = 0;
	d = 2;
	while(d*d<=n)
	{
		p=0;
		while(n%d==0)
		{
			n=n/d;
			p=1;
		}
		s=s+d*p;
		d++;
	}
	if(n!=1)
	{
		s=s+n;
	}
	cout << s;
	return 0;
}
