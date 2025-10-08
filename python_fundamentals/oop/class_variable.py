class Dolphin:

    pod_id = 1
    pod_name = 'Bay Watchers'
    pod_size = 0

    def __init__(self, name,age, trait):
        self.name = name
        self.age = age
        self.trait = trait
        Dolphin.pod_size += 1


dolphin1 = Dolphin('Taj',18, 'Funny')
dolphin2 = Dolphin('Eliza', 22, 'Fast')
dolphin3 = Dolphin('Bo', 29, 'Clever')

print(f'{dolphin3.name} just joined the pod "{Dolphin.pod_name}" and now the members are {Dolphin.pod_size} in total.')

