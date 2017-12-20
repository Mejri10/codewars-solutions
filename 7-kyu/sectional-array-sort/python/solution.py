def sect_sort(array, start, length=0):
    interval = slice(start, start + length) if length else slice(start,None)
    return array[:start] + sorted(array[interval]) + array[start+length:]*(length>0)
   