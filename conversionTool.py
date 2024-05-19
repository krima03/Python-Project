class ConversionTool:

    def convert_grams_to_cups(grams):
	# Converts given measurement in grams to cups
        return grams * (1/128)
    
    def convert_dryOunces_to_cups(ounces):
	# Converts given measurement in dry ounces to cups
        return ounces * (1/4.5)
    
    def convert_fluidOunces_to_cups(ounces):
	# Converts given measurement in fluid ounces to cups
        return ounces * (1/8)
    
    def converter():
          while True:
            print("Conversion Tool")
            print("1: Grams to Cups")
            print("2: Dry Ounces to Cups")
            print("3: Fluid Ounces to Cups")
            print("4: Exit")
            choice = input("Choose an option: ")
    
                # Exits while loop if user chooses to exit
            if choice == '4':
                  print("Exiting the program.")
                  break
                
            # saves user input of cups as a variable
            measurement = float(input("Enter the number of your chosen unit of measure: "))
    
            if choice == '1':  # Convert cups to tablespoons
                result = ConversionTool.convert_grams_to_cups(measurement)
                print(str(measurement) + " grams is " + str(result) + " cups.")
            elif choice == '2':  # Convert cups to teaspoons
                result = ConversionTool.convert_dryOunces_to_cups(measurement)
                print(str(measurement) + " dry ounces is " + str(result) + " cups.")
            elif choice == '3':  # Convert ounces to cups
                result = ConversionTool.convert_fluidOunces_to_cups(measurement)
                print(str(measurement) + " fluid ounces is " + str(result) + " cups.")
            else:
                print("Invalid choice, please try again.")
    
    
ConversionTool.converter()
