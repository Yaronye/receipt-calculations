if __name__ == '__main__':
    ronyasum = 0
    sofiasum = 0
    ebbasum = 0
    susansum = 0
    x = True

    while x:
        userInput = input("Who paid for the receipt? 1: Ronya, 2: Sofia, 3: Susan, 4: Ebba. Type 9 if you want "
                          "to move on to the next step." + '\n')
        if userInput != str(9):
            tempSum = input("What's the sum of the receipt?" + '\n')
            if userInput == str(1):
                ronyasum += float(tempSum)
            elif userInput == str(2):
                sofiasum += float(tempSum)
            elif userInput == str(3):
                susansum += float(tempSum)
            elif userInput == str(4):
                ebbasum += float(tempSum)
            else:
                print("Incorrect input")
            print(tempSum + " added to their sum.")
            print("\nCurrent sum for Ronya: " + str(ronyasum) + " Sofia: " + str(sofiasum) + " Susan: " + str(susansum) +
                  " Ebba: " + str(ebbasum) + "\n")
        else:
            x = False

    totalsum = ronyasum + sofiasum + ebbasum + susansum
    partSum = totalsum/4
    print("The total sum spent this month is " + str(totalsum) + "kr." + '\n' + "Ronya sum: " + str(ronyasum) + ' kr\n'
          + "Sofia sum: " + str(sofiasum) + ' kr\n' + "Susan sum: " + str(susansum) + ' kr\n' + "Ebba sum: " + str(ebbasum))

    partRonya = ronyasum - partSum
    partSofia = sofiasum - partSum
    partSusan = susansum - partSum
    partEbba = ebbasum - partSum

    print("The amount spent on average per person: " + str(partSum))
    if partRonya < 0:
        print('\n' + "Ronya is in debt with " + str((-1 * partRonya)) + " kr")
    else:
        print("Ronya is missing " + str(partRonya) + " kr")

    if partSofia < 0:
        print("Sofia is in debt with " + str((-1 * partSofia)) + " kr")
    else:
        print("Sofia is missing " + str(partSofia) + " kr")

    if partSusan < 0:
        print("Susan is in debt with " + str((-1 * partSusan)) + " kr")
    else:
        print("Susan is missing " + str(partSusan) + " kr")

    if partEbba < 0:
        print("Ebba is in debt with " + str((-1 * partEbba)) + " kr")
    else:
        print("Ebba is missing " + str(partEbba) + " kr")



