# Bulk Supplements Scraper & Price Alert

A Python project that scrapes prices of protein and creatine products from Bulk.com, creates or stores the data in CSV files, updates the datasets automatically once a week, and sends Telegram notifications when prices fall below a set threshold. 

---

## **Background**
I love gym and I'm used to buy supplements on Bulk.com. One day I noticed an absurd price error: strawberry vegan protein powder price was 0.00 EUR. That's what made me think about this project and now I've done it. I'm not a computer scientist (as you can imagine), I'm a statistics student with a programming passion, but I thought this could be an interesting project to enhance my python skills. Of course this project isn't perfect and I probably made some mistake, but I believe this is a good starting point to become familiar with Github and programming in general!

---

## **Features**
- Automatic extraction of product data (flavour, weight, price, discounted price, currency)
- Saves data into two separate CSVs (`bulk_protein_data.csv` and `bulk_creatine_data.csv`)
- Weekly automatic dataset updates
- Telegram notifications for prices below defined thresholds
- Modular project structure, easy to extend

---

## **Project Structure**
```
project/
│
├── config.py          # General configuration variables
├── scraper.py         # Functions to scrape data from Bulk.com
├── updater.py         # Functions to update datasets
├── alert_bot.py       # Telegram and price alert functions
├── main.py            # Main script with optional weekly scheduling
├── data/              # Folder containing CSV files
│   ├── bulk_protein_data.csv
│   └── bulk_creatine_data.csv
├── .gitignore
├── requirements.txt
├── example.env        # Example file for required data
└── README.md
```

---

## **Prerequisites**
- Python 3.10+
- Required libraries: `requests`, `beautifulsoup4`, `pandas`, `python-dotenv`, `schedule`

Install the dependencies with:

```bash
pip install -r requirements.txt
```

---

## **Configuration**
1. Fill in your real values in `example.env`:

```
BOT_TOKEN=your_bot_token
CHAT_ID=your_chat_id
```


## **How to Run**
1. Run the main script:

```bash
python main.py
```

The script will automatically create or update datasets weekly and send Telegram notifications if necessary.

---

## **How It Works**
1. `scraper.py` scrapes product data from Bulk.com.
2. `main.py` appends new data to existing CSVs or creates new CSV's.
3. `alert_bot.py` checks for prices below thresholds and sends Telegram messages.
4. `scheduler.py` schedules the weekly update and coordinates all functions.

---

## **Contributing**
Feel free to contribute via pull requests or report issues using GitHub Issues.

---

## **License**
MIT License
