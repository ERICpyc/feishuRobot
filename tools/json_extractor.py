
def extract_element_from_json(obj, path):
    '''
    输入关键字，就可以将关键字的值信息存放在列表中并输出
    如果关键字是对象名，则返回的对象字典信息到列表中
    如果关键字是列表名，则返回的列表信息到列表中（返回双重列表）
    '''
    def extract(obj, path, ind, arr):
        '''
        从一个嵌套的字典中提取一个元素，并返回到列表中。
        params: obj - dict - 输入字典
        params: path - list - 构成JSON路径的字符串列表
        params: ind - int - 起始索引
        params: arr - 列表 - 输出列表
        '''
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr