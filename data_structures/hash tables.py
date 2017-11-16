import data_structures.profiler as profiler

# Imagine that Python did not include a dictionary data structure (e.g. phoneNumbers['John Smith'] = 0123456789)
# How would we create one?


# This class merely stores two pieces of information together - the key and value used in a dictionary
# eg if dictionary is being used as a phone book, the key might be 0123456789 and the value might be "John"
# The key and value can be of any variable type, eg integer, float, string etc - even a reference to an object
class key_and_value:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# Simple (bad) way - just store all entries in a list, adding them in linear order
# Very inefficient as each time we add or get an entry, we have to search through
# every item in order. Time complexity is O(n)

bad_dictionary_list = []

def bad_dictionary_set(key, value):
    # First, does the key already exist in the list?
    for i in range(0,len(bad_dictionary_list)):
        if bad_dictionary_list[i].key == key:
            # Key already exists, replace its value with the new one
            bad_dictionary_list[i].value = value
            return

    # Not found, add new entry
    bad_dictionary_list.append( key_and_value(key, value))

def bad_dictionary_get(key):
    for i in range(0,len(bad_dictionary_list)):
        if bad_dictionary_list[i].key == key:
            return bad_dictionary_list[i].value

def test_bad_dictionary():
    bad_dictionary_set('Susan Smith', 12345)
    bad_dictionary_set('John Jones', 98765)
    bad_dictionary_set('Harry Hill', 6574583)

    print(bad_dictionary_get('John Jones'))
    print(bad_dictionary_get('Harry Hill'))
    print(bad_dictionary_get('Susan Smith'))



# Good way - use a hash table

class GoodDictionary:
    def __init__(self, hash_function, num_buckets=10000):
        self.hash_function = hash_function
        self.num_buckets = num_buckets
        self.hashtable_list = []
        for i in range(0,num_buckets):
            self.hashtable_list.append( [] )

    @staticmethod
    def get_string_hash(key):
        # This is a very simple hashing function, it's probably not a particularly good one.
        # It only works when the key is a string.
        index = 0
        i = 1
        for c in key:
            index += ord(c) * i # ord converts character to ascii/unicode code
            i+=1

        return index

    def set(self, key, value):
        index = self.hash_function(key) % self.num_buckets # use mod to restrict index to valid list indicies
        bucket = self.hashtable_list[index]

        # Does the key already exist in the list?
        for i in range(0, len(bucket)):
            if bucket[i].key == key:
                bucket[i].value = value
                return

        # Otherwise, add to bucket
        bucket.append(key_and_value(key, value))

    def get(self, key):
        index = self.hash_function(key) % self.num_buckets
        bucket = self.hashtable_list[index]

        for i in range(0, len(bucket)):
            if bucket[i].key == key:
                return bucket[i].value

        return None

    @staticmethod
    def test_good_dictionary():
        test_dictionary = GoodDictionary( GoodDictionary.get_string_hash )
        test_dictionary.set('Susan Smith', 12345)
        test_dictionary.set('John Jones', 98765)
        test_dictionary.set('Harry Hill', 6574583)
        test_dictionary.set('sdgg', 0)
        test_dictionary.set('gfjfgj', 1)
        test_dictionary.set('fghjfg', 2)
        test_dictionary.set('mnvv', 3)
        test_dictionary.set('hgfdh', 4)
        test_dictionary.set('hgdhdf', 5)

        print(test_dictionary.get('John Jones'))
        print(test_dictionary.get('Harry Hill'))
        print(test_dictionary.get('Susan Smith'))

        test_dictionary.print_hashtable()

    def print_hashtable(self):
        # print the actual contents of the hash table so we can see how the buckets have been used
        for bucket in self.hashtable_list:
            output_string = "["
            for i in range(0,len(bucket)):
                output_string += str(bucket[i].key) + ":" + str(bucket[i].value)
                if i < len(bucket) - 1:
                    output_string += ","
            output_string += "]"
            print(output_string)

    def get_bucket_usage_percent(self):
        buckets_used = sum(len(item) > 0 for item in self.hashtable_list)
        return buckets_used / self.num_buckets


def profile_bad_dictionary(num_items):
    p = profiler.Profiler()
    for i in range(0,num_items):
        bad_dictionary_set(str(i), 0)
    return p.get_seconds()

def profile_good_dictionary(num_items, hash_function, num_buckets=10000):
    test_dictionary = GoodDictionary(hash_function, num_buckets)
    p = profiler.Profiler()
    for i in range(0,num_items):
        test_dictionary.set(str(i), 0)
    return p.get_seconds(), test_dictionary.get_bucket_usage_percent()


column_headings = "{:<5} {:<10}  {}".format("Items", "Seconds", "Buckets used")
column_headings_without_buckets = "{:<5} {:<10}".format("Items", "Seconds")

format_string = "{:<5} {:<10}  {:.3%}"
format_string_without_buckets = "{:<5} {:<10}"

max_items = 2 ** 13


print("Profiling bad dictionary (just stored as a list of key-value pairs)")
print(column_headings_without_buckets)
i = 1
while i <= max_items:
    time = profile_bad_dictionary(i)
    print(format_string_without_buckets.format(i, time))
    i *= 2


print("Profiling good dictionary (10,000 buckets, bad hash function)")
print(column_headings)
i = 1
while i <= max_items:
    time, percent_buckets_used  = profile_good_dictionary(i, GoodDictionary.get_string_hash, 10000)
    print(format_string.format(i, time, percent_buckets_used))
    i *= 2

print("Profiling good dictionary (10,000 buckets, built-in Python hash function)")
print(column_headings)
i = 1
while i <= max_items:
    time, percent_buckets_used = profile_good_dictionary(i, hash, 10000)  # better hashing function (Python built-in function)
    print(format_string.format(i, time, percent_buckets_used))
    i *= 2
