

def main():
    integers =[]
    
    for i in range(10):
        while True:
            user_input = input(f"Enter integer {i+1}/10: ")
            try:
                number = int(user_input)
                integers.append(number)
                current_sum = sum(integers)
                current_max = max(integers)
                print(f"current sum = {current_sum}, current max = {current_max}")
                break
            except ValueError:
                print("Please enter a valid integer.")
                
if __name__ == "__main__":
    main()