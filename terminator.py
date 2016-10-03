import requests

from lxml import etree


response = requests.get('https://linux.die.net/man/1/terminator')
root = etree.HTML(response.content)


def render_table(title, column_headers, dl_node, text=''):
    text += '\n\n## {}\n\n'.format(title)
    text += format_row(column_headers)
    text += format_row(['------' for header in column_headers])
    for command in get_commands(dl_node):
        text += format_row(command)
    return text


def format_row(iterable):
    return '|' + '|'.join(iterable) + '|\n'


def get_commands(dl_node):
    def get_text(node):
        return ''.join([x for x in node.itertext()]).replace('\n', '')

    commands = []
    idx = 0
    children = dl_node.getchildren()

    while idx + 2 <= len(children):
        dt, dd = children[idx:idx + 2]
        commands.append((get_text(dd), get_text(dt)))
        idx += 2

    return commands


if __name__ == "__main__":
    options, keybindings = root.xpath('//*[@id="content"]/dl')

    readme = '# Terminator Keyboard Shortcuts and Options\n\n'
    readme += render_table('Keybindings', ['Description', 'Shortcut'], keybindings)
    readme += render_table('Options', ['Description', 'Option'], options)

    with open('README.md', 'w') as f:
        f.write(readme)
