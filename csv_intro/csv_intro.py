import csv
import re


def valid_email(email: str) -> bool:
    regex = re.compile(
        r'(?:[a-z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:['
        r'\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:['
        r'a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?['
        r'0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:['
        r'\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')
    if regex.match(email):
        return True
    else:
        return False


class Person:
    def __init__(self, title, first_name, last_name, gender, email):
        self._title = title
        self._first_name = first_name
        self._last_name = last_name
        self._gender = gender
        if valid_email(email):
            self._email = email
        else:
            raise Exception(f"The email {email} is not a valid email address")

    def get_title(self):
        return self._title

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_gender(self):
        return self._gender

    def get_email(self):
        return self._email


def read_persons_csv(file: str = "user_details.csv") -> list:
    try:
        persons = []
        with open(file, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            next(csv_reader)
            for line in list(csv_reader):
                persons.append(Person(line[0],
                                      line[1],
                                      line[2],
                                      line[3],
                                      line[4]))
            return persons
    except:
        print("Error: File not found")


def extract_names_and_email(persons: list) -> list:
    tr_lines = [[person.get_first_name(), person.get_last_name(), person.get_email()] for person in persons]
    return tr_lines


def write_persons_csv(lines: list, file: str = "new_details.csv") -> None:
    try:
        with open(file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow(["firstName", "lastName", "email"])
            csv_writer.writerows(lines)
    except:
        print("Unable to write to csv file")


if __name__ == "__main__":
    data = read_persons_csv()
    tr_data = extract_names_and_email(data)
    write_persons_csv(tr_data)
