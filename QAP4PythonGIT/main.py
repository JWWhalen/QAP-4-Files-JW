# QAP 4 One Stop Insurance Company
#   Written by: Justin Whalen
# July 23, 2023 - July 25, 2023



import datetime
import FormatValues as FV
import time
from tqdm import tqdm


# Read default data from the File
f = open("OSICDef.dat", "r")
PolicyNum = int(f.readline())
BasicPrem = float(f.readline())
Discount = float(f.readline())
LiabCover = float(f.readline())
GlassCover = float(f.readline())
LoanCarCover = float(f.readline())
HSTRate = float(f.readline())
ProFee = float(f.readline())

print("Welcome to the One Stop Insurance Company!")


while True:
    # Get user input for customer details
    FirstName = input("Enter customer's first name: ").title()
    LastName = input("Enter customer's last name: ").title()
    StAddress = input("Enter customer's street address: ")
    City = input("Enter customer's city: ").title()
    ProvinceList = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'NT', 'YT', 'NU']
    while True:
        Province = input(f"Enter customer's province (XX): ").upper()
        if Province not in ProvinceList:
            print("Invalid province. Please try again.")
        else:
            break
    PostalCode = input("Enter customer's postal code: ")
    PhoneNumber = input("Enter customer's phone number (##########): ")
    NumCars = int(input("Enter the number of cars being insured: "))
    ExtraLiability = input("Do you want extra liability coverage? (Y/N): ").upper()
    GlassCoverage = input("Do you want optional glass coverage? (Y/N): ").upper()
    LoanerCar = input("Do you want optional loaner car coverage? (Y/N): ").upper()
    PaymentMethodList = ['FULL', 'MONTHLY']
    while True:
        PaymentMethod = input(f"Enter payment method (FULL, MONTHLY): ").upper()
        if PaymentMethod not in PaymentMethodList:
            print("Invalid payment method. Please try again.")
        else:
            break

    ExtraLiabilityCost = 0
    GlassCoverageCost = 0
    LoanerCarCost = 0
    if ExtraLiability == 'Y':
        ExtraLiabilityCost += NumCars * LiabCover
    if GlassCoverage == 'Y':
        GlassCoverageCost += NumCars * GlassCover
    if LoanerCar == 'Y':
        LoanerCarCost += NumCars * LoanCarCover
    TotalExtraCosts = ExtraLiabilityCost + GlassCoverageCost + LoanerCarCost

    premium = BasicPrem + ((BasicPrem - (Discount * BasicPrem))* (NumCars - 1))
    TotalInsPrem = premium + TotalExtraCosts
    HSTAmount = TotalInsPrem * HSTRate
    TotalCost = TotalInsPrem + HSTAmount

    # Calculate monthly payment if selected
    if PaymentMethod == 'MONTHLY':
        MonthlyPay = (TotalCost + ProFee) / 8

    f = open("Policies.dat", "a")
    InvoiceDate = datetime.datetime.now()
    NextPaymentDate = (datetime.datetime.now().replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
    policy_line = f"{PolicyNum}, {InvoiceDate}, {FirstName}, {LastName}, {StAddress}, {City}, {Province}, {PostalCode}, {PhoneNumber}, {NumCars}, {ExtraLiability}, {GlassCoverage}, {LoanerCar}, {PaymentMethod}, {TotalInsPrem:.2f}\n"
    f.write(policy_line)
    f.close()

    # Display the receipt
    print()
    print(" ==================== One Stop Insurance Company ====================")
    print(f"|  Policy Number: {PolicyNum}                      Invoice Date: {FV.FDateS(InvoiceDate)} |")
    print("|                                                                    |")
    print("|   Customer Information:                      Policy information:   |")
    print("|--------------------------------------------------------------------|")
    print(f"|   {FirstName + ' ' + LastName:<20s}                       # of Cars Insured:  {NumCars} | ")
    print(f"|   {StAddress:<20s}                       Liability Coverage: {ExtraLiability} |\n"
          f"|   {City:<20s}                       Glass Coverage:     {GlassCoverage} |\n"
          f"|   {Province:<2s}                                         Loaner Car Coverage:{LoanerCar} |\n"
          f"|   {PostalCode:<6s}                                                           |")
    print(f"|   {PhoneNumber:<10}                                                       |")
    print(f"|                                                                    |")
    print(f"|--------------------------------------------------------------------|")
    print("|            ********************************************            |")
    print(f"|            *   Extra Liability Cost:     {FV.FDollar2(ExtraLiabilityCost):>10s}   *            |")
    print(f"|            *   Glass Coverage Cost:      {FV.FDollar2(GlassCoverageCost):>10s}   *            |")
    print(f"|            *   Loaner Car Cost:          {FV.FDollar2(LoanerCarCost):>10s}   *            |")
    print(f"|            *   Total Extra Costs:        {FV.FDollar2(TotalExtraCosts):>10s}   *            |")
    print("|            ********************************************            |")
    print(f"|                                                                    |")
    print(f"|                 Payment Method:           {PaymentMethod:>7s}                  |")
    print(f"|                 Insurance Premium:     {FV.FDollar2(TotalInsPrem):>10s}                  |")
    print(f"|                 HST:                   {FV.FDollar2(HSTAmount):>10s}                  |")
    print(f"|                 Total Cost:            {FV.FDollar2(TotalCost):>10s}                  |")
    print(f"|                                                                    |")
    if PaymentMethod == 'MONTHLY':
        print(f"|                 Monthly Payment:       {FV.FDollar2(MonthlyPay):>10s}                  |")
        print(f"|                   Next payment Date: {FV.FDateS(NextPaymentDate)}                    |")
    print("======================================================================")


    # Increase the policy number for the next entry
    PolicyNum += 1
    print("Saving Policy Information...")
    for _ in tqdm(range(100), desc="Processing policy information", ncols=80, colour="Blue"):
        # Simulating some processing delay, you can remove this line
        time.sleep(0.05)
    print()
    print("Policy Information Successfully Saved! ")
    print()

    # Ask if the user wants to enter another policy
    choice = input("Do you want to enter another policy? (Y/N): ").upper()
    if choice != 'Y':
        # Write current default values back to OSICDef.dat before exiting
        defaults_file = open("OSICDef.dat", "w")
        defaults_file.write(
            f"{PolicyNum}\n{BasicPrem}\n{Discount}\n{LiabCover}\n{GlassCover}\n{LoanCarCover}\n{HSTRate}\n{ProFee}\n")
        defaults_file.close()
        print()
        print("Policy information processed and saved. Goodbye!")
        break