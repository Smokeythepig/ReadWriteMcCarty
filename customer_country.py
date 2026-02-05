import csv

def main():
    # Open the source and the destination files
    with open('customers.csv', 'r') as infile, open('customer_country.csv', 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header for the new file
        writer.writerow(['Full Name', 'Country'])
        
        # Skip the header of the source file
        next(reader)
        
        count = 0
        for row in reader:
            # Assuming First Name is index 1, Last Name is index 2, Country is index 4
            # Adjust indices based on your specific CSV structure
            full_name = f"{row[1]} {row[2]}"
            country = row[4]
            writer.writerow([full_name, country])
            count += 1
            
    print(f"Total number of customers: {count}")

if __name__ == "__main__":
    main()