# kindle my clipping file processor
import os
import re
import pprint
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass

KINDLE_FILE_DIR = "kindle"
PAGES_DIR = "../pages"
KINDLE_MY_CLIPPINGS = "My Clippings.txt"
KINDLE_FILE_NAME = "../pages/kindle.md"

# Constants for configuration
MIN_CONTENT_LENGTH = 5
SIMILARITY_THRESHOLD = 0.9
LENGTH_DIFFERENCE_THRESHOLD = 10


@dataclass
class KindleNote:
    """Data class for storing Kindle note information"""

    date: datetime
    content: str


def get_txt_file_path(file_name):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    kindle_directory = os.path.join(script_directory, "..", KINDLE_FILE_DIR)
    return os.path.join(kindle_directory, file_name)


def read_txt_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            content = file.read()
        if not content:
            return None
        return content
    except FileNotFoundError:
        pprint.pprint(f"Error: The file {file_path} does not exist.")
        return None
    except Exception as e:
        pprint.pprint(f"An error occurred while reading the file: {e}")
        return None


def get_content_fingerprint(content: str) -> str:
    """
    Generate a fingerprint for content comparison by:
    1. Removing all spaces and punctuation
    2. Converting to lowercase
    3. Finding the longest common content if possible
    """
    # Remove all spaces and punctuation, convert to lowercase
    cleaned = re.sub(r"[^\w\u4e00-\u9fff]", "", content).lower()

    # If the content is too short (less than 20 chars), use it as is
    if len(cleaned) < 20:
        return cleaned

    # For longer content, use a substring that's likely to be the core content
    # Start from index 10 to skip potential prefixes
    return cleaned[10:]


def clean_text(text: str) -> str:
    """Clean text by removing spaces, punctuation and converting to lowercase"""
    return re.sub(r"[^\w\u4e00-\u9fff]", "", text).lower()


def is_similar(text1: str, text2: str) -> bool:
    """Check if two texts are similar based on content"""
    clean1 = clean_text(text1)
    clean2 = clean_text(text2)

    # If one text contains the other
    if clean1 in clean2 or clean2 in clean1:
        return True

    # For similar length texts
    if abs(len(clean1) - len(clean2)) < LENGTH_DIFFERENCE_THRESHOLD:
        matching_chars = sum(
            1 for i in range(min(len(clean1), len(clean2))) if clean1[i] == clean2[i]
        )
        return matching_chars / max(len(clean1), len(clean2)) >= SIMILARITY_THRESHOLD

    return False


def process_content(raw_content: str) -> str:
    """Process raw content by handling quoted text and spaces"""

    def replace_quoted_content(match: re.Match) -> str:
        return f'"{re.sub(r"\s+", "", match.group(1))}"'

    content = re.sub(r'"([^"]+)"', replace_quoted_content, raw_content)
    return re.sub(r"\s+", "", content)


def parser_clippings_content(content: str) -> List[Dict[str, Any]]:
    """Parse and deduplicate Kindle clippings content"""
    content = content.replace("\ufeff", "").strip()

    note_pattern = re.compile(
        r"(?:^|\n==========\n)?\s*"
        r"(?P<title>[^()]+) \((?P<author>[^)]+)\)\n"
        r"- Your Highlight on Location (?P<location>\d+-\d+) \| "
        r"Added on (?P<date>[^\n]+)\n\n"
        r"(?P<content>.*?)(?=\n==========|\Z)",
        re.S | re.M,
    )

    # Collect notes by book
    books: Dict[Tuple[str, str], List[KindleNote]] = defaultdict(list)

    for match in note_pattern.finditer(content):
        try:
            title = re.sub(r"^=+\s*", "", match.group("title").strip())
            author = match.group("author").strip()
            date_obj = datetime.strptime(
                match.group("date").strip(), "%A, %B %d, %Y %I:%M:%S %p"
            )
            processed_content = process_content(match.group("content"))

            if len(processed_content) >= MIN_CONTENT_LENGTH:
                books[(title, author)].append(
                    KindleNote(date=date_obj, content=processed_content)
                )
        except ValueError:
            continue

    # Deduplicate and format output
    result = []
    for (title, author), notes in books.items():
        # Sort notes by date (newest first)
        sorted_notes = sorted(notes, key=lambda x: x.date, reverse=True)
        deduplicated = []

        for note in sorted_notes:
            if not any(is_similar(note.content, kept.content) for kept in deduplicated):
                deduplicated.append(note)

        result.append(
            {
                "title": title,
                "author": author,
                "notes": [
                    {
                        "date": note.date.strftime("%Y-%m-%d %H:%M:%S"),
                        "content": note.content,
                    }
                    for note in deduplicated
                ],
            }
        )

    return result


