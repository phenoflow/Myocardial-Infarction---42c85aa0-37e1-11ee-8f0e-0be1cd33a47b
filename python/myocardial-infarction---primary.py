# Nathaniel M Hawkins, Shaun Scholes, Madhavi Bajekal, Hande Love, Martin O'Flaherty, Rosalind Raine, Simon Capewell, 2023.

import sys, csv, re

codes = [{"code":"14A3.00","system":"readv2"},{"code":"14A4.00","system":"readv2"},{"code":"14AH.00","system":"readv2"},{"code":"G305.00","system":"readv2"},{"code":"4109H","system":"oxmis"},{"code":"4119N","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('myocardial-infarction-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["myocardial-infarction---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["myocardial-infarction---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["myocardial-infarction---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
