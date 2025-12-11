#include <iostream>
using namespace std;

int main()
{
	int n,x,y,ok,i;
	cin >> n >> x >> y;
	ok = 0;
	for(i=1; i<=n; i++)
	{
		if((i%x==0 && i%y!=0) || (i%x!=0 && i%y==0))
		{
			cout << i << ' ';
			ok = 1;
		}
	}
	if(ok==0)
	{
		cout << 0;
	}

	return 0;
}
