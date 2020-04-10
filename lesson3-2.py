def person_info(name, lastname, birthday, city, email, phone):
    return f"Name - {name}; Last name - {lastname}; birthday - {birthday}; " \
           f"city - {city}; email - {email}; phone - {phone}"


print(person_info(name="Василий", lastname="Пупкин", birthday="25.10.85", city="Саратов",
                  email="vasil.pupkin@gmail.com", phone="+79179189189"))
