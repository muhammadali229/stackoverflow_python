import sys
input_sys = int(sys.argv[1])
print([input_sys if i == input_sys else i for i in range(input_sys, input_sys + 5)])