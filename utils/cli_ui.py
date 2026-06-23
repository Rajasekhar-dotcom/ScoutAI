import inspect

def welcome() -> str:
    welcome_message = inspect.cleandoc("""
==================================================

🚀 Scout AI

Your AI Mentor for:

• Startup Ideas
• Market Analysis
• Revenue Models
• Competitor Research
• MVP Planning
• Growth Strategies

Commands:

• exit/quit  - Exit the application

==================================================
""")
    
    return welcome_message
    
def main():
    print(welcome())

if __name__ == "__main__":
    main()