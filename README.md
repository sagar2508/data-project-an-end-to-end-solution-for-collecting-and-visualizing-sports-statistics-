# Cricket Records Data Pipeline & Power BI Dashboard

**Project:** Cricket Records Automation and Visualization

**Files included:**

* `cricket recodrs.py` — Selenium automation script for data extraction
* `Cricket Record.pbix` — Power BI dashboard for visualization

---

## About

The **Cricket Records Project** is an end-to-end data engineering and analytics pipeline built using **Selenium**, **Azure Data Factory (ADF)**, and **Power BI**. The pipeline automates data collection from ESPN CricInfo, processes the extracted data, and visualizes key cricket statistics such as most runs, batting averages, and performance trends.

---

## Architecture Overview

```
Selenium (Python) → Data Extraction  →  Azure Data Factory → Data Storage  →  Power BI Dashboard
```

### Workflow Summary

1. **Selenium Automation (Python Script)**

   * The `cricket recodrs.py` script uses Selenium to scrape player statistics from [ESPN CricInfo](https://www.espncricinfo.com/records).
   * Extracts top batting records and saves them into `.txt` and `.xlsx` formats.
   * The data includes: Player, Matches, Innings, Runs, Average, Strike Rate, 100s, 50s, 4s, and 6s.

2. **Azure Data Factory (ADF)**

   * ADF pipelines automate the **data ingestion** from the local Excel or cloud blob storage.
   * Data transformations and dataflows clean and prepare the dataset for analytics.
   * The final curated dataset is stored in **Azure SQL Database** or **Data Lake** for Power BI.

3. **Power BI Dashboard**

   * The Power BI file `Cricket Record.pbix` visualizes the final dataset.
   * Interactive visuals show:

     * Top Run Scorers
     * Player performance trends
     * Comparative stats between eras or teams
     * Key KPIs (average, strike rate, total runs)

---

## Technologies Used

| Layer              | Technology                     |
| ------------------ | ------------------------------ |
| Data Extraction    | Python, Selenium, WebDriver    |
| Data Processing    | Azure Data Factory             |
| Data Storage       | Azure SQL Database / Data Lake |
| Data Visualization | Power BI                       |

---

## Folder Structure

```
/ (root)
├─ cricket recodrs.py             # Web scraping script
├─ Cricket Record.pbix            # Power BI visualization
├─ data/                          # (optional) extracted Excel/Text data
├─ docs/                          # screenshots, data dictionary, ADF pipeline diagrams
└─ README.md                      # this file
```

---

## Selenium Script Details

**File:** `cricket recodrs.py`

### Key Steps:

1. Opens ESPN CricInfo records page.
2. Navigates to the "Batting Records" → "Most Runs" section.
3. Scrapes the data table and writes it to a text file.
4. Converts the text file into a structured Excel file using **pandas**.

### Output Columns:

* Player | Span | Matches | Innings | Not Outs | Runs | Highest Score | Average | Balls Faced | Strike Rate | 100s | 50s | 0s | 4s | 6s

---

## Azure Data Factory Integration

The ADF pipeline performs the following tasks:

* **Ingest:** Reads the Excel output from local storage or Azure Blob.
* **Transform:** Cleans, filters, and normalizes the data for consistency.
* **Load:** Writes cleaned data to **Azure SQL Database** or **Data Lake Gen2**.
* **Trigger:** Scheduled trigger to automate daily or weekly data refreshes.

ADF also supports **data lineage tracking** and **error monitoring** through pipeline logs.

---

## Power BI Dashboard Overview

**File:** `Cricket Record.pbix`

### Key Visuals

* Top 10 Run Scorers
* Average & Strike Rate by Player
* Career Span vs. Total Runs
* Distribution of Centuries and Fifties
* KPI Cards (Total Runs, Average, Matches, Innings)

### Filters & Interactivity

* Time Range (Career Span)
* Player Search
* Country Filter
* Match Type Filter (Test / ODI / T20)

---

## Setup Instructions

### 1. Run Selenium Script

```bash
python cricket recodrs.py
```

The script will generate two files in the working directory:

* `test_cricket_records.txt`
* `test_cricket_records.xlsx`

### 2. Load Data into Azure

* Upload `test_cricket_records.xlsx` to your **Azure Blob Storage**.
* Use **ADF Copy Activity** to load data into Azure SQL / Data Lake.

### 3. Connect Power BI

* Open `Cricket Record.pbix` in Power BI Desktop.
* Update **Data Source Settings** to point to your Azure SQL / Data Lake.
* Click **Refresh** to pull latest data.

---

## Troubleshooting

| Issue                     | Cause                     | Solution                                  |
| ------------------------- | ------------------------- | ----------------------------------------- |
| Selenium crashes          | ChromeDriver mismatch     | Update ChromeDriver path/version          |
| Blank visuals in Power BI | Data source not connected | Reconnect to Azure or local Excel         |
| Slow refresh              | Large dataset             | Use aggregations or optimize ADF dataflow |

---

## Future Enhancements

* Add **Bowling Records** scraping feature.
* Integrate **Azure Synapse** for advanced analytics.
* Include **Power BI Service refresh schedule** using ADF triggers.
* Build a **web-based dashboard** with real-time updates.

---

## License

Include your preferred open-source license (e.g., MIT License) in a `LICENSE` file.

---



---

## Version History

* **v1.0** — Initial version integrating Selenium, ADF, and Power BI.

---

> Need enhancements? I can include a visual ADF pipeline diagram, DAX formula documentation, or sample outputs from Selenium scraping for your GitHub README.
