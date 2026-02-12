# def login(**kwargs):

#     if "username" in kwargs and "password" in kwargs:
#         print("login successful")


# login(username='root', password='root')


# def student_data(**kwargs):


# student_data(hari=70, suman=32, himal=90)


def position(*args, **kwargs):

    print(args)
    print(kwargs)


position(
    1,
    2,
    3,
    4,
    5,
    add=True,
)


def test(**data):
    print(data)
    print(type(data))

    print(data.keys())


test(fname="hari", lname="sharma", middle_name="test", testing="test")


# in
def login(**kwargs):
    if "username" in kwargs and "password" in kwargs:
        print("login successful")
    else:
        print("both username and password keys are required")


login(username="root", password="132456")  # login successful
login(username="test")  # both username and password keys are required
login(password="test")  # both username and password keys are required

# Design a function that takes **kwargs representing student names as keys and their marks as values.
# Ignore students with marks below 40
# Calculate and display the average of the remaining students


def student_data(**kwargs):
    print(kwargs.values())

    for i in kwargs.values():
        if i >= 40:
            pass


student_data(hari=70, suman=32, sudan=71, himal=100)


def test(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


test(1, 2, 3, 4, 5, 6, 7, name="hari", age=10)


def math_operation(*args, **kwargs):
    add = 0
    multiple = 1
    if kwargs["add"]:
        for i in args:
            add = add + i
        return add

        print("perform add")
    elif kwargs["multiple"]:
        for i in args:
            multiple = multiple * i
        return multiple


print(math_operation(1, 2, 4, add=False, multiple=True))
