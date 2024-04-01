"""Let's use iostream in Python."""

from iostream import cin, cout


def main():
    data = [None, float]
    cout << "Please enter a name and an age: ";
    cin >> data;
    name, age = data
    cout << name << " is " << age << " years old!" << '\n';


if __name__ == "__main__":
    main()
