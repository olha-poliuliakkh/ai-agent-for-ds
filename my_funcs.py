import prompts as pr
import calling_gpt as cg
import sys
import io
import openai as op
import contextlib


def classify_task(req) :
    if req == 1:
        model_to_use = "Support Vector Machines"
    elif req == 2:
        model_to_use = "Linear Regression"
    else:
        model_to_use = "Random Forest"
    
    return model_to_use



def generate_cod (sys_prompt, us_prompt, d_set=None):
    error_log = []

    while True and len(error_log) <= 10:
        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()
        with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
            try:
                response = cg.resp(sys_prompt, us_prompt)
                print(response.choices[0].message.content.strip())

                generated_code = response.choices[0].message.content.strip()
                if isinstance(d_set, str) and d_set in globals():
                    lines = generated_code.split("\n")
                    for i in range(len(lines)):
                        if "df =" in lines[i]:
                            lines[i] = f"df = {d_set}"  # тут уже не рядок, а доступ до змінної
                    generated_code = "\n".join(lines)
                exec(generated_code)
                break

            except Exception as e:
                us_prompt += " Check the mistake you made last time: "
                error_message = f"Error: {e}"
                error_log.append(error_message)
                i = len(error_log) - 1 
                if i > 0: 
                    us_prompt = us_prompt.replace(error_log[i-1], " ") 
                us_prompt += error_log[i]
            finally:
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__

    output_result = stdout_buffer.getvalue()
    print(generated_code)
    print(output_result)