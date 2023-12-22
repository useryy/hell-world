if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the main text from the webpage (adjust the tag/class/ID to match the actual structure of the page)
    main_text = soup.find('div', {'class': 'your-class-name'}).get_text()
