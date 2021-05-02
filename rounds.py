def bracket_formula(entries: int, rounds):
    """
    Sorts the entries into brackets
    
    Input:
        - entries: the amount of entries
        - rounds_int: the amount of rounds wanted
        
    Output: List of lists of brackets
    """
    # Initializes list of brackets
    brackets = []
    for i in range(rounds):
        brackets.append([])

    # Initializes counters and bool
    i = 0
    bracket_index = 0
    count_up = True
    
    while i < entries:
        i += 1
        # Counting up
        if count_up == True:
            # Access bracket
            current_bracket = brackets[bracket_index]           
            # Append new entry to current bracket
            current_bracket.append(i)      
            # Replace edited current bracket
            brackets[bracket_index] = current_bracket
            # Checks to see if counting down needs to start
            if bracket_index == rounds - 1:
                count_up = False
            bracket_index += 1
        elif count_up == False:
            # Subtract one from counting down
            bracket_index -= 1 
            # Access bracket
            current_bracket = brackets[bracket_index]
            # Appens entry
            current_bracket.append(i)
            # Replace edited current bracket
            brackets[bracket_index] = current_bracket
            # Checks to see if counting down is needed
            if bracket_index == 0:
                count_up = True
    return brackets