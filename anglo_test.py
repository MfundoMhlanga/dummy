import streamlit as st
import pandas as pd
import numpy as np

# Dummy data generation
np.random.seed(42)
dates_paid = pd.date_range(start='2023-07-01', periods=10).repeat(4)
dates_seo = pd.date_range(start='2023-07-01', periods=10)
dates_social = pd.date_range(start='2023-07-01', periods=5).repeat(4)

data = {
    'Date': dates_paid,
    'Network': ['Twitter', 'Facebook', 'LinkedIn', 'Google Ads'] * 10,
    'CPA': np.random.uniform(1, 5, 40),
    'Impressions': np.random.randint(1000, 5000, 40),
    'Clicks': np.random.randint(100, 500, 40),
    'Conversions': np.random.randint(10, 100, 40)
}
df_paid = pd.DataFrame(data)

seo_data = {
    'Date': dates_seo,
    'Keyword': ['SEO'] * 10,
    'Clicks': np.random.randint(1000, 5000, 10),
    'Impressions': np.random.randint(10000, 50000, 10),
    'CTR': np.random.uniform(1, 10, 10),
    'Average Position': np.random.uniform(1, 10, 10)
}
df_seo = pd.DataFrame(seo_data)

social_data = {
    'Date': dates_social,
    'Platform': ['Twitter', 'Facebook', 'Instagram', 'LinkedIn'] * 5,
    'Mentions': np.random.randint(100, 1000, 20),
    'Sentiment': np.random.choice(['Positive', 'Neutral', 'Negative'], 20),
    'Engagement': np.random.randint(1000, 5000, 20)
}
df_social = pd.DataFrame(social_data)

# Reset indexes to start at 1
df_paid.index = df_paid.index + 1
df_seo.index = df_seo.index + 1
df_social.index = df_social.index + 1

# Streamlit app
st.title("Digital Marketing Performance Dashboard")

# Initialize session state
if 'section' not in st.session_state:
    st.session_state.section = 'Paid Media Performance'

# Horizontal buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Paid Media Performance"):
        st.session_state.section = 'Paid Media Performance'

with col2:
    if st.button("SEO Performance"):
        st.session_state.section = 'SEO Performance'

with col3:
    if st.button("Social Listening Performance"):
        st.session_state.section = 'Social Listening Performance'

# Display selected section
if st.session_state.section == 'Paid Media Performance':
    st.header("Paid Media Performance")
    st.markdown("""
    This section shows the performance of your paid advertising campaigns across different networks. 
    Paid media includes ads on platforms like Twitter, Facebook, LinkedIn, and Google Ads. Key metrics include:
    - **Date**: The date of the performance data.
    - **CPA (Cost-Per-Acquisition)**: The average cost to acquire a customer through the ads.
    - **Impressions**: The number of times your ads were seen.
    - **Clicks**: The number of times users clicked on your ads.
    - **Conversions**: The number of users who completed a desired action (e.g., purchase, sign-up) after clicking on your ad.
    """)
    network = st.selectbox("Select Paid Media Network", df_paid['Network'].unique())
    filtered_paid_df = df_paid[df_paid['Network'] == network]
    st.write(f"Displaying metrics for: {network}")
    st.write(filtered_paid_df)
    st.header("Summary Statistics for Paid Media")
    summary_paid = filtered_paid_df.describe()
    st.write(summary_paid)

    # Paid Media Insights
    st.header("Paid Media Insights")
    st.markdown("""
    **Cost-Per-Acquisition (CPA) Insights:**
    - A lower CPA indicates a more cost-effective advertising campaign.
    - Currently, the CPA ranges from ${:.2f} to ${:.2f} for {}.
    - If the CPA is high, consider optimizing your ad targeting or improving your ad creatives to attract more relevant clicks.

    **Impressions Insights:**
    - Impressions measure how often your ads are seen.
    - {} has between {} and {} impressions.
    - High impressions with low clicks might indicate the need for better ad copy or visuals.

    **Clicks Insights:**
    - Clicks represent user interest in your ads.
    - Your ads received between {} and {} clicks.
    - Low clicks despite high impressions can suggest the need for more engaging ad content.

    **Conversions Insights:**
    - Conversions show how effective your ads are at driving actions.
    - Conversions range from {} to {}.
    - If conversions are low, ensure your landing page is optimized and relevant to your ad content.
    """.format(filtered_paid_df['CPA'].min(), filtered_paid_df['CPA'].max(), network,
            network, filtered_paid_df['Impressions'].min(), filtered_paid_df['Impressions'].max(),
            filtered_paid_df['Clicks'].min(), filtered_paid_df['Clicks'].max(),
            filtered_paid_df['Conversions'].min(), filtered_paid_df['Conversions'].max()))

    st.header("Paid Media Metrics Visualization")
    st.subheader("Cost-Per-Acquisition (CPA)")
    st.bar_chart(filtered_paid_df[['CPA']])
    st.subheader("Impressions")
    st.line_chart(filtered_paid_df[['Impressions']])
    st.subheader("Clicks")
    st.area_chart(filtered_paid_df[['Clicks']])
    st.subheader("Conversions")
    st.line_chart(filtered_paid_df[['Conversions']])

