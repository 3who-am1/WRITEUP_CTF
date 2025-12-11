#include <iostream>
using namespace std;

int main()
{
	int x,y,nr,i,aux;
	cin >> x >> y;
	if(x>y)
	{
          aux = x;
	  x = y;
	  y = aux;
	}
	nr=1;
	for(i=y; i>=x; i--)
	{
		cout << "1";
		if(nr>=x)
		{
			cout << "2";
		}
		nr=nr*3;
		cout << "1";
	}
	return 0;
}
