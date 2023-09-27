# This is how you package differnet files with functions and can import them to other scripts and files to use with your script.
# Say you create a fancy function that will help you in a scriot, you can save that function and then import it in another script.

# so here is the example function below

print('Imported my_module...')

test = 'Test String'

def find_index(to_search, taget):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == taget:
            return i
    return -1    
    