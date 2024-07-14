def test_config():
    return True

def create_dictionary():
    prog_langs = {"C++":"1979","Java":"1992","Python":"1996","C#":"2001"} #4 pairs Keys/Values
    print(prog_langs)
    print(prog_langs["C++"])
    print(prog_langs["Python"])

    if "C+++" in prog_langs:
        print(prog_langs["C+++"])

    prog_langs["Ada"] = "1980" #Add a value
    print(prog_langs)

    prog_langs["C++"] = "1980"
    print(prog_langs)

    if "C#" in prog_langs:
        del prog_langs["C#"]
        print(prog_langs)

    prog_langs["C#"] = 2001
    print(prog_langs)

def use_for_loop_dictionary():
    prog_langs = {"C++":"1979","Java":"1992","Python":"1996","C#":"2001"}

    print(prog_langs.keys())

    for current_key in prog_langs:
        print(current_key, prog_langs[current_key])

    for current_value in prog_langs.values():
        print(current_value)

    for keys, values in prog_langs.items():
        print(keys, values)

def use_while_loop_dictionary():
    prog_langs = {"C++":"1979","Java":"1992","Python":"1996","C#":"2001"}

    keys = prog_langs.keys()
    print(keys)
    keys_list = list(keys)
    print(keys_list)

    indx = 0

    while indx < len(keys_list):
        print(prog_langs[keys_list[indx]])
        indx += 1

def dictionary_built_in_methods():
    prog_langs = {"C++":"1979","Java":"1992","Python":"1996","C#":"2001"}

    prog_langs.clear()
    print(prog_langs)

    prog_langs = {"C++":"1979","Java":"1992","Python":"1996","C#":"2001"}

    value = prog_langs.get("C++", "Key Not Found")
    print(value)

    item = prog_langs.popitem()
    print(prog_langs)
    print(item)

    
