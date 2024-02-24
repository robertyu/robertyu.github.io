import os
import markdown
from datetime import datetime
from bs4 import BeautifulSoup
from pygments.formatters import HtmlFormatter


def convert_md_to_html(md_file_path, css_style='monokai'):
    # Load Markdown content
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML with syntax highlighting
    html_content = markdown.markdown(md_content, extensions=['codehilite'])

    # Generate CSS for the chosen Pygments style
    formatter = HtmlFormatter(style=css_style)
    css_content = formatter.get_style_defs('.codehilite')

    # Wrap the content in HTML tags, including the Pygments CSS in a <style> tag
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{os.path.basename(md_file_path).replace('.md', '')}</title>
        <style>{css_content}</style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    return html_template


def save_html(html_content, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)


def add_links_to_readme(readme_path, links):
    with open(readme_path, 'a', encoding='utf-8') as readme_file:
        for link in links:
            readme_file.write(f"- [{link['title']}]({link['url']})\n")


def find_markdown_files(root_path):
    markdown_files = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith(".md") and not file.startswith('README'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files


def rewrite_readme_with_links(readme_path, links, header="## Generated HTML Links\n"):
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        readme_file.write(header)
        for link in links:
            readme_file.write(f"- [{link['title']}]({link['url']})\n")


def main(root_path, readme_path):
    markdown_files = find_markdown_files(root_path)
    print(markdown_files)
    
    # Sort files by datetime (year and month) in descending order
    sorted_files = sorted(markdown_files, key=lambda x: datetime.strptime(x.split('.')[-3] + '.' + x.split('.')[-2], '%Y.%m'), reverse=True)

    links = []

    for md_file in sorted_files:
        html_content = convert_md_to_html(md_file)
        output_file = md_file.replace('.md', '.html')
        save_html(html_content, output_file)
        file_title = os.path.basename(md_file)[:-3]
        file_url = output_file
        links.append({'title': file_title, 'url': file_url})

    # Clear and rewrite README with sorted links
    rewrite_readme_with_links(readme_path, links)
    print("Conversion complete. README updated with links to HTML files.")


if __name__ == "__main__":
    root_path = '.'  # Set to your Markdown files' root directory
    readme_path = 'README.md'  # Path to your README file
    main(root_path, readme_path)

