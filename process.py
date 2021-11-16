# # opens file
# log_file = open("um-server-01.txt")

# # defines sales_reports taking in the opened file as a parameter
# def sales_reports(log_file):
#     # reads in the input file one line at a time
#     for line in log_file:
#         # removes trailing whitespace from the line and returns a copy
#         line = line.rstrip()
#         # defines day as the indices from 0-3 in the line
#         day = line[0:3]
#         # if the values if the indices in day equal "Mon"
#         if day == "Mon":
#             # print the line from the original file to sales_reports 
#             print(line)

# # prints out the entries in the file that meet the criteria 
# sales_reports(log_file)
# log_file.close();

log_file = open('um-server-01.txt')

def sales_reports(log_file):
    for line in log_file:
            line = line.rstrip()
            line_list = line.split(' ')
            qty = int(line_list[2])
            if qty >=10:
                print(line)
sales_reports(log_file)
