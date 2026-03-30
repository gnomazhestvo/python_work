# 7.1. Каршеринг. Напишите программу, которая спрашивает у
# пользователя, какую машину он хотел бы взять напрокат.
# Выведите сообщение с введенными данными (например,
# «Посмотрим, смогу ли я найти вам Subaru»).

message = 'Какую машину вы хотели бы взять напрокат?\n'
car_model = input(message)
car_model = car_model.lower()

if car_model == 'bmw':
    car_model_modified = car_model.upper()
else:
    car_model_modified = car_model.title()
print(f'Посмотрим, смогу ли я найти для вас {car_model_modified}...')