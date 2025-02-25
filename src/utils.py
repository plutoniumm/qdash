from logging import info, warning, error


def CSS(file: str) -> str:
    if not file.endswith(".css"):
        raise ValueError("Only CSS files are allowed")

    with open("assets/" + file, "r") as f:
        return f.read()


def JS(file: str) -> str:
    valid = [".js", ".mjs", ".cjs", ".ts"]
    if not any(file.endswith(ext) for ext in valid):
        raise ValueError("Only JS files are allowed")

    with open("assets/" + file, "r") as f:
        return f.read()


def GA(id: str) -> str:
    head = f"""
    <script async src="https://www.googletagmanager.com/gtag/js?id={id}"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{id}');
    </script>
    """

    return head


def Event(msg: str, typ: str = "INFO", trace: str = "") -> str:
    typ = typ.upper()
    if typ not in ["INFO", "WARN", "ERR"]:
        raise ValueError("Invalid event type")

    msg = f'{typ} {trace} "{msg}"'
    if typ == "INFO":
        info(msg)
    elif typ == "WARN":
        warning(msg)
    else:
        error(msg)
