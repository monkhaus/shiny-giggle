import subprocess

text = "This text should be strikethrough"
strikethrough_script_path = "./strikethrough.sh"

formatted_text = subprocess.run([strikethrough_script_path, text], capture_output=True, text=True).stdout.strip()

print(formatted_text)
