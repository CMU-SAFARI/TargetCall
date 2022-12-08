import sys
import os

data_dir = sys.argv[1]

viral_list = ['AC_000007.1' ,'NC_001526.4', 'NC_001731.1' ,'NC_009334.1', 'NC_045512.2' ,'NC_055231.1', 'NC_063383.1']
list_final = []
list_final = viral_list

# Calculate the counts in the full dataset
print('default')
abundances_dir = data_dir + use_case + '/default/filtered-sam/'
for element in list_final:
    print(element)
    os.system('cat ' + abundances_dir + '* | cut -f1-3 | grep '+ element + ' | cut -f1 | grep -v "LN:" | grep -v "PN:" |  sort -u | wc -l')

models = ["TINYX0111", "TINYX011", "TINYX01", "TINYX2", "TINYX3"]

print('model')
# Calculate the counts in the filtered dataset
for model in models:
    print(model)
    abundances_dir = data_dir + use_case + '/' + model + '/filtered-sam/'
    for element in list_final:
        print(element)
        os.system('cat ' + abundances_dir + '* | cut -f1-3 | grep '+ element + ' | cut -f1 | grep -v "LN:" | grep -v "PN:" |  sort -u | wc -l')

