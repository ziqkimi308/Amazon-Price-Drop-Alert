# Amazon Price Drop Alert

- This project scrapes product price data from Amazon using BeautifulSoup. If the price of a specific item drops below a predefined threshold, an email is automatically sent to notify the user. This can help track deals and discounts for items on Amazon.

---

### Features:

- Price Monitoring: Automatically tracks the price of an Amazon product.
- Email Alerts: Sends an email notification when the price drops below your specified limit.
- Customizable: Easily change the Amazon product URL and price limit for your preferences.
- User-Friendly Setup: Simple to configure with minimal dependencies.

---

### How It Works:
- The script scrapes the Amazon product page to get the title and price.
- If the price drops below your set threshold (PRICE_LIMIT), an email is sent to the target address with the product details and link.
- You can customize the product link, price limit, and email details for different monitoring.

---

### Dependencies:
- Requests: To fetch the webpage data from Amazon.
- BeautifulSoup4: For parsing the HTML content and extracting relevant information.
- LXML: Used by BeautifulSoup to parse HTML quickly.
- SMTP: For sending email notifications through Gmail’s SMTP service.

---

### Screenshots:

<img width="1031" alt="image" src="https://github.com/user-attachments/assets/f62d4455-dbb1-4467-be5b-3b1e05754088" />
