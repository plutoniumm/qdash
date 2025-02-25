def CSS(file: str) -> str:
    if not file.endswith(".css"):
        raise ValueError("Only CSS files are allowed")

    with open(file, "r") as f:
        return f.read()

def JS(file: str) -> str:
    valid = [".js", ".mjs", ".cjs", ".ts"]
    if not any(file.endswith(ext) for ext in valid):
        raise ValueError("Only JS files are allowed")

    with open(file, "r") as f:
        return f.read()

def GA(id: str) -> str
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