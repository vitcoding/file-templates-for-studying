from string_number import dbl_number

# exercise file template creation
def exercise_file(
    file_path: str,
    chapter: int,
    lesson: int,
    theme: str,
    # ex_quantity: int = 30,
    start_exercise_num: int = 1,
    end_exercise_num: int = 30,
) -> None:

    with open(file_path, mode="w", encoding="utf-8") as fw:
        fw.write(f'print("-" * 100)\n\n')
        fw.write(f'##### {dbl_number(chapter)}.{dbl_number(lesson)} {theme.capitalize()}\n')
        fw.write(f"# Lesson notes{'\n' * 3}")

        for i in range(start_exercise_num, end_exercise_num + 1):
            fw.write("###\n# ")
            fw.write(
                f"{dbl_number(chapter)}.{dbl_number(lesson)}.{dbl_number(i)}\n\n\n"
            )
            fw.write(
                f"def {theme}_{dbl_number(chapter)}_{dbl_number(lesson)}_{dbl_number(i)}():\n{" " * 4}pass\n\n\n"
            )
            # fw.write("\tpass") # "\t" - wrong var
            fw.write(
                f"# {theme}_{dbl_number(chapter)}_{dbl_number(lesson)}_{dbl_number(i)}()\n\n"
            )
            fw.write('"' * 3 + "\n" * 2 + '"' * 3 + "\n\n\n")

        fw.write("###\n#\n\n\n")

        fw.write("# print()\n")
        fw.write("#\n\n")
        fw.write('print("-" * 100)\n\n')
        fw.write('"' * 3 + "\n" * 2 + '"' * 3 + "\n\n")


def main():
    print(__file__.split("\\")[-1])
    print("-" * 100)
    ###
    #

    folder = "./"

    #############################
    # input block
    chapter = 9
    lesson = 3
    theme = "example"
    # theme = "example"
    start_exercise_num = 1
    end_exercise_num = 13
    #############################

    file_name = f"{dbl_number(chapter)}_{dbl_number(lesson)}_{theme}.py"
    ex_file_path = folder + file_name

    # exercise_file(ex_file_path, chapter, lesson, theme)

    #
    ###
    print("-" * 100)


if __name__ == "__main__":
    main()
