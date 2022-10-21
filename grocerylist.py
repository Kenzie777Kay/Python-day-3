def grocery_list():
    
    groc_list = [] 
     
    while True:  
        question = input('what would you like to do? add/remove/show/quit? : ') 
       
        if question.lower() == 'add':
            adding_list = input('what would you like to add? : ')
            groc_list.append(adding_list)

        elif question.lower() == 'remove':
            remove_list= input('What item would you like to remove? : ')
            groc_list.remove(remove_list)
        
        elif question.lower() == 'show':
            print(groc_list)
        
        elif question.lower() == 'quit':
            break 
        else:
            print('sorry that was not an option would you like to add/show/quit?: ')

grocery_list()