def build_style(*styles):
    out = '@import url("widgets/block.css");'
    out += '@import url("widgets/menu.css");'
    out += '@import url("widgets/drop.css");'
    out += '@import url("widgets/shadow.css");'
    out += "body { margin: 0; padding: 0; height: 100%; width: 100%; }"
    out += "".join(str(style) for style in styles)
    return out


def build_body(filename):
    with open(filename, "r", encoding="utf8") as file:
        data = file.read()
    return data


def build_template(title: str, style: str, body: str):
    with open("template.uweb", "r", encoding="utf8") as file:
        template = file.read()
    kwargs = {"title": title, "style": style, "body": body}
    return template.format(**kwargs)


__all__ = ["build_style", "build_body", "build_template"]
