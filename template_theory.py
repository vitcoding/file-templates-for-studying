from string_number import dbl_number


# theory file template creation
def theory_file(
    file_path: str, chapter: int, lesson: int, theme: str, themes_num: int = 5
) -> None:

    with open(file_path, mode="w", encoding="utf-8") as fw:
        fw.write(
            f"##### {dbl_number(chapter)}.{dbl_number(lesson)} {theme.capitalize()}\n"
        )
        fw.write(f"# Lesson notes{'\n' * 4}")

        for i in range(1, themes_num + 1):
            fw.write(f"### Step {i}. Theory\n{'#' * 55}\n{'\n' * 10}\n")
            fw.write(f"### Step {i}. Comments\n")
            for j in range(6):
                fw.write(f"{'#' * 35}\n\n")
            fw.write(f"{'\n' * 10}\n")


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
    #############################

    file_name = f"{dbl_number(chapter)}_{dbl_number(lesson)}_{theme}.txt"
    th_file_path = folder + file_name
    theory_file(th_file_path, chapter, lesson, theme)

    #
    ###
    print("-" * 100)


if __name__ == "__main__":
    main()
