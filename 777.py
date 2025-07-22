import sys

if len(sys.argv) != 2:
    print("Використання: python script.py <число>", file=sys.stderr)
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("Помилка: введено не число", file=sys.stderr)
    sys.exit(2)

if number % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")
