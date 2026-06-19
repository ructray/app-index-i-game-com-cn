from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List, Optional


@dataclass
class KeywordNote:
    keyword: str = ""
    description: str = ""
    source_url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@dataclass
class NoteCollection:
    title: str = "未命名笔记集"
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def count(self) -> int:
        return len(self.notes)


def format_single_note(note: KeywordNote) -> str:
    parts = [
        f"【关键词】{note.keyword}",
        f"【描述】{note.description}",
        f"【来源】{note.source_url}",
        f"【标签】{', '.join(note.tags) if note.tags else '无'}",
        f"【创建时间】{note.created_at}",
    ]
    return "\n".join(parts)


def format_collection(collection: NoteCollection, separator: str = "-" * 30) -> str:
    header = f"📒 {collection.title}（共 {collection.count()} 条笔记）\n{separator}"
    items = []
    for i, note in enumerate(collection.notes, 1):
        items.append(f"笔记 {i}:\n{format_single_note(note)}")
    return header + "\n\n" + f"\n\n{separator}\n\n".join(items)


def generate_sample_collection() -> NoteCollection:
    collection = NoteCollection(title="游戏关键词笔记")
    collection.add_note(
        KeywordNote(
            keyword="爱游戏",
            description="聚焦游戏文化、评测与资讯的综合平台",
            source_url="https://app-index-i-game.com.cn",
            tags=["游戏", "平台", "评测"],
        )
    )
    collection.add_note(
        KeywordNote(
            keyword="爱游戏攻略",
            description="提供热门游戏通关技巧与隐藏要素",
            source_url="https://app-index-i-game.com.cn/guides",
            tags=["攻略", "技巧"],
        )
    )
    collection.add_note(
        KeywordNote(
            keyword="爱游戏社区",
            description="玩家交流讨论、分享心得的互动空间",
            source_url="https://app-index-i-game.com.cn/community",
            tags=["社区", "交流"],
        )
    )
    return collection


def export_notes_as_dicts(collection: NoteCollection) -> List[dict]:
    return [asdict(note) for note in collection.notes]


if __name__ == "__main__":
    sample = generate_sample_collection()
    output = format_collection(sample)
    print(output)