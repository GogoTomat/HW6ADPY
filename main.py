def get_name(doc_number):
    for number in documents:
        if number['number'] == doc_number:
            return number['name']

def get_shelf(document_number):
    for doc in directories:
        if document_number in directories[doc]:
            return doc
    return "No such document"

def get_all_doc():
    for doc in documents:
        type = doc['type']
        number = doc['number']
        name = doc['name']
        print('{0} "{1}" "{2}"'.format(type, number, name))

def add_new_doc(doc_type, doc_number, doc_owner, shelf_id):
    if shelf_id not in directories:
        return "No such directory"
    else:
        new_doc = dict(type=doc_type, number=doc_number, name=doc_owner)
        documents.append(new_doc)
        directories[shelf_id] += [doc_number]
        return "Document added successfully"

def add_shelf():
    number = input("Enter the number of the new shelf: ")
    directories[number] = []

def move_doc(doc_number, shelf_number):
    doc_existence = False

    if shelf_number not in directories:
        return "No such shelf"

    for key, value in directories.items():
        if doc_number in value:
            doc_existence = True
            directories[shelf_number] += [doc_number]
            value.remove(doc_number)

    if doc_existence:
        return "Document added successfully"
    else:
        return "No such document"

def del_doc(doc_number):
    initial_len = len(documents)
    for i, d in enumerate(documents):
        if d["number"] == doc_number:
            documents.pop(i)

    if initial_len == len(documents):
        return "No such document"

    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)

    return "Document deleted successfully"

def main():
    while True:
        print("Commands: p, s, l, a, d, m, as, q.")
        command = str(input('Input the command: '))

        if command == 'p':
            number_doc = input('Input the number of the document: ')
            print(get_name(number_doc))
        elif command == 's':
            number_doc = input('Input the number of the document: ')
            print(get_shelf(number_doc))
        elif command == 'l':
            get_all_doc()
        elif command == 'a':
            doc_type = input("Input the type of the document: ")
            doc_number = input("Input the number of the document: ")
            doc_owner = input("Input the owner's name: ")
            shelf_id = input("Input the number of the shelf : ".format(directories.keys()))
            print(add_new_doc(doc_type, doc_number, doc_owner, shelf_id))
            print('')
            print(documents)
            print('')
            print(directories)
        elif command == 'd':
            doc_number = input("Input the number of the document which you want to delete: ")
            print(del_doc(doc_number))
            print(documents)
            print(directories)
        elif command == 'm':
            doc_number = input("Input the number of the document you want to move: ")
            shelf_id = input("Input the number of the shelf to which you want to move the document: ")
            print(move_doc(doc_number, shelf_id))
            print(directories)
        elif command == 'as':
            add_shelf()
        elif command == 'q':
            break

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

main()
