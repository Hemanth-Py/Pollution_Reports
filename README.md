# Pollution Reports

Python scripts for generating city-wise and pollutant-wise air quality reports for India from XLSX data.

---

## What It Does

- Reads air quality data from `AirQuality-India-Realtime.xlsx`
- Groups and aggregates pollution entries by city and by pollutant type
- Generates two PDF reports:
  - `CityWiseReport.pdf` — Avg/Max/Min pollution per city
  - `PollutantWiseReport.pdf` — Avg/Max/Min per pollutant type across states
- Connects to RDS MySQL for additional data queries

---

## Tech Stack

- Python 3
- pandas / openpyxl — XLSX data processing
- reportlab — PDF generation
- MySQL (AWS RDS) — optional database queries

---

## Setup

```bash
git clone https://github.com/Hemanth-Py/Pollution_Reports.git
cd Pollution_Reports

pip install -r requirements.txt

cp .env.example .env
# Edit .env with your RDS credentials if using database queries
```

---

## Usage

### Generate PDF Reports

```bash
python pollution_report.py
```

Outputs `CityWiseReport.pdf` and `PollutantWiseReport.pdf` in the project root.

### Run RDS Queries

```bash
python rds_connecctor.py
```

Requires `.env` with valid RDS credentials.

---

## Environment Variables

```bash
RDS_HOST=your-rds-endpoint.rds.amazonaws.com
RDS_USERNAME=admin
RDS_PASSWORD=your-password
RDS_PORT=3306
```

---

**Built with:** Python · pandas · reportlab · AWS RDS
