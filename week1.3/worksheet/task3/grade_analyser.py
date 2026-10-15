# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

# open the file

# read in the data, and for each student calculate their average grade and classification



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder

file_name = input("Enter the filename: ")


def classify(average):
    if average >= 70:
        return "1"
    elif average >= 60:
        return "2:1"
    elif average >= 50:
        return "2:2"
    elif average >= 40:
        return "3"
    else:
        return "F"


with open(file_name, 'r') as infile, open(file_name + "_out.csv", 'w') as outfile:
    next(infile)
    for line in infile:
        line = line.strip()
        if line == "":                      # skip any blank lines
            continue

        parts = line.split(',')
        student_id = parts[0]

        # keep only the non-empty grade fields, so the trailing ",,,," is ignored
        grades = [float(g) for g in parts[1:] if g.strip() != ""]

        average = sum(grades) / len(grades)
        classification = classify(average)

        outfile.write(f"{student_id},{average:.2f},{classification}\n")