# Evan McKague
# bloom_filter.py
# Description: This program is a way of determining if a data member (in this case passwords) falls in a given set 
#               using a quick and efficient method

import mmh3                             # third party hashing functioning
from math import ceil, log              # used for calculating bloom filter efficiency 
from bitarray import bitarray 
from datetime import datetime

class BloomFilter(object):
    def __init__(self, file_of_bad_passwords):
        self.file = self.get_file_size(file_of_bad_passwords)
        self.size_of_bit_array = self.get_bit_size()
        self.number_of_hash_functions = self.get_hash_functions()
        self.bit_arrary = bitarray(self.size_of_bit_array)
        self.bit_arrary.setall(0)

    def get_file_size(self, file_of_bad_passwords):
        size = len(open(file_of_bad_passwords).readlines())
        
        return size

    def get_bit_size(self):
        n = self.file                                       # number_of_bad_passwords 
        p = 0.00000010                                      # false_positive_probability
        
        m = ceil((n * log(p)) / log(1 / pow(2, log(2)))) 
        print("\nBit array size will be", m)
        print("False positive probability of {:.8f}".format(p))
        
        return m

    def get_hash_functions(self):
        n = self.file                                       # number_of_bad_passwords 
        k = round((self.size_of_bit_array/n) * log(2))      # hash_count 
        print(k, "hash function(s) will be used\n")
        
        return k

    def check_password(self, item):
        temp = True
        for i in range(self.number_of_hash_functions):
            index = mmh3.hash(item, i) % self.size_of_bit_array
            if self.bit_arrary[index] == 0:
                temp = False

        return temp

    def add_to_bloom(self, item):
        for i in range(self.number_of_hash_functions):
            index = mmh3.hash(item, i) % self.size_of_bit_array
            self.bit_arrary[index] = 1

        return self


def file_is_openable(file_name):
    try:
        open(file_name, "r")
        return True
    except IOError:
        print("Error file does not appear to exist")
        return False


while True:
    bad_passwords_file_name = input("Please enter the name of the file name with the bad passwords: ")
    if file_is_openable(bad_passwords_file_name):
        break

while True:
    possible_passwords_file_name = input("Please enter the name of the file with possible passwords: ")
    if file_is_openable(bad_passwords_file_name):
        break


# bad_passwords_file_name = "dictionary.txt"
# possible_passwords_file_name = "sample_input.txt"

bloom = BloomFilter(bad_passwords_file_name)

bad_passwords = open(bad_passwords_file_name).readlines()
for password in bad_passwords:
    password = password.rstrip()
    bloom.add_to_bloom(password)

possible_passwords = open(possible_passwords_file_name).readlines()
date_and_time = datetime.now().strftime("%Y-%m-%d--%H.%M")

output_file_name = "bloom_filter_output-" + date_and_time + ".txt"
print("output file name: ", output_file_name)
with open(output_file_name, "w") as out_file:
    for password in possible_passwords:
        password = password.rstrip()
        if bloom.check_password(password):
            out_file.write("{} is maybe present\n".format(password))
            print(password, "is maybe present")
        else:
            out_file.write("{}is not present\n".format(password))
            print(password, "is not present")



