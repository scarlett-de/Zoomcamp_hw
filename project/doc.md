1. Price Distribution Analysis
Graph: Boxplot or Violin Plot
Purpose: Compare pricing disparities across neighborhoods/room types.
Example:

Y-axis: Price

X-axis: neighbourhood_group (Brooklyn, Manhattan, etc.) or room_type
Insight: Identify outliers (e.g., ultra-luxury listings) and median prices (e.g., Manhattan is costlier than Brooklyn).

2. Occupancy vs. Price
Graph: Scatter Plot
Purpose: Check if higher prices correlate with lower occupancy (availability_365).
Example:

X-axis: Price

Y-axis: availability_365 (days booked/year)

Color: room_type
Insight: Do affordable listings book faster? Are expensive homes vacant often?

3. Neighborhood Demand
Graph: Bar Chart or Heatmap
Purpose: Show top neighborhoods by bookings/reviews.
Example:

X-axis: neighbourhood (top 10 by number_of_reviews)

Y-axis: reviews_per_month (proxy for demand)
Insight: Highlight high-demand areas (e.g., Midtown) for hosts to target.

4. Host Listings Impact
Graph: Scatter Plot or Histogram
Purpose: Analyze if hosts with many listings (calculated_host_listings_count) charge differently.
Example:

X-axis: calculated_host_listings_count

Y-axis: price
Insight: Do "superhosts" dominate pricing in certain areas?

5. Seasonal Trends
Graph: Line Chart
Purpose: Track booking trends over time (if data includes dates).
Example:

X-axis: last_review (month/year)

Y-axis: number_of_reviews (booking frequency)
Insight: Peak seasons (e.g., summer) may justify higher prices.

6. Room Type Popularity
Graph: Pie Chart or Stacked Bar
Purpose: Show market share of room_type (Entire home/apt vs. Private room).
Insight: Travelers may prefer entire homes despite higher costs.

Tools & Tips:
Python: Use seaborn for quick visualizations (e.g., sns.boxplot(x='neighbourhood_group', y='price')).

Tableau: Interactive dashboards to filter by neighborhood/price range.

Color: Use hues for room_type or neighbourhood_group to highlight patterns.
