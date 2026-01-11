from typing import Dict, List
from app.models import Term

glossary: Dict[str, Term] = {
    "Event loop": Term(
        title="Event loop",
        definition="Механизм, который управляет выполнением асинхронных задач, распределяя время процессора между ними.",
        source_link="https://docs.python.org/3/library/asyncio-eventloop.html"
    ),
    "Coroutine": Term(
        title="Coroutine",
        definition="Функция, которая может приостанавливать своё выполнение и передавать управление event loop для других задач.",
        source_link="https://docs.python.org/3/library/asyncio-task.html#coroutines"
    ),
    "Future": Term(
        title="Future",
        definition="Объект, представляющий результат асинхронной операции, который станет доступен в будущем.",
        source_link="https://docs.python.org/3/library/asyncio-future.html"
    ),
    "Concurrency": Term(
        title="Concurrency",
        definition="Способность программы выполнять несколько задач одновременно, используя асинхронные механизмы.",
        source_link="https://en.wikipedia.org/wiki/Concurrency_(computer_science)"
    ),
    "Parallelism": Term(
        title="Parallelism",
        definition="Выполнение нескольких задач одновременно на разных ядрах процессора для повышения производительности.",
        source_link="https://en.wikipedia.org/wiki/Parallel_computing"
    ),
}


def get_all_terms() -> List[Term]:
    return list(glossary.values())


def get_term(title: str) -> Term | None:
    return glossary.get(title)


def add_term(term: Term) -> Term | None:
    if term.title in glossary:
        return None
    glossary[term.title] = term
    return term


def update_term(title: str, definition: str | None = None, source_link: str | None = None) -> Term | None:
    term = glossary.get(title)
    if not term:
        return None
    if definition is not None:
        term.definition = definition
    if source_link is not None:
        term.source_link = source_link
    return term


def delete_term(title: str) -> Term | None:
    return glossary.pop(title, None)
