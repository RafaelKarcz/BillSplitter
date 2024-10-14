import random

def get_friend_names(friend_count: int) -> dict:
    """
    Prompts the user to input the names of friends and returns a dictionary with names as the keys and zeroes as the initial values.
    """
    friends_dictionary = {}
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(friend_count):
        friend_name = input()
        friends_dictionary[friend_name] = 0
    return friends_dictionary

def get_friend_count() -> int:
    """
    Prompts the user to input the number of friends joining and returns the count.
    """
    try:
        number_of_friends = int(input('Enter the number of friends joining (including you): '))
        if number_of_friends >= 1:
            return number_of_friends
        else:
            print('No one is joining for the party')
            return 0
    except ValueError:
        print('ValueError. Only integers are allowed.')
        return 0

def get_total_bill() -> int:
    """
    Prompts the user to input the total bill value and returns it.
    """
    try:
        total_bill_value = int(input('Enter the total bill value:\n'))
        return total_bill_value
    except ValueError:
        print('ValueError. Only integers are allowed.')
        return 0

def split_the_bill(friend_count: int, total_bill_value: int) -> int:
    """
    Calculates the split bill value per friend.
    """
    if total_bill_value % friend_count == 0:
        return total_bill_value // friend_count
    else:
        return round(total_bill_value / friend_count, 2)

def apply_lucky_feature(friend_count: int, friends_dictionary: dict, total_bill_value: int) -> dict:
    """
    Applies the lucky feature, where one friend is chosen randomly to not pay, and the rest share the bill.
    """
    user_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if user_choice == 'Yes':
        lucky_friend = random.choice(list(friends_dictionary.keys()))
        print(f'{lucky_friend} is the lucky one!')
        adjusted_split_value = (
            total_bill_value // (friend_count - 1)
            if total_bill_value % (friend_count - 1) == 0
            else round(total_bill_value / (friend_count - 1), 2)
        )
        for friend in friends_dictionary:
            friends_dictionary[friend] = adjusted_split_value
        friends_dictionary[lucky_friend] = 0
    elif user_choice == 'No':
        print('No one is going to be lucky')
    else:
        print('Sorry, only Yes or No are accepted as input.')
    return friends_dictionary

def main():
    number_of_friends = get_friend_count()
    if number_of_friends == 0:
        return

    friends_dictionary = get_friend_names(number_of_friends)
    total_bill_value = get_total_bill()
    if total_bill_value == 0:
        return

    split_value = split_the_bill(number_of_friends, total_bill_value)
    friends_dictionary = {key: split_value for key in friends_dictionary.keys()}
    friends_dictionary = apply_lucky_feature(number_of_friends, friends_dictionary, total_bill_value)
    
    print(friends_dictionary)

if __name__ == '__main__':
    main()