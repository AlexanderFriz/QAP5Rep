# One Stop Insurance Company Data Files & Reports
# Alex Frizzell
# December 1st, 2021

import datetime

# Constants
EXTRA = 130.00
GLASS = 86.00
LOAN = 58.00

while True:
    def FormatDollar(DollarValue):
        DollarValueStr = "${:,.2f}".format(DollarValue)
        DollarValuePad = "{:>10}".format(DollarValueStr)
        return DollarValuePad

    # User Inputs
    CustFirstName = input("Enter The First Name: ")
    CustLastName = input("Enter The Last Name: ")
    Address = input("Enter The Address: ")
    City = input("Enter The City Name: ")
    Province = input("Enter The Province: ")
    Postal = input("Enter The Postal Code: ")
    PhoneNum = input("Enter The Phone: ")
    NumCarsInsured = int(input("Enter The Number of Cars Insured: "))

    PolicyNumData = 0
    BasicPremData = 0
    InsurancePrem = 0
    DisAddCarsData = 0
    ExtraLiabilityData = 0
    GlassCoverageData = 0
    LoanerData = 0
    HSTRateData = 0
    FeeForMonthlyPayData = 0
    Date = 0
    TotExtraCost = 0
    HST = 0
    TotInsurancePrem = 0
    TotCost = 0
    MonthlyPay = 0

    while True:
        ExtraLiability = input("Enter Y for Yes or N for No if you Want Extra Liabilities(up to 1,000,000): ")
        if ExtraLiability == "":
            print("Invalid - Can't be blank ...")
        elif ExtraLiability.upper() != "Y" and ExtraLiability.upper() != "N":
            print("Invalid Must be a Y or N")
        else:
            break

    while True:
        GlassCoverage = input("Enter Y or N For Glass Coverage: ")
        if GlassCoverage == "":
            print("Invalid Cant be Blank")
        elif GlassCoverage.upper() != "Y" and GlassCoverage.upper() != "N":
            print("Invalid must be a Y or N")
        else:
            break

    while True:
        Loaner = input("Enter Y or N For A Loaner Car: ")
        if Loaner == "":
            print("Invalid cant be Blank")
        elif Loaner.upper() != "Y" and Loaner.upper() != "N":
            print("Invalid must be a Y or N")
        else:
            break
    FullOrMonthly = input("Enter F If You Want To Pay In Full or M If You Want To Pay Monthly")

    # Calculations
    f = open("OSICDef.dat", "r")
    for OSICLine in f:
        OSICData = OSICLine.split(",")
        PolicyNumData = OSICData[0].strip()
        BasicPremData = float(OSICData[1].strip())
        DisAddCarsData = float(OSICData[2].strip())
        ExtraLiabilityData = float(OSICData[3].strip())
        GlassCoverageData = float(OSICData[4].strip())
        LoanerData = float(OSICData[5].strip())
        HSTRateData = float(OSICData[6].strip())
        FeeForMonthlyPayData = float(OSICData[7].strip())

        if ExtraLiability == "Y".upper():
            ExtraLiability = ExtraLiabilityData
        elif ExtraLiability == "N".upper():
            ExtraLiability = 0
        elif GlassCoverage == "Y".upper():
            GlassCoverage = GlassCoverageData
        elif GlassCoverage == "N".upper():
            GlassCoverage = 0
        elif Loaner == "Y".upper():
            Loaner = LoanerData
        elif Loaner == "N".upper():
            Loaner = 0
        else:
            break
    f.close()

    TotExtraCost = ExtraLiabilityData + GlassCoverageData + LoanerData
    TotInsurancePrem = BasicPremData + TotExtraCost
    HST = TotInsurancePrem * HSTRateData
    TotCost = TotInsurancePrem + HST
    MonthlyPay = FeeForMonthlyPayData + TotCost / 12

    # Formatting
    Date = datetime.date.today()
    DateDsp = "{}".format(Date.strftime("%d-%m-%Y"))

    # Receipt
    print()
    print("  ONE    STOP    INSURANCE    COMPANY")
    print("             RECEIPT")
    print("=======================================")
    print("Date: {}".format(DateDsp))
    print("Policy #: {}".format(PolicyNumData))
    print("Customer Name: {} {}".format(CustFirstName, CustLastName))
    print("Address: {}, {}, {}, {}".format(Address, City, Province, Postal))
    print("Phone: {}".format(PhoneNum))
    print("=======================================")
    print("Number of Cars Insured:               {}".format(NumCarsInsured))
    print("Extra Liability:                      {}".format(ExtraLiability.upper()))
    print("Glass Coverage:                       {}".format(GlassCoverage.upper()))
    print("Loan Car:                             {}".format(Loaner.upper()))
    print("Pay in Full or Monthly:               {}".format(FullOrMonthly.upper()))
    print("=======================================")
    print("Premium:                        ${:,.2f}".format(BasicPremData))
    print("Discount Additional Cars:         %{:,.2f}".format(DisAddCarsData))
    print("Extra Liability Cost:           ${:,.2f}".format(ExtraLiabilityData))
    print("Glass Coverage Cost:             ${:,.2f}".format(GlassCoverageData))
    print("Loan Cost:                       ${:,.2f}".format(LoanerData))
    print("Total Extra Cost:               ${:,.2f}".format(TotExtraCost))
    print("Total Insurance Premium:      ${:,.2f}".format(TotInsurancePrem))
    print("HST:                            ${:,.2f}".format(HST))
    print("Total Cost:                   ${:,.2f}".format(TotCost))
    print("Monthly Pay:                    ${:,.2f}".format(MonthlyPay))
    print("=======================================")
    print("Thanks for using One Stop Insurance!")
    print()

    # Writing to Policies File
    f = open("Policies.dat", "a")
    f.write(str("{}\n,".format(PolicyNumData)))
    f.write(str("{}\n,".format(CustFirstName)))
    f.write(str("{}\n,".format(CustLastName)))
    f.write(str("{}\n,".format(Address)))
    f.write(str("{}\n,".format(City)))
    f.write(str("{}\n,".format(Province)))
    f.write(str("{}\n,".format(Postal)))
    f.write(str("{}\n,".format(PhoneNum)))
    f.write(str("{}\n,".format(NumCarsInsured)))
    f.write(str("{}\n,".format(ExtraLiability)))
    f.write(str("{}\n,".format(GlassCoverage)))
    f.write(str("{}\n,".format(Loaner)))
    f.write(str("{}\n,".format(FullOrMonthly)))
    f.write(str("{}\n".format(TotCost)))
    print()
    print("Policies File is Updated!")
    print()

    PolicyNumData += 1
    while True:
        PolicyNumData = input("Would you like to enter another policy? (Y or N): ").upper()
        if PolicyNumData == "Y" or PolicyNumData == "N":
            break
    PolicyNumData = "N"
    if PolicyNumData == "Y":
        continue
    else:
        break

f = open("OSICDef.dat", "w")
f.write("{}\n".format(str(PolicyNumData)))
f.write("{}\n".format(str(BasicPremData)))
f.write("{}\n".format(str(DisAddCarsData)))
f.write("{}\n".format(str(ExtraLiabilityData)))
f.write("{}\n".format(str(GlassCoverageData)))
f.write("{}\n".format(str(LoanerData)))
f.write("{}\n".format(str(HSTRateData)))
f.write("{}\n".format(str(FeeForMonthlyPayData)))
f.close()
    # Detailed Report
    # print("ONE STOP INSURANCE COMPANY")
    # print("POLICY LISTING AS OF {}".format(DateDsp))







