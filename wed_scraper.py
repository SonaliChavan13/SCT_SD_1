import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/catalogue/page-1.html"

def scrape_products():
    try:
        status_label.config(text="Scraping data... Please wait ⏳")

        response = requests.get(URL, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        products = soup.find_all("article", class_="product_pod")

        with open("products.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Product Name", "Price", "Rating"])

            for product in products:
                name = product.h3.a["title"]
                price = product.find("p", class_="price_color").text
                rating = product.find("p", class_="star-rating")["class"][1]

                writer.writerow([name, price, rating])

        status_label.config(text="✅ Data saved to products.csv")
        messagebox.showinfo("Success", "Product data extracted and saved successfully!")

    except Exception as e:
        status_label.config(text="❌ Error occurred")
        messagebox.showerror("Error", str(e))


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("E-commerce Product Scraper")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(
    root,
    text="🛒 Product Data Scraper",
    font=("Arial", 18, "bold")
).pack(pady=15)

tk.Label(
    root,
    text="Extract product name, price & rating\nfrom an e-commerce website",
    font=("Arial", 11),
    justify="center"
).pack(pady=10)

tk.Button(
    root,
    text="Scrape Products",
    command=scrape_products,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    width=18
).pack(pady=20)

status_label = tk.Label(root, text="", font=("Arial", 11))
status_label.pack(pady=10)

root.mainloop()
