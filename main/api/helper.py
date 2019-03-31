from django.forms.models import model_to_dict

def parse_exception(exception):
    return exception.__str__().replace('"','').replace('(','').replace(')','').split(',')

def rename_dict(prefix, old_dict):
    new_dict = {}
    for key in old_dict:
        new_dict[prefix+key] = old_dict[key]
    
    return new_dict

def get_required_dict(required_column, old_dict):
    new_dict = {}
    for key in required_column:
        if(key in old_dict):
            new_dict[key] = old_dict[key]

    return new_dict

def model_list_to_list_of_dict(model_list):
    list_of_dict = [model_to_dict(model) for model in model_list]
    return list_of_dict

def get_sort_parameter(field, direction):
    if direction == 'asc':
        direction = ''
    else :
        direction = '-'

    return direction + field

def get_entry_range_from_page(page_num, entry_num):
    page_num = int(page_num)
    entry_num = int(entry_num)
    start = (page_num-1) * entry_num
    end = start + entry_num

    return start, end