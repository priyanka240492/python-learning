# Clean emp names by providing space in between first and last names
import pandas as pd

data = {'emp_id': [101, 102, 103, 104],
        'emp_name': ['JohnDoe', 'JaneSmith', 'AliceJohnson', 'BobBrown'],
        'submitted_project': [True, False, True, False]}
df = pd.DataFrame(data)

def split_emp_name(**kwargs):
    """
    Splits concatenated employee names into first and last names by inserting a space
    
    **Kwargs: name (string) and submitted_project (string) are passed as keyword arguments
    
    Returns: None

    """
    name = kwargs.get('name') # kwargs.get or kwargs['name'] both work
    submitted_project = kwargs['submitted_project']
    # Find the position where the last name starts (first uppercase letter after the first character)
    for i in range(1, len(name)):
        if name[i].isupper():
            first_name = name[:i]
            last_name = name[i:]
            cleaned_name = first_name + ' ' + last_name
            print(f"Cleaned Name: {cleaned_name}, Submitted Project: {submitted_project}")
            return
    # If no uppercase letter found, return the original name
    print(f"Cleaned Name: {name}, Submitted Project: {submitted_project}")

print(split_emp_name.__doc__) # Calls function docstring

# Apply the function and print the cleaned names with project submission status
for _, row in df.iterrows(): 
        split_emp_name(name=row['emp_name'], submitted_project=row['submitted_project'])

# Keynote: Use df.itertuples() to improve performance in medium/large datasets
for row in df.itertuples(index=False): 
        split_emp_name(name=row.emp_name, submitted_project=row.submitted_project)



