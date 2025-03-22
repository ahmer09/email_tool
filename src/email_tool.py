#email_tool/email_tool.py

import webbrowser
def create_and_show_email(to: str, subject: str, body: str):
    mailto_url = f"mailto:{to}?subject={subject}&body={body}"
    webbrowser.open(mailto_url, new=1)
    return None
