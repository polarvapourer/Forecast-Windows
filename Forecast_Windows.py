# @Author: Ibrahim Bashir
# @Date: 20 November 2026
# @Version: 1.0.0
# This program compares how well 8 and 16 weeks of sales history predict each customer's weekly purchases in spring and autumn.

from datetime import date, timedelta
from statistics import mean


WEEK = timedelta(weeks=1)
START_DATE = date(2025, 1, 6)  # A Monday. Each record represents one full week.

# Choose the test dates before looking at the results.
FORECAST_DATES = [
    date(2025, 5, 5),   # Spring
    date(2025, 11, 3),  # Autumn
]


def create_sales_history():
    """Create 52 weeks of fictional sales for three customers."""
    sales = {
        "Weekly": {},
        "Occasional": {},
        "Autumn regular": {},
    }

    for week_number in range(52):
        monday = START_DATE + week_number * WEEK

        # This customer gives us an easy check. Both forecasts should predict 2.
        sales["Weekly"][monday] = 2

        # The remainder is zero in weeks 0, 12, 24, and so on.
        if week_number % 12 == 0:
            sales["Occasional"][monday] = 6
        else:
            # A zero records a known week without a purchase.
            sales["Occasional"][monday] = 0

        if monday.month in (9, 10, 11):
            sales["Autumn regular"][monday] = 4
        else:
            sales["Autumn regular"][monday] = 1

    return sales


def predict_sales(history, forecast_date, weeks_back):
    """Predict one customer's weekly sales from their recent weekly average."""
    past_sales = []

    # Offset 1 is last week. Offset 0 would reveal the week we're predicting.
    for offset in range(1, weeks_back + 1):
        past_monday = forecast_date - offset * WEEK
        past_sales.append(history[past_monday])

    return mean(past_sales)


def compare_forecasts(sales, forecast_date):
    """Compare both history lengths for the same customers on one date."""
    errors_8 = []
    errors_16 = []

    print(f"\nWeek beginning {forecast_date:%d %B %Y}")
    print(f"{'Customer':<16} {'8 weeks':>9} {'16 weeks':>9} {'Actual':>8}")

    for customer, history in sales.items():
        prediction_8 = predict_sales(history, forecast_date, 8)
        prediction_16 = predict_sales(history, forecast_date, 16)

        # Look up the actual sales only after making both predictions.
        actual = history[forecast_date]

        # abs() counts a miss of 2 items the same in either direction.
        errors_8.append(abs(prediction_8 - actual))
        errors_16.append(abs(prediction_16 - actual))

        # Round for display only. The error calculation uses the full values.
        print(f"{customer:<16} {prediction_8:>9.2f} "
              f"{prediction_16:>9.2f} {actual:>8}")

    mae_8 = mean(errors_8)
    mae_16 = mean(errors_16)

    print(f"\n8-week mean absolute error:  {mae_8:.3f} items per customer")
    print(f"16-week mean absolute error: {mae_16:.3f} items per customer")

    if mae_8 < mae_16:
        print("The 8-week forecast was more accurate on this date.")
    elif mae_16 < mae_8:
        print("The 16-week forecast was more accurate on this date.")
    else:
        print("Both forecasts had the same average error on this date.")


def main():
    # Build the history once so both experiments use the same sales records.
    sales = create_sales_history()

    for forecast_date in FORECAST_DATES:
        compare_forecasts(sales, forecast_date)


# Start the experiment when this file is run directly.
if __name__ == "__main__":
    main()
    input("\nPress Enter to close...")





