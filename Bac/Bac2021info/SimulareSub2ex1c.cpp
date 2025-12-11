#include <iostream>
using namespace std;

int main()
{
	int x, p, y, c;
	cin >> x;
	p = 1;
	y = 0;
	do
	{
		c = x%10;
		x = x/10;
		if(c!=0)
		{
			if(x%10<c)
			{
				y = y*10+c;
			}
			else
			{
				y = c*p+y;
			}
			p=p*10;
		}
	}while(x!=0);
	cout << y;
	return 0;
}
