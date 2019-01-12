# Exception handling in python

try:
    f = open(r'testfile.txt') # When this operation fails do things as in except block instead of giving the error
    if f.name == "test_file.txt":
        raise Exception
except FileNotFoundError as e: #manage the file not found error
    print(e) 
except Exception as e:
    print("Error!")
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally...")





try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# Output: An IOError occurred. No such file or directory
# This would be printed whether or not an exception occurred!


try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # any code that should only run if no exception occurs in the try,
    # but for which exceptions should NOT be caught
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs. And an error here would NOT be caught
# This would be printed in every case.