from llama_index.core.tools import FunctionTool
import os


def code_reader_func(fn):
    path = os.path.join("data", fn)
    try:
        with open(path, "r") as f:
            content = f.read()
            return {"file content": content}

    except Exception as e:
        return {"error": str(e)}


code_reader = FunctionTool.from_defaults(
    fn=code_reader_func,
    name="code_reader",
    description="""
        this tool can read the contents of code files and return 
    their results. Use this when you need to read the contents of a file
    """
)
