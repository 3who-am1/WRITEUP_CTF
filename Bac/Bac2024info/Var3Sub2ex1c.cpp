#include <iostream>
using namespace std;

int main()
{
	int n,p,i,x;
	cin >> n;
	p = 1;
	for(i=1;i<=n; i++)
	{
		cin >> x;
		do
		{
			x=x/3;
		
		}while(x>3);
		
		if(x!=0)
		{
			p=p*x;
		}
	}
	cout << p;
	return 0;
}
