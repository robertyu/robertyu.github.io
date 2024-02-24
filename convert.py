import os
import markdown
from bs4 import BeautifulSoup

def convert_md_to_html(md_file_path):
    # Configure Markdown to HTML conversion with code syntax highlighting
    md_extensions = ['codehilite']
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    html_content = markdown.markdown(md_content, extensions=md_extensions)
    soup = BeautifulSoup(html_content, 'html.parser')
    pretty_html = soup.prettify()
    return pretty_html

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
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def main(root_path, readme_path):
    markdown_files = find_markdown_files(root_path)
    links = []

    for md_file in markdown_files:
        html_content = convert_md_to_html(md_file)
        output_file = md_file.replace('.md', '.html')
        save_html(html_content, output_file)
        file_title = os.path.basename(md_file)[:-3]
        file_url = output_file
        links.append({'title': file_title, 'url': file_url})

    add_links_to_readme(readme_path, links)
    print("Conversion complete. README updated with links to HTML files.")

if __name__ == "__main__":
    root_path = '.'  # Set to your Markdown files' root directory
    readme_path = 'README.md'  # Path to your README file
    main(root_path, readme_path)
