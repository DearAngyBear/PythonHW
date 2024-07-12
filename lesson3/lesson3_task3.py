from mailing import Mailing
from address import Address

Ad1 = Address ("124365", 'Москва', 'Ленина', "1", "34")
Ad2 = Address ("191186","Санкт-Петербург", "Казанская", 4, 1)
M1 = Mailing ( Ad2, Ad1, 100, "№12345")

print (f"Отправление {M1.track} из {M1.from_address.index}, {M1.from_address.city}, {M1.from_address.street}, {M1.from_address.house} - {M1.from_address.flat}" 
       f" в {M1.to_address.index}, {M1.to_address.city}, {M1.to_address.street}, {M1.to_address.house} - {M1.to_address.flat}. Стоимость {M1.cost} рублей." )