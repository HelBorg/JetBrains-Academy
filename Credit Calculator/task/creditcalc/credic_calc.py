from math import log, ceil, floor
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--type", required=False)
ap.add_argument("--principal", required=False)
ap.add_argument("--payment", required=False)
ap.add_argument("--periods", required=False)
ap.add_argument("--interest", required=False)
args = vars(ap.parse_args())

type_ = args["type"]
a = int(args["payment"]) if args["payment"] is not None else None
p = int(args["principal"]) if args["principal"] is not None else None
n = int(args["periods"]) if args["periods"] is not None else None
credit_interest = float(args["interest"]) if args["interest"] is not None else None

if type_ is None \
        or "annuity" not in type_ and "diff" not in type_ \
        or len(args) < 4 \
        or "diff" in type_ and a is not None\
        or a is not None and a < 0\
        or p is not None and p < 0\
        or n is not None and n < 0\
        or credit_interest is None \
        or credit_interest < 0:

    print("Incorrect parameters")
    exit()

credit_interest = float(credit_interest)
i = credit_interest / 12 / 100

if type_ in "diff":
    overp = -p
    for m in range(1, n + 1):
        d = p / n + i * (p - p * (m - 1) / n)
        print(f"Month {m}: paid out {ceil(d)}")
        overp += ceil(d)
    print("\nOverpayment =", overp)
    exit()

if n is None:
    principal_ = a / (a - i * p)
    count_of_periods = log(principal_, 1 + i)
    n = ceil(count_of_periods)
    string_ = " "
    another = False
    if n // 12 != 0:
        string_ += str(n // 12) + " years"
        another = True
    if n % 12 != 0:
        if another is True:
            string_ += " and "
        string_ += str(n % 12) + " months"
    print("You need" + string_ + " to repay this credit!")

if a is None:
    a = ceil(p * i * (1 + i) ** n / ((1 + i) ** n - 1))
    print("Your annuity payment = " + str(a) + "!")

if p is None:
    p = floor(a * ((1 + i) ** n - 1) / (i * ((1 + i) ** n)))
    print("Your credit principal = " + str(p) + "!")

print("\nOverpayment =", ceil(a * n - p))
