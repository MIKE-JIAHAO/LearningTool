# modules/error_feedback.py
import ast
import io
import contextlib

def analyze_code(code):
    try:
        ast.parse(code)
        return {"status": "success", "message": "No syntax errors detected."}
    except SyntaxError as e:
        return {"status": "error", "message": f"Syntax Error: {e}"}
    except Exception as e:
        return {"status": "error", "message": f"Unknown Error: {e}"}

def run_code(code):
    try:
        exec_output = io.StringIO()
        with contextlib.redirect_stdout(exec_output):
            exec(code, {})
        return exec_output.getvalue()
    except Exception as e:
        return f"Runtime Error: {e}"
