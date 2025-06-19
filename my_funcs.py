import prompts as pr
import calling_gpt as cg
import sys
import io
import openai as op
import contextlib
import traceback


def classify_task(req) :
    if req == 1:
        model_to_use = "Support Vector Machines"
    else:
        model_to_use = "Linear Regression"
    # else:
    #     model_to_use = "Random Forest"
    
    return model_to_use



def generate_code(sys_prompt, us_prompt, d_set_name, d_set):
    error_log = []
    temp = us_prompt 

    while True and len(error_log) <= 10:
        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()
        with contextlib.redirect_stdout(stdout_buffer), contextlib.redirect_stderr(stderr_buffer):
            try:
                response = cg.resp(sys_prompt, us_prompt)
                print(response.choices[0].message.content.strip())
                generated_code = response.choices[0].message.content.strip()
                lines = generated_code.split("\n")
                lines.insert(10, f"df = {d_set_name}")
                generated_code = "\n".join(lines)
                exec_globals = {d_set_name: d_set}
                exec_globals = {
                    d_set_name: d_set,
                    "df": d_set
                }
                exec(generated_code, exec_globals)
                return generated_code, stdout_buffer.getvalue()
                

            except Exception:
                traceback.print_exc()
                error_message = stderr_buffer.getvalue()
                print(error_message)
                text_for_prompt = " Your code {code} caused an {error}. Fix it and generate the whole code again. You can also check out previous errors {list} to avoid them in future"
                us_prompt = temp + text_for_prompt.format(code = generated_code, error = error_message, list =  error_log)
                error_log.append(error_message)

                # i = len(error_log) - 1 
                # if i > 0: 
                #     us_prompt = us_prompt.replace(error_log[i-1], " ") 
                # us_prompt += error_log[i]
            # finally:  
            #     sys.stdout = sys.__stdout__
            #     sys.stderr = sys.__stderr__

    return None, f"Failed after {len(error_log)} attempts.\nErrors:\n{''.join(error_log)}"