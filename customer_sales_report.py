import csv

def main():
    try:
        # Using 'utf-8-sig' handles hidden BOM characters
        with open('sales.csv', 'r', encoding='utf-8-sig') as infile, \
             open('salesreport.csv', 'w', newline='') as outfile:
            
            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)
            
            writer.writerow(['Customer ID', 'Total'])
            
            sales_totals = {}
            
            for row in reader:
                # Use .get() or strip() to be extra safe with header names
                cust_id = row['CustomerID']
                
                # Calculate total: SubTotal + TaxAmt + Freight
                total_amt = float(row['SubTotal']) + float(row['TaxAmt']) + float(row['Freight'])
                
                # Aggregate the data
                if cust_id in sales_totals:
                    sales_totals[cust_id] += total_amt
                else:
                    sales_totals[cust_id] = total_amt
            
            # Write the aggregated results to the new file
            for cust_id, total in sales_totals.items():
                writer.writerow([cust_id, f"{total:.2f}"])
                
        print("Success! salesreport.csv has been created.")

    except KeyError as e:
        print(f"Error: Could not find column {e}")
        # This will show you exactly what Python is seeing for column names
        with open('sales.csv', 'r', encoding='utf-8-sig') as f:
            print("Actual columns found:", f.readline().split(','))

if __name__ == "__main__":
    main()