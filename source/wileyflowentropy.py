import csv
import flowratio as fr

flowEntropy = fr.computeEntropy(bad=1, good=10, batchSize=1, cycles=10, imps=0.055, energy=0.65, fixedFlow=True, energyMax=1)
# for key, value in flowEntropy.items():
#    print(f"Key: {key}")
#   print(value)  # Assuming each record is a single value or a string representation

# Specify the CSV file path
csv_file = 'results.csv'

# Write the results to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Cycle', 'flow', 'imps', 'need', 'energy'])

    # Write the data rows
    for key, value in flowEntropy.items():
        if key != 'ratio':
            row = [key, value['flow'], value['imps'],
                   value['need'], value['energy']]
            writer.writerow(row)

print(f"CSV file '{csv_file}' created successfully.")
