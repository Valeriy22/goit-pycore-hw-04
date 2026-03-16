def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: enter name and phone. Example: add John 1234567890"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: enter name and phone. Example: change John 0987654321"
    name, phone = args
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: enter a name. Example: phone John"
    name = args[0]
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
```

**Структура програми:**
```
parse_input()      — парсер команд
add_contact()      — додати новий контакт
change_contact()   — змінити існуючий контакт
show_phone()       — показати номер за ім'ям
show_all()         — показати всі контакти
main()             — цикл запит-відповідь
```

**Приклад сесії:**
```
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add John 1234567890
Contact added.
Enter a command: add Vika 0991234567
Contact added.
Enter a command: all
John: 1234567890
Vika: 0991234567
Enter a command: change John 0987654321
Contact updated.
Enter a command: phone John
0987654321
Enter a command: phone Mike
Error: contact 'Mike' not found.
Enter a command: ADD SARA 1111111111
Contact added.
Enter a command: exit
Good bye!
