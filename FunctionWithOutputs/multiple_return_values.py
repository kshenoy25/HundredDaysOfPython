from FunctionWithOutputs.function_output_demo import format_name


def peoples_names(f_name, l_name):
    """
    This program contains a docstring
    """
    if f_name == "" or l_name == "":
        return("You did not provide valid inputs!")
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return(f"Result: {formated_f_name} {formated_l_name}")

print(peoples_names(input("What is your first name?"), input("What is your last name?")))