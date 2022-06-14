import runpy
from pathlib import Path

from . import web

root: str = '/'


def set_root(root_: str):
    global root

    root = root_


def generate_links(dest: str):
    main = Path(__import__("__main__").__file__)
    bridge = Path(__file__).with_name("bridge.php")
    bridge_text = bridge.read_text().replace('@script_path@', str(main.resolve())) \
                                    .replace('@phpton_dir@', str(bridge.parent.parent.resolve()))
    # copied_bridge = Path(dest) / "phpton.php"
    # copied_bridge.write_text(bridge_text)
    for route in web.ROUTES:
        if route.endswith('/'):
            route += 'index.php'
        if route.startswith('/'):
            route = route[1:]
        if not route.endswith('php'):
            route += '.php'
        target = Path(dest) / route
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(bridge_text)


load = runpy.run_path


def run(path: str):
    if path.startswith(root):
        path = path[len(root):]
        path = '/' + path
    parts = path.split('?')
    web.ROUTES[parts[0]]()
