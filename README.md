# bloom_filter
bloom_filter is a way of determining if a password falls in a list of given passwords (meant to be easily guessed passwords)

The progame takes two txt files where each line denotes a password. 
 - The first file is a list of passwords to be entered into the bloom filter. 
 - The second file is a list of passwords to test if they are now in the bloom filter. 

This gives a good example of how bloom filters can be used quickly and efficiently to create better security measures when users are trying to create a password.

prints output to a file named bloom_filter_output_[date]--[time].txt and prints the output to the command line

## Installation - non OSU server
```bash
pip install -r requirements.txt 
```

## Usuage 

```python
python3 bloom_filter.py

Please enter the name of the file name with the bad passwords: [file path]
Please enter the name of the file with possible passwords: [file path]

Bit array size will be [some number]
False positive probability of 0.00000010
[some number] hash function(s) will be used

output file name: bloom_filter_output_[date]--[time].txt
[password1] is maybe present
[password2] is maybe present
[password3] is maybe present
[password4] is maybe present
[password5] is not present
etc...
``` 
