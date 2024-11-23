from google_play_scraper import reviews, Sort
import pandas as pd
import time

# Package name of Namma Yatri
app_id = 'in.juspay.nammayatri'

# Function to fetch all reviews
def fetch_all_reviews(app_id, lang='en', country='in', count=100):
    all_reviews = []
    continuation_token = None
    total_reviews_fetched = 0

    try:
        while True:
            result, continuation_token = reviews(
                app_id,
                lang=lang,
                country=country,
                sort=Sort.NEWEST,
                count=count,
                continuation_token=continuation_token
            )
            all_reviews.extend(result)
            total_reviews_fetched += len(result)
            print(f"Fetched {total_reviews_fetched} reviews so far...")

            # If there is no continuation token, we have fetched all reviews
            if not continuation_token:
                break
            
            # Optional: Add a short delay to avoid overloading the server
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProcess interrupted! Saving the reviews fetched so far...")

    return all_reviews

# Fetch all reviews
reviews_data = fetch_all_reviews(app_id)

# Convert to DataFrame
reviews_df = pd.DataFrame(reviews_data)

# Display the first few rows
print(reviews_df.head())

# Save to CSV
reviews_df.to_csv('namma_yatri_all_reviews.csv', index=False)
