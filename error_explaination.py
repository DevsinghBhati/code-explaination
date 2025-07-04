import subprocess

def ask_ollama(prompt, model="mistral"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output = result.stdout.decode()
        return output
    except Exception as e:
        return f"Error: {e}"

def explain_code(code_text):
    prompt = f"""You are a code explainer AI. Please explain the following Python code line by line in simple terms:"""
    return ask_ollama(prompt)


print("HERE IS YOUR CODE'S EXPLAINATION ")
ASK = input("DO YOU WANT ME TO EXPLAIN YOUR FULL CODE :").lower().split()
code = ""
for i in ASK :
    if i in [ 'yes' , 'y']:
        check = int(input("ENTER (1) YOU WANT TO WRIte code or (2) you want to add from file : "))
        if check == 1 :
            print("Paste your Python code (end with empty line):")
            lines = []
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
            code = "\n".join(lines)
        elif check == 2:
            path = input("ENTER THE PATH OF YOUR CODE (.py):")
            with open (path,'r') as f:
                code = f.read()
        else:
            print("INVALID choice !")

print("ExPLAINING :: \n")
expaination = explain_code(code)
print(expaination)