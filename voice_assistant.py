```python
import datetime

def respond_to_command(command):
    if command.lower() == "hello":
        return "Hello there!"
    elif command.lower() == "time":
        now = datetime.datetime.now()
        return now.strftime("%H:%M:%S")
    elif command.lower() == "date":
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d")
    else:
        return "Sorry, I didn't understand that command."

def main():
    while True:
        user_input = input("You: ")
        response = respond_to_command(user_input)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
```