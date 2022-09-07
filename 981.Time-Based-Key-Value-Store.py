# Design a time-based key-value data structure that can store multiple values 
# for the same key at different time stamps and retrieve the key's value at a 
# certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with 
# the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called 
# previously, with timestamp_prev <= timestamp. If there are multiple such values, 
# it returns the value associated with the largest timestamp_prev. If there are no 
# values, it returns "".

# class TimeMap:

#     def __init__(self):
#         self.object = {}
        
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key in self.object:
#             self.object[key][timestamp] = value
#         else:
#             self.object[key] = {timestamp: value}
        

#     def get(self, key: str, timestamp: int) -> str:
#         timestamps = list(self.object[key].keys())
#         if timestamp in timestamps:
#             return self.object[key][timestamp]
#         else:
#             timestamps.append(timestamp)
#             timestamps.sort() 
#             index = timestamps.index(timestamp) - 1
#             if index >= 0:
#                 newTime = timestamps[index]
#                 return self.object[key][newTime]   
#             else:
#                 return ""


class TimeMap:

    def __init__(self):
        self.store = {} 
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res 