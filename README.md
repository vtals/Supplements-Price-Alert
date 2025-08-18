# Bulk Supplements Scraper & Price Alert

A Python project that scrapes prices of protein and creatine products from Bulk.com, stores the data in CSV files, updates the datasets automatically once a week, and sends Telegram notifications when prices fall below a set threshold. 

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
├── scheduler.py       # Main script with weekly scheduling
├── data/              # Folder containing CSV files
│   ├── bulk_protein_data.csv
│   └── bulk_creatine_data.csv
├── .gitignore
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
1. Create a `.env` file
2. Fill in your real values in `.env`:

```
BOT_TOKEN=your_bot_token
CHAT_ID=your_chat_id
```


## **How to Run**
1. Ensure the initial CSVs are present in the `data/` folder.
2. Run the main script:

```bash
python scheduler.py
```

The script will automatically update datasets weekly and send Telegram notifications if necessary.

---

## **How It Works**
1. `scraper.py` scrapes product data from Bulk.com.
2. `updater.py` appends new data to existing CSVs.
3. `alert_bot.py` checks for prices below thresholds and sends Telegram messages.
4. `scheduler.py` schedules the weekly update and coordinates all functions.

---

## **Contributing**
Feel free to contribute via pull requests or report issues using GitHub Issues.

---

## **License**
MIT License
