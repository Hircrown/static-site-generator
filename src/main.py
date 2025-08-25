from textnode import TextType, TextNode

def main():
    text_node = TextNode(
        "Go to google.com", TextType.LINK, "http://google.com"
    )
    print(text_node)

if __name__ == "__main__":
    main()