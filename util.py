from urllib.parse import quote


AUTHOR = 'm9810223'
QUERY = quote(f'is:merged author:{AUTHOR}')
GH = 'https://github.com'

CONTRIBUTIONS = [
    'microsoft/playwright-python',  # refine / fix
    'fastapi/typer',  # fix
    'pydantic/pydantic-settings',  # fix(feat)
    'likec4/likec4',  # feat
    'encode/httpcore',  # refine
    'rabbitmq/tls-gen',  # chore(fix)
    'beancount/fava',  # chore
    'psf/cachecontrol',  # chore
    'rabbitmq/rabbitmq-website',  # docs(fix)
    'pdm-project/pdm',  # docs(fix)
    'microsoft/playwright-pytest',  # typo
]

SH_GH = 'https://img.shields.io/github'
STYLE = 'for-the-badge'


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
