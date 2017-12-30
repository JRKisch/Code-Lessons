def prompt_user(knob):
    return input( "what "+knob+" were you born\n")
    

birthYear=prompt_user("year")
birthMonth=prompt_user("month")
birthDay=prompt_user("day")
print("your birth date is " + birthYear + "/" + birthMonth + "/" + birthDay)

