# exception handling

try:
    number = int(input("Enter a number: "))
    print(1/ number)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Enter only number please.")
except Exception:
    print("Somrething went wrong.")
finally:
    print("Do some cleanup.")