def filter_assignment_priority(class_value):
    priority_group=['Critical','High','Moderate','Low','Planning']
    value=priority_group[int(class_value)]
    return value