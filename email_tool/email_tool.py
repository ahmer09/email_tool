#email_tool.py

import webbrowser
def create_and_show_email(to: str, subject: str, body: str):
    mailto_url = f"mailto:{to}?subject={subject}&body={body}"
    webbrowser.open(mailto_url, new=1)
    return None


if __name__ == '__main__':
    create_and_show_email('4u.ahmer@gmail.com', 'test', 'test')