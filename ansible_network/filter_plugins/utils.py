from ansible import errors

def convert_to_role_var(ints):
    to_return = {}
    listed_return = []
    for item in enumerate(ints):
        for name in item[1]['name'].split(','):
            try:
                to_return[item[0]].append({'name': str(name).strip()})
            except KeyError:
                to_return[item[0]] = []
                to_return[item[0]].append({'name': str(name).strip()})
        for k,v in item[1].iteritems():
            if k == 'name':
                continue
            else:
                for entry in to_return[item[0]]:
                    entry[k] = v 
    for ik, iv in to_return.iteritems():
        for i in iv:
           listed_return.append(i)
    return listed_return
               
   

class FilterModule(object):
    def filters(self):
        return {
            'convert_to_role_var': convert_to_role_var,
    }
