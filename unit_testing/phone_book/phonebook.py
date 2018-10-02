from collections import Counter


class PhoneBook:
    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        if len(self.entries) == 0 or len(self.entries) == 1:
            return True

        cnt = Counter()

        for phone_number in self.entries.values():
            cnt[phone_number] += 1

        if cnt.most_common(1)[0][1] > 1:
            return False

        phone_numbers = list(cnt.elements())

        for i in range(len(phone_numbers)):
            for j in range(i + 1, len(phone_numbers)):
                if len(phone_numbers[i]) < len(phone_numbers[j]):
                    if phone_numbers[j].startswith(phone_numbers[i]):
                        return False
                else:
                    if phone_numbers[i].startswith(phone_numbers[j]):
                        return False
        return True
