from datetime import date, datetime


def check_func(year):
    current_year = date.today().year
    birth_year = int(year)

    age = current_year - birth_year

    if age < 18:
        return 'Minor'
    elif age == 18 or age <= 36:
        return 'Youth'
    elif age > 36:
        return 'Elder'


if __name__ == '__main__':
    year = input("Enter your year of birth: ")
    user_year = datetime.strptime(year, "%Y")
    user_state = check_func(user_year)
    print(user_state)
