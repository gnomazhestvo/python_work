from pathlib import Path

path = Path('text_files/programming.txt')

contents = 'I love programming.\n'
contents += 'I love creating new games.\n'
contents+= 'I also love working with data.\n'

path.write_text(contents)