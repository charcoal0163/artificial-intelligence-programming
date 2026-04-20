import classModule
obj1 = classModule.Student(202420163, "Ahamd", "Mathematics", "Professor", 1, 3, 2024)
obj1.printDeets()

import classModule as mod
obj2 = mod.User("Acheron", "Dalbah", 19)
obj2.describe()

from classModule import Admin as alias
obj3 = alias("Acheron", "Dalbah", 19, "Can add files", "Can delete files")
obj3.describe()