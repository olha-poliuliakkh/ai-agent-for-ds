import io
import contextlib
import traceback

stdout_buffer = io.StringIO()
stderr_buffer = io.StringIO()

with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
    try:
        print(2 / 0)
    except Exception:
        traceback.print_exc()

# Отримуємо повне повідомлення про помилку
error_message = stderr_buffer.getvalue()

print(error_message)
