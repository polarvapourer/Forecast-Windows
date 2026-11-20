# Forecast Windows

[Download Forecast Windows for Windows](https://github.com/polarvapourer/Forecast-Windows/releases/latest/download/ForecastWindows.exe)

Does a longer shopping history give a better sales forecast? This Python
experiment compares two predictions for each customer: one based on their
previous 8 weeks of purchases and one based on their previous 16 weeks.

## How it works

The program creates a year of weekly sales for three fictional customers:
a weekly shopper, an occasional shopper and someone who buys more in autumn.

Each forecast uses the customer's average weekly purchases before the test
date. Both forecasts are scored on the same customers in the same week.
The score is the mean absolute error: the average number of items each
prediction missed by. Lower is better.

## Results

| Forecast week | More accurate forecast |
|---|---|
| 5 May 2025 | 16 weeks |
| 3 November 2025 | 8 weeks |

The autumn shopper explains the November result. They bought 4 items that
week. The 8-week forecast predicted 4, while the 16-week forecast predicted
2.69 because it included quieter summer weeks. These results come from the
fictional shopping patterns in the script.

## Run it

**Windows executable:** Open the [latest release](https://github.com/polarvapourer/Forecast-Windows/releases/latest), expand **Assets**, and download `ForecastWindows.exe`. Double-click it to run the forecast comparison.

**Python source:** Download `Forecast_Windows.py`, open PowerShell in the
folder containing it, and run:

```powershell
py Forecast_Windows.py
```

The script uses only Python's standard library.

## Research inspiration

Sowrirajan, T. and Wang, Y. (2026), [The Window Lever](https://arxiv.org/abs/2611.26521).
The project adapts the paper's idea of testing different history lengths
on the same customers and forecast dates.
