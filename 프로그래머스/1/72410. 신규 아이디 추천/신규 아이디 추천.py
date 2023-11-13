import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', '', new_id)
    new_id = re.sub('[.]{2,}', '.', new_id)
    new_id = new_id.strip('.')
    if new_id == '':
        new_id += 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    if len(new_id) <= 2:
        ch = new_id[-1]
        while len(new_id) != 3:
            new_id += ch
    
    return new_id