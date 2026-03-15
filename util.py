from urllib.parse import quote
from typing import Literal


AUTHOR = 'm9810223'
QUERY = quote(f'is:merged author:{AUTHOR}')
GH = 'https://github.com'

CONTRIBUTIONS = [
    'beancount/fava',  # chore
    'encode/httpcore',  # refine
    'fastapi/typer',  # fix
    'likec4/likec4',  # feat
    'microsoft/playwright-pytest',  # typo
    'microsoft/playwright-python',  # refine / fix
    'pdm-project/pdm',  # docs(fix)
    'psf/cachecontrol',  # chore
    'pydantic/pydantic-settings',  # fix(feat)
    'rabbitmq/rabbitmq-website',  # docs(fix)
    'rabbitmq/tls-gen',  # chore(fix)
]

SH_GH = 'https://img.shields.io/github'
STYLE: Literal['flat', 'flat-square', 'plastic', 'for-the-badge', 'social'] = 'social'


def convert(user_repo: str) -> str:
    pathname = f'{SH_GH}/issues-search/{user_repo}'
    search = f'?style={STYLE}&label={quote(user_repo)}&query={QUERY}'
    src = f'{pathname}{search}'
    img = _md_img(src, alt=user_repo)
    href = f'{GH}/{user_repo}/pulls?q={QUERY}'
    a = _md_a(href, text=img)
    return a

    li = _md_li(a)
    return li


def main() -> None:
    for x in CONTRIBUTIONS:
        if x is not None:
            print(convert(x))

        print()


def _md_img(src: str, *, alt: str = '') -> str:
    return f'![{alt}]({src})'


def _md_a(href: str, *, text: str = '') -> str:
    return f'[{text}]({href})'


def _md_li(content: str) -> str:
    return f'- {content}'


if __name__ == '__main__':
    main()
