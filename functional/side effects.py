# This is a contrived example of 'side effects'. Two threads (the 'main thread' and the one started on line 25)
# run the same code. Because the StringMeasurer object created on line 21 exists in memory that can be altered by
# both threads, the timing of how each thread runs can affect the program's output. As it stands, the program
# will give the wrong output - uncomment line 27 to make it give the correct output. In the real world, having
# multiple threads writing to the same memory can cause many problems, which can sometimes be almost impossible
# to track down

import _thread
import time

class StringMeasurer:
    def __init__(self, string_to_measure):
        self.string_to_measure = string_to_measure      # side effect - stores an instance variable on the current object

    def set_string_to_measure(self, new_string_to_measure):
        self.string_to_measure = new_string_to_measure  # side effect - stores an instance variable on the current object

    def print_string_length(self):
        print(len(self.string_to_measure))

measurer = StringMeasurer("Hello")

# Create a thread which will call StringMeasurer.print_string_length
# second parameter is a tuple giving the arguments which will be passed to the specified function on the new thread
_thread.start_new_thread (StringMeasurer.print_string_length, (measurer,))  # tuple with single item must have a comma

#time.sleep(1)

measurer.set_string_to_measure("Something else")
measurer.print_string_length()

time.sleep(1)
