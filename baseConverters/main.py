import sys
import math

# Use
#   alias factorTree='cd ~ && cd rootdir-scripts && cd factorTree && f(){pipenv run python3 factorTree.py "$1"; unset -f f; cd ~;}; f'
# to run from terminal


if __name__ == "__main__":
    args = sys.argv

    if len(args) < 3:
        print("Need at least 2 operators")
    elif len(args) > 4:
        print("Yo too many params")

    fromBase = sys.argv[1]
    toBase = sys.argv[3]
    num = sys.argv[2]

    if (fromBase == "10" or fromBase == "decimal") and (
        toBase == "2" or toBase == "binary"
    ):
        resp = ""
        num = int(num)  # cast to int
        # Padding
        numDigits = math.log2(num) // 1 + 1
        padding = ""
        while numDigits % 4 != 0:
            padding += "0"
            numDigits += 1
        while num > 0:
            bit = num % 2
            resp = "1" + resp if bit == 1 else "0" + resp
            num = num // 2

        count = 0
        resp = padding + resp
        for char in resp:
            count += 1
            if count % 4 == 0:
                print(char, end=" ")
            else:
                print(char, end="")
        print()
    elif (fromBase == "10" or fromBase == "decimal") and (
        toBase == "16" or toBase == "hex"
    ):
        print("bin2dec")
    elif (fromBase == "2" or fromBase == "binary") and (
        toBase == "10" or toBase == "decimal"
    ):
        resp = 0
        power = 0
        for i in range(len(num) - 1, -1, -1):
            resp += int(num[i]) * pow(2, power)
            power += 1
        print(resp)
    elif (fromBase == "2" or fromBase == "binary") and (
        toBase == "16" or toBase == "hex"
    ):
        print("bin2hex")
    elif (fromBase == "16" or fromBase == "hex") and (
        toBase == "2" or toBase == "binary"
    ):
        print("hex2bin")
    elif (fromBase == "16" or fromBase == "hex") and (
        toBase == "10" or toBase == "decimal"
    ):
        print("bin2hex")
