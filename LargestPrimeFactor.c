#include <stdio.h>


long long sieve(long long a)
{
  for(long long i = 2; i < a/2; i++)
    {
      if(a%i == 0) 
	return sieve(a/i);
    }
  return a;
}

int main()
{
  long long Num = 600851475143;
  long long factor;
  factor = sieve(Num);
  printf("%llu\n", factor);
  return 0;
}
