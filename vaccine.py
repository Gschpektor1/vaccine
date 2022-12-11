class Human:

    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type

    def __repr__(self):
        return self.name
    # Represents a citizen of the city, it has the following attributes:
    # id_number (str), name (str), age (int), priority (bool)
    # and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.


class Queue:
    def __init__(self, humans=[]):
        self.humans = humans

    def add_person(self, person):
        if person.age > 60:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)
    # Adds a human to the queue, if he is older than 60 years old or a priority person,
    # put him at the beginning of the list (at index 0) before every other.

    def find_in_queue(self, person):
        return self.humans.index(person)
    # Returns the index of a human in the queue.

    def swap(self, person1, person2):
        a, b = self.humans.index(person1), self.humans.index(person2)
        self.humans[b], self.humans[a] = self.humans[a], self.humans[b]
    # Swaps person1 with person2.

    def get_next(self):
        return self.humans[0]
    # Returns the next human waiting in the queue.
    # The next human should be the one located at the index 0 in the list.

    def get_next_blood_type(self, blood_type):
        for human in self.humans:
            if human.blood_type == blood_type:
                return human
        return 'none'
    # Returns the first human with this specific blood type.

    def sort_by_age(self):
        queue = self.humans.sort(key=(priority=True))
    # Sorts the queue
    # first the priority people
    # then, the older people
    # then the younger people


human_1 = Human(1, 'Adam', 18, True, 'O')
human_2 = Human(2, 'Bob', 88, False, 'A')
human_3 = Human(3, 'Charlie', 59, True, 'B')

queue = Queue()

queue.add_person(human_1)
queue.add_person(human_2)
queue.add_person(human_3)




