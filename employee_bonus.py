import csv

def main():
    try:
        # Using 'utf-8-sig' to handle hidden Windows formatting
        with open('employee_data.csv', 'r', encoding='utf-8-sig') as infile:
            reader = csv.DictReader(infile)
            
            for row in reader:
                # Grab the data from the CSV
                name = row.get('Name', 'Unknown')
                salary = float(row.get('Salary', 0))
                bonus_rate = float(row.get('Bonus', 0))
                
                # Calculate the values
                bonus_amt = salary * bonus_rate
                total_pay = salary + bonus_amt
                
                # Print in the vertical block format
                print(f"Name:   {name}")
                print(f"Salary: $ {salary:>10,.2f}")
                print(f"Bonus:  $ {bonus_amt:>10,.2f}")
                print(f"Pay:    $ {total_pay:>10,.2f}")
                print() # This adds the empty line between employees

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()