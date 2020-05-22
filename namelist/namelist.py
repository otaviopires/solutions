def namelist(names):
    names_list = []
    for name in names:
        names_list.append(name['name'])
    if len(names_list) > 1:
        return(', '.join(names_list[:-1]) + ' & ' + str(names_list[-1]))
    elif len(names_list) == 1:
        return(names_list[0])
    else:
        return('')
    
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ]))
print(namelist([ {'name': 'Bart'} ]))
print(namelist([]))