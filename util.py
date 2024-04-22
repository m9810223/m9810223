from urllib.parse import quote


AUTHOR = 'm9810223'
QUERY = quote(f'author:{AUTHOR} is:merged')
GH = 'https://github.com'
SH_GH = 'https://img.shields.io/github'


def md_img(src: str, *, alt: str = ''):
    return f'![{alt}]({src})'


def md_a(href: str, *, text: str = ''):
    return f'[{text}]({href})'


def md_li(content: str):
    return f'- {content}'


def convert(user_repo: str):
    pathname = f'{SH_GH}/issues-search/{user_repo}'
    search = f'?style=for-the-badge&label={quote(user_repo)}&query={QUERY}'
    src = f'{pathname}{search}'
    img = md_img(src, alt=user_repo)
    href = f'{GH}/{user_repo}/pulls?q={QUERY}'
    a = md_a(href, text=img)
    li = md_li(a)
    return li


def main():
    contributions = [
        'rabbitmq/tls-gen',
        'rabbitmq/rabbitmq-website',
        'tiangolo/typer',
        'beancount/fava',
        'encode/httpcore',
        'microsoft/playwright-python',
        'microsoft/playwright-pytest',
        'pydantic/pydantic-settings',
        'psf/cachecontrol',
        'pdm-project/pdm',
    ]
    for x in contributions:
        print(convert(x))


if __name__ == '__main__':
    main()
