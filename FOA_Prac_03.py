def dfs_scenario(links, protagonist):
    visited = set()

    def dfs(person):
        if person not in visited:
            print(person, end=" ")
            visited.add(person)
            for linked_person in links[person]:
                dfs(linked_person)

    dfs(protagonist)

links = {
    'Sorav': ['PERSON A,', 'PERSON B,', 'PERSON C,'],
    'PERSON A,': ['PERSON D,', 'PERSON E,'],
    'PERSON B,': ['PERSON F,'],
    'PERSON C,': ['PERSON G,', 'PERSON H,'],
    'PERSON D,': [ ],
    'PERSON E,': [ ],
    'PERSON F,': [ ],
    'PERSON G,': [ ],
    'PERSON H,': [ ]

}
First_person = 'Sorav'
print('dfs traversal')
dfs_scenario(links, First_person)
