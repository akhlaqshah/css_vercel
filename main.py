# This is a sample Python script.
from flask import Flask

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    my_list =[1,2,3,4,5,6,7,8,9,10]
    print(f'Hi, {name} {my_list[-4:]}')  # Press ⌘F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(f'PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
