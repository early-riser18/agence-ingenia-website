from jinja2 import Environment, FileSystemLoader
import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

# Run from base dir.
env = Environment(loader=FileSystemLoader("src"))
pages = ["templates/index.html"]

output_dir = "."
os.makedirs(output_dir, exist_ok=True)

output_page = "index.html"


def build_page():
    for page in pages:
        template = env.get_template(page)
        html = template.render()
        with open(output_page, "w", encoding="utf-8") as f:
            f.write(html)

    print(f"Site built in {output_page}")


class BuildEventHandler(FileSystemEventHandler):
    """Handles file system events and triggers page rebuild."""

    def should_rebuild(self, file_path):
        """Check if the file change should trigger a rebuild."""
        # Get the filename from the path
        filename = os.path.basename(file_path)

        # Skip if it's the output file to prevent infinite loops
        if filename == output_page:
            return False

        return True

    def on_modified(self, event):
        if not event.is_directory and self.should_rebuild(event.src_path):
            print(f"File {event.src_path} was modified. Rebuilding...")
            build_page()

    def on_created(self, event):
        if not event.is_directory and self.should_rebuild(event.src_path):
            print(f"File {event.src_path} was created. Rebuilding...")
            build_page()

    def on_deleted(self, event):
        if not event.is_directory and self.should_rebuild(event.src_path):
            print(f"File {event.src_path} was deleted. Rebuilding...")
            build_page()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # Initial build
    print("Building initial page...")
    build_page()

    path = sys.argv[1] if len(sys.argv) > 1 else "."
    event_handler = BuildEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"Watching for changes in {path}... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
