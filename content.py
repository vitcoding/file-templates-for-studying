import re


def content_file(content_raw_file_path, content_file_path="content.txt"):
    regex = r"\d+\.\d*\s\w+"
    with open(content_raw_file_path, mode="r", encoding="utf-8") as fr, open(
        content_file_path, mode="w", encoding="utf-8"
    ) as fw:
        data = []
        for line in fr:
            if re.search(regex, line):
                # print(line.strip())
                fw.write(line)


def main():
    print(__file__.split("\\")[-1])
    print("-" * 100)
    ###
    #

    # print("It's " + f'{__file__.split("\\")[-1]}')

    folder = "./"
    content_raw_filename = "content_raw.txt"
    content_filename = "tmp_content.txt"
    content_raw_file_path = folder + content_raw_filename
    content_file_path = folder + content_filename

    content_file(content_raw_filename, content_filename)

    #
    ###
    print("-" * 100)


if __name__ == "__main__":
    main()
