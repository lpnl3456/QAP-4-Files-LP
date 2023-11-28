# A program to allow One Stop Insurance Company to calculate new nsurance policy information for its customers
# Written on Nov 17, 2021
# Auther: Luke Peddle

# Import libraries
import datetime
import random
import FormatValues as FV  
# Set constents

POLCY_NUM = 1944
BASIC_PRE_RATE = 869.00
ADD_CAR_DIS_RATE = 0.25
EXTRA_LIABILITY_RATE = 130.00
GLASS_COV_RATE = 86.00
LOANER_CAR_RATE = 58.00
HST_RATE = 0.15
PROCESSING_FEE_RATE = 39.99

def validString (string):
    # A funcation to validate strings

    if string == "":
        valid = False
        print("Input cannot be blank - Please re-enter")
        print()
    else:
        valid = True
    return valid
    
def validOption(option):
    # A function to validate inputs for extra costs
    valid= True
    if option == "":
         print("Input cannot be blank - Please re-enter")
         print()
         valid = False

    if option != "Y" and option != "N" :
        print("The input must be either a Y or a N - Please re-enter")
        print()
        valid = False

    return valid
    




# Main Program

ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
paymentList = ["Full","Monthly", "Down Pay"]



while True:
    dateOfClaim =[] 
    costOfClaim = []

    # Have the user input the values 

    while True:
        custFirstName  = input("Enter the customer's first name: ").title()
        valid = validString(custFirstName)
        
        if valid == True:
            print()
            break

    while True:
        custLastName = input("Enter the customer's last name: ").title()
        valid = validString(custLastName)
        
        if valid == True:
            print()
            break

    while True: 
        stAdd = input("Enter the customer's street Address: ")
        valid = validString(stAdd)
        
        if valid == True:
            print()
            break

    while True:
        city = input("Enter the customer's city: ").title()
        valid = validString(city)
        
        if valid == True:
            print()
            break
    while True:
        prov = input("Enter the customer's province(XX): ").upper()
        valid = validString(prov)
        
        if valid == True:
            if len(prov) != 2:
                print("Province is a 2 digit code - please re-enter.")
                print()
            elif prov not in ProvLst:
                print("Not a valid province - please re-enter.")
                print()
            else:
                print()
                break
                
    while True: 
        postCode = input("Enter the customer's postal code (X#X#X#): ").upper()
        valid = validString(postCode)
        
        if valid == True:
            if postCode[0].isalpha() == False or  postCode[2].isalpha() == False or  postCode[4].isalpha() == False :
                print("Postal code must contian a letter at postion 1, 3, and 5 - Please re-enter")
                print()
            elif postCode[1].isdigit() == False or  postCode[3].isdigit() == False or  postCode[5].isdigit() == False :
                print("Postal code must contian a number at postion 2, 4, and 6 - Please re-enter")
                print()
            else:
                print()    
                break
            
    while True:
        phoneNum = input("Enter the customer's phone number (##########): ")
        
        valid = validString(phoneNum)
        
        if valid == True:
            if phoneNum.isdigit() == False :
                print("Phone number must contian only numbers - Please re-enter")
                print()
            elif len(phoneNum) != 10:
                print("Phone number must contain only ten number - Please re-enter")
                print()
            else:
                print()
                break
    while True:          
        try:
            totCarInsured = int(input("Enter the amount of cars insured: "))
        except:
            print("Input must be a full number - Please re-enter")
            print()
        else:
            print()
            break

    while True:
        extraLiab = input("Enter if the customer has extra liability(Y or N): ").upper()
        
        valid = validOption(extraLiab)
        
        if valid == True:
            print()
            break

    while True:
        opGlassCover = input("Enter if the customer has glass coverage(Y or N): ").upper()
        
        valid = validOption(opGlassCover)
        
        if valid == True:
            print()
            break
    
    while True:
        opLoanCar = input("Enter if the customer has a loaner car(Y or N): ").upper()
        
        valid = validOption(opLoanCar)
        
        if valid == True:
            print()
            break
        
    while True:
        payMeth = input("Enter the customer payment method(Full or Monthly or Down Pay): ").title()
        
        valid = validString(payMeth)
        
        if valid == True:
            if payMeth not in paymentList:
                print("Not a valid payment method - please re-enter.")
                print()
            else:
                print()
                break

    if payMeth == "Down Pay":
        while True: 
            try:
                downPayAmount = float(input("Enter the amount of the down payment: "))
            except:
                print("The down payment must be a number - Please re-enter")
                print()
            else:
                break
    else:
        downPayAmount = 0.00
    
    while True:
        while True:
            claimDate = str(input("Enter the date of the previous claim (YYYY-MM-dd): "))
            try:
                test = datetime.datetime.strptime(claimDate, "%Y-%M-%d")
            
            except:
                print("Invalid date format - Please re-enter")
                print()
            else:
                print()
                break 

        dateOfClaim.append(claimDate)

        while True:
            
                try:
                    claimCost = float(input('Enter the prevoius claim cost: '))
                
                except:
                    print("The claim cost must be a number - Please re-enter")
                    print()
                else:
                    claimCost = FV.FDollar2(claimCost)
                    print()
                    break 
        
        costOfClaim.append(claimCost)

        while True:
                AddClaim = input("Do you want to add another previous claim of the costomer(Y or N): ").upper()

                valid = validString(AddClaim)

                if valid == True:
                    if AddClaim != "Y" and AddClaim != "N":
                        print("Input must be either Y or N - Please re-enter")
                        print()
                    else:
                        print()
                        break
                
        if AddClaim == "N":
                print()
                break

    

    # Calculations
    basInPre = BASIC_PRE_RATE 
    addInPre = ((totCarInsured - 1)* BASIC_PRE_RATE)/ (1 + ADD_CAR_DIS_RATE)
    inPre = basInPre + addInPre

    exLiabCost = 0
    if extraLiab == "Y":
        exLiabCost = EXTRA_LIABILITY_RATE

    glassCovCost = 0
    if opGlassCover == "Y":
        glassCovCost = GLASS_COV_RATE


    loanerCost = 0
    if opLoanCar == "Y":
        loanerCost = LOANER_CAR_RATE

    totExCost = exLiabCost + glassCovCost + loanerCost

    totInsurPre = inPre + totExCost

    hstAmount = totInsurPre *HST_RATE

    totCost = totInsurPre + hstAmount

    if payMeth == "Full":
        downPayAmount = totCost

    monPay = (totCost + PROCESSING_FEE_RATE - downPayAmount )/8

    # Print recipt 

    print()
    print(f"One Stop Insurance Company Insurance policy")
    print()
    print(f"Policy Number:                         Amount of cars insured:               {totCarInsured:>3d}")
    basInPreDsp = FV.FDollar2(basInPre)
    print(f"     {POLCY_NUM:>4d}                              Basic insurance premiums:      {basInPreDsp:>10s}")
    addInPreDsp = FV.FDollar2(addInPre)
    print(f"                                       Addtional insurance premiums:  {addInPreDsp:>10s}")
    inPREDsp = FV.FDollar2(inPre)
    print(f"                                       Cost of insurance premiums:    {inPREDsp:>10s}")
    print(f"Sold to:                               -----------------------------------------")
    print(f"                                       Extra liability:                        {extraLiab:>1s}")
    fullname = FV.FName(custFirstName, custLastName)
    exLiabCostDsp = FV.FDollar2(exLiabCost)
    print(f"     {fullname:<15s}                   Extra liability cost:          {exLiabCostDsp:>10s}")
    print(f"     {stAdd:<15s}                   Glass Coverage:                         {opGlassCover:>1s}")
    glassCovCostDsp = FV.FDollar2(glassCovCost)
    fullAdd = city + ", " + prov + " " + postCode
    print(f"     {fullAdd:<15s}                 Glass coverage cost:           {glassCovCostDsp:>10s}")
    phoneNumDsp = FV.FPhone(phoneNum)
    print(f"     {phoneNumDsp:<12s}                      Loaner car:                             {opLoanCar:<1s}")
    loanerCostDsp = FV.FDollar2(loanerCost)
    print(f"                                       Loaner car cost:               {loanerCostDsp:>10s}")
    totExCostDsp = FV.FDollar2(totExCost)
    print(f"                                       Total extra cost:              {totExCostDsp:>10s}")
    print(f"                                      ------------------------------------------")

    totInsurPreDsp = FV.FDollar2(totInsurPre)
    print(f"                                       Total insurance premiums:      {totInsurPreDsp:>10s}")
    hstAmountDsp = FV.FDollar2(hstAmount)
    print(f"                                       HST:                           {hstAmountDsp:>10s}")
    totCostDsp = FV.FDollar2(totCost)
    print(f"                                       Total cost:                    {totCostDsp:>10s}")
    print(f"                                       ------------------------------------------")
    print(f"                                       Payment method:                   {payMeth:>8s}")
    PROCESSING_FEE_RATEDsp = FV.FDollar2(PROCESSING_FEE_RATE)
    print(f"                                       Processing fee:                 {PROCESSING_FEE_RATEDsp:>10s}")
    downPayAmountDsp = FV.FDollar2(downPayAmount)
    print(f"                                       Down payment amount:            {downPayAmountDsp:>10s}")
    monPayDSP = FV.FDollar2(monPay)
    print(f"                                       Monthly payment:                {monPayDSP:>10s}")
    print(f"                                       ------------------------------------------")
    invoiceDate = datetime.datetime.now()
    invoiceDateDsp = invoiceDate.strftime("%Y-%M-%d")
    print(f"                                       Invoice date:                   {invoiceDateDsp:>10s}")
    firstPaymentDate = invoiceDate + datetime.timedelta(days = 30)
    firstPaymentDateDsp = firstPaymentDate.strftime("%Y-%M-%d")
    print(f"                                       FirstPayment Date:              {firstPaymentDateDsp:>10s}")

    print()
    print(f"                                    Previous Claims")
    print(f"                       Claim #  Claim Date            Amount")
    print(f"                       -------------------------------------")
    

    for claim in range (len(costOfClaim)):
        claimDsp = claim+1
        print(f"                         {claimDsp:>2d}.    {dateOfClaim[claim]:<10}        {costOfClaim[claim]:>10s}")
    print(f"                       -------------------------------------")

    # Ask the user if they want to continue using the program
    while True:
        con = input("Do you want to continue using the program(Y or N): ").upper()

        valid = validString(con)
        if valid == True:
            if con != "Y" and con != "N":
                        print("Input must be either Y or N - Please re-enter")
                        print()
            else:
                break
                
    if con == "N":
        break

print()
print("Thank you for using the program.")



