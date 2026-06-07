def optimize_prompt(user_input):
    """
    A utility to structure user input into a better prompt for Manus.
    """
    system_instruction = "You are Manus, an autonomous general AI agent. "
    structured_prompt = f"{system_instruction}\n\nUser Goal: {user_input}\n\nPlease break this down into steps and execute them autonomously."
    return structured_prompt

if __name__ == "__main__":
    raw_input = "Build a website for my coffee shop"
    optimized = optimize_prompt(raw_input)
    print("--- Optimized Prompt for Manus ---")
    print(optimized)

# Custom template support added.