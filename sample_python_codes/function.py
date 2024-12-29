def add_numbers(num1, num2):    
    result = num1 + num2        
    return result              

# This block only runs if the file is run directly
if __name__ == "__main__":
    # Function calls go here
    sum_result = add_numbers(5, 3)
    print(f"The sum is: {sum_result}")