with open('demo_log.log', 'r') as file:
    for line in file:
        if "error" in line:
            with open ('error.log', 'a') as f:
                 f.write(line)
        elif "info" in line:
                with open('info.log', 'a') as f:
                    f.write(line)