def clean_text(text):
    lines = text.split("\n")
    usable_lines = []
    for line in lines:
        if "Advertisement" in line and len(line) < 150: # Short "Advertisement Article continues below" line
            continue
        if "newsletter" in line.lower(): # "Sign up for our newsletter" spam
            continue
        if "<|endoftext|>" in line.lower(): # Model detects end of text
            line = line.split("<|endoftext|>")[0]
            usable_lines.append(line.strip())
            break
        if len(line.strip()) == 0: # no text; just a linebreak
            continue
            # line separation will be re-added on rendering later
        usable_lines.append(line.strip())
    last_line = usable_lines[-1].strip()
    if not (last_line.endswith(".") or last_line.endswith("!") or last_line.endswith("\"")): # end is not a full sentence
        usable_lines.remove(last_line)
    return "\n\n".join(usable_lines)