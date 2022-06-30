from parsing import parsing_methods as pm


def main():
    text_search = input("Input request: ")
    pm.parse_search_yandex(text=text_search)


if __name__ == '__main__':
    main()
