class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(n):
            print(int((i+1) % 3))
            if int((i+1) % 3) == 0 and int((i+1) % 5) == 0:
                result.append("FizzBuzz")
            elif int((i+1) % 3) == 0:
                result.append("Fizz")
            elif int((i+1) % 5) == 0:
                result.append("Buzz")
            else:
                result.append(str(i+1))
                
        return result