if st.session_state.section == 'SEO Performance':
    st.header("SEO Performance")
    st.markdown("""
    This section shows the performance of your SEO (Search Engine Optimization) efforts. SEO helps improve your website's visibility on search engines. Key metrics include:
    - **Date**: The date of the performance data.
    - **Clicks**: The number of times users clicked on your website from search engine results.
    - **Impressions**: The number of times your website appeared in search engine results.
    - **CTR (Click-Through Rate)**: The percentage of impressions that resulted in clicks.
    - **Average Position**: The average position of your website in search engine results.
    """)
    st.write(df_seo)
    st.header("Summary Statistics for SEO")
    summary_seo = df_seo.describe()
    st.write(summary_seo)

    # SEO Insights
    st.header("SEO Insights")
    st.markdown("""
    **Clicks Insights:**
    - Clicks indicate how many users visit your site from search results.
    - You have between {} and {} clicks.
    - Low clicks might suggest the need to improve meta titles and descriptions to be more compelling.

    **Impressions Insights:**
    - Impressions reflect how often your site appears in search results.
    - Impressions range from {} to {}.
    - If impressions are high but clicks are low, focus on improving your site's search result snippets.

    **CTR Insights:**
    - CTR measures the effectiveness of your search listings.
    - Your CTR ranges from {:.2f}% to {:.2f}%.
    - A low CTR can indicate that your listings are not attracting enough attention or relevance.

    **Average Position Insights:**
    - The average position shows your ranking in search results.
    - Your average position is between {:.2f} and {:.2f}.
    - Higher (numerically lower) positions generally lead to more clicks, so aim to improve your rankings through quality content and backlinks.
    """.format(df_seo['Clicks'].min(), df_seo['Clicks'].max(),
            df_seo['Impressions'].min(), df_seo['Impressions'].max(),
            df_seo['CTR'].min(), df_seo['CTR'].max(),
            df_seo['Average Position'].min(), df_seo['Average Position'].max()))

    st.header("SEO Metrics Visualization")
    st.subheader("Clicks")
    st.bar_chart(df_seo[['Clicks']])
    st.subheader("Impressions")
    st.line_chart(df_seo[['Impressions']])
    st.subheader("Click-Through Rate (CTR)")
    st.area_chart(df_seo[['CTR']])
    st.subheader("Average Position")
    st.line_chart(df_seo[['Average Position']])

if st.session_state.section == 'Social Listening Performance':
    st.header("Social Listening Performance")
    st.markdown("""
    This section shows the performance of your social media presence and engagement. Social listening helps you monitor and analyze conversations about your brand on social media. Key metrics include:
    - **Date**: The date of the performance data.
    - **Mentions**: The number of times your brand was mentioned on social media.
    - **Sentiment**: The overall sentiment (positive, neutral, negative) of the mentions.
    - **Engagement**: The number of interactions (likes, comments, shares) with your social media posts.
    """)
    platform = st.selectbox("Select Social Media Platform", df_social['Platform'].unique())
    filtered_social_df = df_social[df_social['Platform'] == platform]
    st.write(f"Displaying metrics for: {platform}")
    st.write(filtered_social_df)
    st.header("Summary Statistics for Social Listening")
    summary_social = filtered_social_df.describe()
    st.write(summary_social)

    # Social Listening Insights
    st.header("Social Listening Insights")
    st.markdown("""
    **Mentions Insights:**
    - Mentions show how often your brand is talked about.
    - You have between {} and {} mentions on {}.
    - Increasing mentions usually indicates growing brand awareness.

    **Engagement Insights:**
    - Engagement measures how users interact with your posts.
    - Engagement ranges from {} to {}.
    - High engagement suggests your content is resonating well with your audience.

    **Sentiment Insights:**
    - Sentiment analysis helps understand public perception of your brand.
    - Sentiment distribution is as follows:
      - Positive: {}
      - Neutral: {}
      - Negative: {}
    - A high number of negative mentions may require addressing customer concerns or improving your products/services.
    """.format(filtered_social_df['Mentions'].min(), filtered_social_df['Mentions'].max(), platform,
            filtered_social_df['Engagement'].min(), filtered_social_df['Engagement'].max(),
            (filtered_social_df['Sentiment'] == 'Positive').sum(),
            (filtered_social_df['Sentiment'] == 'Neutral').sum(),
            (filtered_social_df['Sentiment'] == 'Negative').sum()))

    st.header("Social Listening Metrics Visualization")
    st.subheader("Mentions")
    st.bar_chart(filtered_social_df[['Mentions']])
    st.subheader("Engagement")
    st.line_chart(filtered_social_df[['Engagement']])
    st.subheader("Sentiment Distribution")
    sentiment_counts = filtered_social_df['Sentiment'].value_counts()
    st.bar_chart(sentiment_counts)
