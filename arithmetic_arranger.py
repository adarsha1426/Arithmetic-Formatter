def arithmetic_arranger(problems, solver = False):
    numerator = ""
    denomenator = ""
    hiphens = ""
    solution_number =  ""
    end_result = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        first_number = ""
        operator = ""
        second_number = ""
        first_number = problem.split()[0]
        operator = problem.split()[1]
        second_number = problem.split()[2]
    
        if first_number.isdigit() and second_number.isdigit():
            if len(first_number) > 4 or len(second_number) > 4:
              return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Numbers must only contain digits."
        solution = ""
        if operator == "+":
            solution = str(int(first_number) + int(second_number))
        elif operator == "-":
            solution = str(int(first_number) - int(second_number))
        else:
            return "Error: Operator must be '+' or '-'."
        distance = max(len(first_number), len(second_number)) + 2
        if problem != problems[-1]:
            numerator =numerator + str(first_number.rjust(distance)) + "    "
            denomenator = denomenator + operator + str(second_number.rjust(distance - 1)) + "    "
            hiphens= hiphens + "-" * (distance) + "    "
            solution_number = solution_number + solution.rjust(distance) + "    "
        else:
            numerator = numerator + str(first_number.rjust(distance))
            denomenator =denomenator + operator + str(second_number.rjust(distance - 1))
            hiphens = hiphens + "-" * (distance)
            solution_number = solution_number + solution.rjust(distance)
    if solver:
        end_result =numerator + "\n" + denomenator + "\n" + hiphens + "\n" + solution_number
    else:
        end_result=numerator + "\n" + denomenator + "\n" + hiphens
    return end_result
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], ))