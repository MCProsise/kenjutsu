def check_users(current_users, new_users):

    pass

    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']

    new_us = ['george', 'ringo', 'superman', 'hannibal', 'sally']

    for new_user in new_us:
        if new_user in current_us:
            print(f"{new_user} is NOT available.")
        else:
            print(f"{new_user} is available!!!")


if __name__ == "__main__":

    current_us = ['chris','haritha', 'sally', 'darnell', 'superman']

    new_us = ['george', 'ringo', 'superman', 'hannibal', 'sally']

    check_users(current_us, new_us)