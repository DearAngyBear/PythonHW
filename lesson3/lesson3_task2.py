from smartphone import Smartphone

Ph1 = Smartphone ("Nokia", "One", "+7 923 183 45 40")
Ph2 = Smartphone ("Honor", "View20", "+7 913 888 88 88")
Ph3 = Smartphone ("iPhone", "20 Pro", "+7 953 160 16 16")
Ph4 = Smartphone ("Samsung", "Edge", "+7 915 000 00 22")
Ph5 = Smartphone ("Motorola", "Old", "+7 930 555 55 55")

catalog = []

catalog.append (Ph1)
catalog.append (Ph2)
catalog.append (Ph3)
catalog.append (Ph4)
catalog.append (Ph5)

for x in catalog:
    print (f"{x.mark} - {x.model}. {x.number}")
