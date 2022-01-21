file_name = input()
dict1 = {}
titles =[]

with open(file_name, 'r') as input_file:
    lines = input_file.readlines()
    for index in range(0, len(lines) - 1, 2):
        if lines[index].strip() == '':
            continue
        count = int(lines[index].strip())
        show = lines[index + 1].strip()
        if count in dict1.keys():
            show_list = dict1.get(count)
            show_list.append(show)
        else:
            dict1[count] = [show]

    with open('output_keys.txt', 'w+') as q:
        for key in sorted(dict1.keys()):
            q.write('{}: {}\n'.format(key, '; '.join(dict1.get(key))))


    for title in dict1.values():
        titles.extend(title)

    with open('output_titles.txt', 'w+') as outfile:

        for title in sorted(titles):
            outfile.write('{}\n'.format(title))
