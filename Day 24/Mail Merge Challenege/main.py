PLACEHOLDER="[name]"

with open("Day 24/Mail Merge Challenege/names.txt") as name_file:
    names=name_file.readlines()

with open("Day 24/Mail Merge Challenege/mail.txt") as mail_file:
    mail=mail_file.read()
    for name in names:
        stripped_name=name.strip()
        new_mail=mail.replace(PLACEHOLDER,stripped_name)
        with open (f"Day 24/Mail Merge Challenege/Mails/letter_for_{stripped_name}.txt",mode='w') as final_mail:
               final_mail.write(new_mail)