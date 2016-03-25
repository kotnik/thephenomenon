#!/usr/bin/env python3
from bs4 import BeautifulSoup
from ebooklib import epub


if __name__ == '__main__':
    chapters = {}

    soup = BeautifulSoup(open("full.html"), 'html.parser')
    for chapter_id in range(1, 200):
        chapter = soup.find(id=chapter_id)
        if not chapter:
            continue
        chapter_title = chapter.h2.text
        chapter_body = chapter.find('div', class_='md').prettify()

        chapters[chapter_id] = {
            "title": chapter_title,
            "body": '<h2>' + chapter_title + '</h2>' + chapter_body
        }

    book = epub.EpubBook()
    book.set_identifier('idphenomenon')
    book.set_title('The Phenomenon')
    book.set_language('en')
    book.add_author('Emperor Cartagia')

    ch_epub = []
    for chapter_id, chapter in chapters.items():
        # intro chapter
        ch = epub.EpubHtml(title=chapter['title'], file_name='ch_%s.xhtml' % chapter_id, lang='en')
        ch.content = chapter['body']
        book.add_item(ch)
        ch_epub.append(ch)

    book.toc = ch_epub

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    style = '''
@namespace epub "http://www.idpf.org/2007/ops";
body {
    font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
}
code {
    white-space: normal;
}
h2 {
     text-align: left;
     text-transform: uppercase;
     font-weight: 200;
}
ol {
        list-style-type: none;
}
ol > li:first-child {
        margin-top: 0.3em;
}
nav[epub|type~='toc'] > ol > li > ol  {
    list-style-type:square;
}
nav[epub|type~='toc'] > ol > li > ol > li {
        margin-top: 0.3em;
}
'''

    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)
    book.add_item(nav_css)

    book.spine = ['nav'] + ch_epub

    epub.write_epub('test.epub', book, {})
