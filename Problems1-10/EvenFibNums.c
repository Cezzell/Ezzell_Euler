#include <stdio.h>

int main()
{
  unsigned int prev = 1;
  unsigned int curr = 2;
  unsigned int sum = 0;
  int count = 2;
  while (curr <= 4000000)
    {
      if (count == 2)
	{
	  sum += curr;
	  count = 0;
	}
      else
	count += 1;
      curr = prev + curr;
      prev = curr - prev;
    }
  printf("%i\n" , sum);
  return 0;
}
      
