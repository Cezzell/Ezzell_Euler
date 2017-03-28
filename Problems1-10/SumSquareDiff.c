#include <stdio.h>

//This program will find the difference between 1^2 +2^2 ... and (1+2+...)^2

int main()
{
  unsigned int res = 0;
  unsigned int sum = 5050*5050;
  for(int i = 1; i < 101; i++)
    {
      res = res + i*i;
    }
  
  res = sum - res;
  printf( "%i", res);
  return 0;
}
