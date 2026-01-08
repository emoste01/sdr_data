import csv

input_file = 'lc_frequency.csv'
output_file = 'LC_Local.TXT'

try:
    with open(input_file, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        with open(output_file, mode='w', encoding='utf-8') as txtfile:
            for row in reader:
                raw_freq = row.get('Frequency')
                desc = row.get('Description')
                
                if raw_freq and desc:
                    try:
                        # Convert MHz to Hz (multiply by 1,000,000)
                        # We use float() first to handle decimals like 173.8
                        freq_hz = int(float(raw_freq) * 1_000_000)
                        
                        # Prepend tags and write to file
                        line = f"f={freq_hz},d={desc}\n"
                        txtfile.write(line)
                    except ValueError:
                        print(f"Skipping row with invalid frequency: {raw_freq}")
                        
    print(f"Successfully created {output_file} with frequencies in Hertz.")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' was not found.")

