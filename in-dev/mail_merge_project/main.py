# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Opens invited_names.txt
with open("./invited_names.txt", 'r') as names:

    # Opens the starting_letter.txt file, reads & locates line that will be replaced.
    with open("./starting_letter.txt", 'r', encoding='utf-8') as mail_file:
        first_line = mail_file.readlines(1)
        get_first_line = first_line[0]
        content = mail_file.read()

        # Loop through the names and replace the first line then create new letter.
        for name in names:
            write_new_line = get_first_line.replace(
                "[name]", f"{name.strip()}")
            new_mail = write_new_line + content

            # Writes new letter and creates filename.
            with open("./mail_merge_project/output/ready_to_send/letter_for_"+name.strip()+".txt", "w") as individual_mail:
                individual_mail.write(new_mail)
