class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

    # Initialize result array with zeros
        res = [0] * (len(num1) + len(num2))

    # Reverse both strings to simulate from least significant digit
        num1, num2 = num1[::-1], num2[::-1]

    # Multiply each digit and add to result
        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = int(num1[i]) * int(num2[j])
                res[i + j] += mul
            # Carry forward
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

    # Remove leading zero if present
        while len(res) > 1 and res[-1] == 0:
            res.pop()

    # Convert result back to string
        return ''.join(map(str, res[::-1]))
        