# I started by adapting from example on page 362 the of book "Cambridge International AS & A-level Computer Science" (Langfield & Dudell)
# However, the code from the book is so wrong that the code below bears almost no resemblance to the original
# It is far from complete as it doesn't deal with collisions
# Requires Python 3.6

# I don't think this approach is widely used these days. It would have been used more in the 70s and 80s when it was
# not possible to load large files entirely into RAM.

# Python has a module called shelve which achieves similar results, i.e. reading/writing data based on a key,
# just like working with a dictionary. However, shelve has the same serious security issues as the 'pickle' - see
# 'CIE sequential file.py' for info about that

import struct
import hashlib

class CarRecord:
    registration_size = 8
    record_size = 12
    string_encoding = 'utf-8'

    def __init__(self, registration, engine_size):
        self.registration = registration    # using this as key field
        self.engine_size = engine_size

        if len(self.registration) > CarRecord.registration_size:
            raise Exception

    def __str__(self):
        return f'{self.registration}     {self.engine_size}'     # f-strings require Python 3.6

    def serialize(self):
        if len(self.registration) > CarRecord.registration_size:
            raise Exception

        reg_encoded = bytes(f'{self.registration:8}', CarRecord.string_encoding)
        return struct.pack('8si', reg_encoded, self.engine_size)

    def deserialize(byte_data):
        data = struct.unpack("8si", byte_data)
        reg = data[0].decode(CarRecord.string_encoding)
        engine = data[1]
        return CarRecord(reg, engine)

    def __hash__(self):
        # I originally used Python's built-in hash but it returns different results on each run of the program
        # for security reasons - see https://stackoverflow.com/questions/27522626/hash-function-in-python-3-3-returns-different-results-between-sessions
        reg_utf8 = self.registration.encode(CarRecord.string_encoding)
        return int(hashlib.sha256(reg_utf8).hexdigest(), 16)

    def __eq__(self, other):
        return self.registration == other.registration and self.engine_size == other.engine_size


filename = 'cars_random.dat'
file_size = 2**10   # 1KiB
num_slots = file_size // CarRecord.record_size


def create_empty_file():
    print(f"Generating empty file of size: {file_size} bytes")
    car_file = open(filename, 'wb')  # open file for binary write
    car_file.write(bytearray(file_size))
    car_file.close()

def write_to_file(data):
    if len(data) == 0:
        return

    print(f"Begin writing - file size: {file_size}, record length {CarRecord.record_size}, num_slots: {num_slots}")

    with open (filename, 'rb+') as car_file:    # open file for binary read and write
        for car in data:
            slot = hash(car) % num_slots
            address = slot * CarRecord.record_size

            serialized = car.serialize()
            assert (len(serialized) == CarRecord.record_size)

            print(f'Writing record to slot {slot}, address {address}')
            car_file.seek(address)
            # TO DO: check for existing record and collision
            car_file.write(serialized)

def verify_file(data):
    with open (filename,'rb') as car_file: # open file for binary read
        for car in data:
            slot = hash(car) % num_slots
            address = slot * CarRecord.record_size
            car_file.seek(address)
            file_data = car_file.read(CarRecord.record_size)
            file_car = CarRecord.deserialize(file_data)
            print(f"Loaded: {file_car}, equal?: {car == file_car}")

    # file is closed automatically as we opened it using 'with'
    return data

###################

cars = [ CarRecord("HU17 IOP", 1400), CarRecord("NH52 EQM", 2000), CarRecord("IK08 DAK", 1000) ]

create_empty_file()
write_to_file(cars)
verify_file(cars)
