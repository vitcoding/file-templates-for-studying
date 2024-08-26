import os
import re
import slugify  # from slugify import slugify # pip install awesome-slugify
from content import content_file
from string_number import dbl_number
from template_theory import theory_file
from template_exercize import exercise_file


def string_convertion(str):
    numbers_str, *theme_list = str.split()
    theme = (" ").join(theme_list)
    numbers_list = [int(n) for n in numbers_str.split(".") if n]
    return *numbers_list, theme


def create_folder(path):
    os.makedirs(path)
    # os.mkdir(path, mode=0o777, *, dir_fd=None)
    # os.makedirs(name, mode=0o777, exist_ok=False)


def slug_to_snake_case(slug_data):
    line_list = slug_data.lower().split("-")
    return "_".join(line_list)


def main():
    print("main")
    print("-" * 100)
    ###
    #

    folder = "./content/"
    content_raw_filename = "content_raw.txt"
    content_filename = "content.txt"
    content_raw_file_path = folder + content_raw_filename
    content_file_path = folder + content_filename
    if not os.path.exists(content_filename):
        content_file(content_raw_file_path, content_file_path)

    templates_folder = "_study_templates"
    # if not os.path.exists(templates_folder):
    #     create_folder(templates_folder)

    regex_folder = r"\d+\.\s\w+"
    regex_theme = r"\d+\.\d+\s\w+"
    folder_name, folder_path = "", f"{templates_folder}/"
    with open(content_file_path, mode="r", encoding="utf-8") as fr:
        for line in fr:
            if re.search(regex_folder, line):
                chapter, theme = string_convertion(line.rstrip())
                folder_name = f"{dbl_number(chapter)}_{slugify.slugify(theme, separator="_")}"
                # print(folder_name)

                # folder_path = f"../{templates_folder}/{folder_name}/"
                folder_path = f"{templates_folder}/{folder_name}/"
                if not os.path.exists(folder_path):
                    create_folder(folder_path)
                    create_folder(f"{folder_path}/Files_{dbl_number(chapter)}")
                    create_folder(f"{folder_path}/_temp_{dbl_number(chapter)}")
            elif re.search(regex_theme, line):
                chapter, lesson, theme = string_convertion(line.rstrip())
                number_str = f"{dbl_number(chapter)}_{dbl_number(lesson)}"
                theme_slug = slugify.slugify(theme.lower(), separator='_')
                theme_name = f"{number_str}_{theme_slug}"
                # print(theme_name)

                ex_file_name = f"{theme_name}.py"
                ex_file_path = folder_path + ex_file_name
                exercise_file(ex_file_path, chapter, lesson, theme_slug)

                th_file_name = f"{theme_name}.txt"
                th_file_path = folder_path + th_file_name
                theory_file(th_file_path, chapter, lesson, theme)
                # break
                
    print("Created directories and files:\n")
    for el in list(os.walk(templates_folder))[1:]:
        print(el[0])
        for file in el[2]:
            print(" ", file)
        print()

    #
    ###
    print("-" * 100)


if __name__ == "__main__":
    main()
