
class GenerateNum:
    #constructor takes a single parameter number, which is expected to be a five-digit integer
    def __init__(self, number: int):
        #a five-digit integer is taken as  input and raises an error if it’s not within the range 10000 to 99999.
        if not (10000 <= number <= 99999):
            raise ValueError("The number must be a five-digit integer.")
        self.number = number

        #Extracts each digit from the end by taking n % 10.
    def reverse_number(self) -> int:
        n = self.number
        reversed_num = 0
        while n > 0:
            last_digit = n % 10
            # The reversed number is built by progressively multiplying the current reversed number by 10 and adding the extracted digit.
            reversed_num = reversed_num * 10 + last_digit
            #Divides n by 10 in each loop iteration to move to the next digit
            n //= 10
        return reversed_num

        #Extracts each digit and accumulates the sum
    def sum_of_digits(self) -> int:
        n = self.number
        total = 0
        while n > 0:
            total += n % 10
            #Divides n by 10 each time to move through each digit.
            n //= 10
        return total


    #Generate a new number by adding 1 to each digit, wrapping around 9 to 0
    def increment_digits(self) -> int:    
        n = self.number
        incremented_number = 0
        place = 1
        while n > 0:
            digit = (n % 10 + 1) % 10
            incremented_number = digit * place + incremented_number
            place *= 10
            n //= 10
        return incremented_number

#Using the number provided
number = 12391
machine = GenerateNum(number)

print("Original number:", number)
print("Reversed number:", machine.reverse_number())
print("Sum of digits:", machine.sum_of_digits())
print("Incremented digits:", machine.increment_digits())
