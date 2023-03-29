def displaySummary(status, total, malePercent, femalePercent):
	print(f"Number of {status} = {total}")
	print(f"Male = {round(malePercent, 2)}%")
	print(f"Female = {round(femalePercent, 2)}%")
	print("\n")

numberOfNewlyHiredMales = int(input("Enter the number of newly hired males: "))
numberOfNewlyHiredFemales = int(input("Enter the number of newly hired females: "))
numberOfPermanentMales = int(input("Enter the number of permanent position males: "))
numberOfPermanentFemales = int(input("Enter the number of permanent position females: "))
numberOfResignedMales = int(input("Enter the number of permanent position males: "))
numberOfResignedFemales = int(input("Enter the number of permanent position females: "))

sumOfNewlyHired = numberOfNewlyHiredMales + numberOfNewlyHiredFemales
sumOfPermanent = numberOfPermanentMales + numberOfPermanentFemales
sumOfResigned = numberOfResignedMales + numberOfResignedFemales

percentMaleNewlyHired = (numberOfNewlyHiredMales / sumOfNewlyHired) * 100
percentFemaleNewlyHired = (numberOfNewlyHiredFemales / sumOfNewlyHired) * 100
percentMalePermanent = (numberOfPermanentMales / sumOfPermanent) * 100
percentFemalePermanent = (numberOfPermanentFemales / sumOfPermanent) * 100
percentMaleResigned = (numberOfResignedMales / sumOfResigned) * 100
percentFemaleResigned = (numberOfResignedFemales / sumOfResigned) * 100

print("\n")
print("===")
print("Thank you for the information")
print("===")
print("Here is the Summary !!!\n")

displaySummary("hired employee", sumOfNewlyHired, percentMaleNewlyHired, percentFemaleNewlyHired)
displaySummary("Permanent Employee", sumOfPermanent, percentMalePermanent, percentFemalePermanent)
displaySummary("Resigned Employee", sumOfResigned, percentMaleResigned, percentFemaleResigned)



