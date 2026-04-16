class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            string = str(i)
            if i % 15 == 0:
                string = "FizzBuzz"
            elif i % 3 == 0:
                string = "Fizz"
            elif i % 5 == 0:
                string = "Buzz"
            result.append(string) 
        return result      