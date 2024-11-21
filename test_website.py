from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def end_to_end():
    # Use webdriver-manager to automatically handle the ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Step 1: Open Google
        driver.get('https://www.google.com')

        # Step 2: Locate the search box and enter the search term
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("https://quantumlevitation.com/")  # Search for the specific URL or page
        search_box.send_keys(Keys.RETURN)  # Press Enter to start the search

        # Step 3: Wait for the results to load
        try:
            # Wait for the results to be visible (the first result might be a bit tricky)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "search"))  # Wait until the search results container is loaded
            )

            # Print all the link texts to debug what is available on the page
            search_results = driver.find_elements(By.CSS_SELECTOR, 'h3')  # Most links are inside <h3> tags in Google search
            for result in search_results:
                print(result.text)  # Debugging: Print out each result's text

            # Step 4: Locate and click the link containing the desired text
            try:
                link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Quantum Levitation: Home"))
                )
                link.click()  # Click on the link to open the page directly
            except Exception as e:
                print(f"Error: Unable to find or click the link with partial text: 'superconductivity kit'. {e}")
                driver.quit()

        except Exception as e:
            print(f"Error: Google search results did not load properly: {e}")
            driver.quit()

        # Step 5: Wait for the page to load completely (you can customize this to wait for specific elements)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))  # Example: Wait for an <h1> element on the new page
            )
        except Exception as e:
            print(f"Error: Page did not load as expected: {e}")
            driver.quit()

        # Step 6: Print the title of the page to confirm you're on the correct page
        print(driver.title)

    finally:
        # Close the browser
        driver.quit()