def write_book_index(structured_data: List[Dict[str, Any]], output_file: str) -> None:
    """
    Write book titles in markdown format with last updated time.
    Only writes new books that don't exist in the file.

    Format:
    - [[Book Title]] - last updated YYYY-MM-DD HH:MM:SS
    """
    try:
        # Read existing content
        existing_content = ""
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                existing_content = f.read()
        except FileNotFoundError:
            pass

        # Prepare new entries
        new_entries = []
        for book in structured_data:
            title = book["title"]
            # Get the most recent note's date
            if book["notes"]:
                last_updated = book["notes"][0][
                    "date"
                ]  # Notes are already sorted by date
                entry = f"- [[{title}]] - last updated {last_updated}"

                # Check if this book title doesn't exist in current content
                if f"[[{title}]]" not in existing_content:
                    new_entries.append(entry)

        # If we have new entries, append them to the file
        if new_entries:
            with open(output_file, "a", encoding="utf-8") as f:
                # Add a newline if file is not empty and doesn't end with one
                if existing_content and not existing_content.endswith("\n"):
                    f.write("\n")
                # Write new entries
                f.write("\n".join(new_entries) + "\n")
            print(f"Added {len(new_entries)} new book entries")
        else:
            print("No new books to add")

    except Exception as e:
        print(f"Error writing to file: {e}")


def write_book_notes(structured_data: List[Dict[str, Any]], pages_dir: str) -> None:
    """
    Write book notes to individual markdown files in the pages directory.
    Only append new notes that don't exist in the file.

    Format:
    - Book Title
    - Author
    -
    - YYYY-MM-DD HH:MM:SS: Note 1
    - YYYY-MM-DD HH:MM:SS: Note 2
    """
    try:
        os.makedirs(pages_dir, exist_ok=True)

        for book in structured_data:
            title = book["title"]
            filename = f"{title}.md"
            filepath = os.path.join(pages_dir, filename)

            # Read existing content if file exists
            existing_content = ""
            existing_notes = set()
            try:
                if os.path.exists(filepath):
                    with open(filepath, "r", encoding="utf-8") as f:
                        existing_content = f.read()
                    # Extract existing timestamps and notes
                    for line in existing_content.split("\n"):
                        if line.startswith("- 20"):  # Looking for timestamp pattern
                            existing_notes.add(line)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                continue

            # Filter out notes that already exist
            new_notes = []
            for note in book["notes"]:
                note_line = f"- {note['date']}: {note['content']}"
                if note_line not in existing_notes:
                    new_notes.append(note_line)

            if not new_notes:
                print(f"No new notes to add for {title}")
                continue

            # Prepare content
            if not existing_content:
                # Create new file with header
                content = [
                    f"- {title}",
                    f"- {book['author']}",
                    "- ",
                ]
                content.extend(new_notes)
                final_content = "\n".join(content)
            else:
                # Append new notes to existing content
                final_content = existing_content.rstrip() + "\n" + "\n".join(new_notes)

            # Write to file
            try:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(final_content + "\n")
                print(f"Added {len(new_notes)} new notes to {title}")
            except Exception as e:
                print(f"Error writing to {filename}: {e}")

    except Exception as e:
        print(f"Error processing books: {e}")


# Modify the main block to use the new function
if __name__ == "__main__":
    kindle_file = get_txt_file_path(KINDLE_FILE_NAME)
    kindle_my_clippings = get_txt_file_path(KINDLE_MY_CLIPPINGS)
    kindle_my_clippings_content = read_txt_file(kindle_my_clippings)

    if kindle_my_clippings_content:
        structured_data = parser_clippings_content(kindle_my_clippings_content)
        # Write book index
        write_book_index(structured_data, kindle_file)
        # Write individual book notes
        script_directory = os.path.dirname(os.path.abspath(__file__))
        pages_directory = os.path.join(script_directory, PAGES_DIR)
        write_book_notes(structured_data, pages_directory)
    else:
        print("No content found in My Clippings.txt")
