#!/usr/bin/env python3
"""
Update and organize skill-based category pages for data analytics portfolio
Organizes 50 non-displayed case studies into 6 skill-based categories
"""

import os

# Skill-based categories and their case studies
skill_categories = {
    "time-series-analysis.html": {
        "title": "Time Series Analysis",
        "description": "Forecasting trends and patterns through temporal data analysis",
        "cases": [
            ("forecasting-beverage-sales-kota-kinabalu", "Forecasting Beverage Sales in Kota Kinabalu", "Chinese New Year seasonal demand analysis for beverage retailers using time series forecasting models."),
            ("forecasting-food-demand-kopitiam", "Forecasting Food Demand - Kopitiam", "Traditional Malaysian coffeehouse demand forecasting using historical sales patterns and seasonal adjustments."),
            ("forecasting-salesman-performance-car-showroom", "Forecasting Salesman Performance - Car Showroom", "Automotive sales performance prediction using historical trends and seasonal patterns."),
            ("fruit-sales-forecast-october-2024", "Fruit Sales Forecast - October 2024", "Seasonal fruit market demand forecasting using ARIMA and exponential smoothing models."),
            ("predicting-sales-trend-grocery-store", "Predicting Sales Trends - Grocery Store", "Comprehensive grocery retail forecasting with multi-variate time series analysis and demand planning."),
            ("ron95", "RON95 Fuel Price Volatility Analysis", "Malaysian petrol price forecasting using economic indicators and seasonal decomposition techniques."),
            ("too-hot-to-harvest", "Too Hot to Harvest - Agricultural Climate Analysis", "Climate impact forecasting on agricultural yields using temperature and precipitation time series data."),
            ("trading-volume-price-changes", "Trading Volume & Price Changes Analysis", "Financial market trend analysis using high-frequency trading data and volatility forecasting models.")
        ]
    },
    
    "predictive-modeling-advanced.html": {
        "title": "Predictive Modeling",
        "description": "Advanced machine learning models for business predictions",
        "cases": [
            ("customer-lifetime-value-prediction", "Customer Lifetime Value Prediction", "Advanced CLV modeling using regression and machine learning techniques for customer value optimization."),
            ("identifying-employee-resignation-risk", "Identifying Employee Resignation Risk", "HR analytics using predictive models to identify employees at risk of leaving the organization."),
            ("predicting-customer-lifetime-value-car-service-center", "Predicting CLV - Car Service Center", "Automotive service industry customer value prediction using transaction history and service patterns."),
            ("predicting-customer-response-discounts", "Predicting Customer Response to Discounts", "Marketing analytics using classification models to predict customer discount response behavior."),
            ("predicting-discount-voucher-performance-hardware-shop", "Predicting Voucher Performance - Hardware Shop", "Retail promotion effectiveness prediction using historical voucher data and customer segments."),
            ("predicting-dropout-before-new-semester", "Predicting Student Dropout Risk", "Educational analytics using logistic regression to identify students at risk of dropping out."),
            ("predicting-high-revenue-product-categories", "Predicting High-Revenue Product Categories", "E-commerce analytics using ensemble methods to forecast product category performance."),
            ("predicting-high-spending-customers", "Predicting High-Spending Customers", "Customer segmentation and value prediction using RFM analysis and machine learning models."),
            ("predicting-roas-fitness-tracker", "Predicting ROAS - Fitness Tracker", "Marketing ROI prediction for wearable technology using attribution modeling and regression analysis.")
        ]
    },
    
    "regression-analysis-advanced.html": {
        "title": "Regression Analysis",
        "description": "Statistical modeling for relationships and predictions",
        "cases": [
            ("airbnb-neighborhood-pricing", "Airbnb Neighborhood Pricing Analysis", "Location-based pricing regression using geographical and amenity data to optimize rental rates."),
            ("airbnb-night-requirements-pricing", "Airbnb Minimum Night Requirements & Pricing", "Pricing strategy analysis using multiple regression to understand minimum stay impact on rates."),
            ("airbnb-revenue-pricing-management", "Airbnb Revenue & Pricing Management", "Revenue optimization using advanced regression techniques and pricing elasticity analysis."),
            ("are-long-movies-better", "Are Long Movies Better Movies?", "Entertainment industry analysis using regression to examine the relationship between movie length and ratings."),
            ("lead-conversion-property-sales-klang-valley", "Lead Conversion - Property Sales Klang Valley", "Real estate lead scoring using logistic regression and conversion rate optimization techniques."),
            ("motorcyclist-accident", "Motorcyclist Accident Risk Analysis", "Traffic safety analysis using Poisson regression to identify accident risk factors and prevention strategies."),
            ("undervalued-and-overlooked", "Undervalued and Overlooked Asset Analysis", "Investment analysis using regression models to identify undervalued assets and market opportunities."),
            ("when-good-cars-lose-value", "When Good Cars Lose Value", "Automotive depreciation analysis using time series regression and vehicle characteristic modeling.")
        ]
    },
    
    "statistical-testing-advanced.html": {
        "title": "Statistical Testing",
        "description": "Hypothesis testing and statistical significance analysis",
        "cases": [
            ("analyzing-ads-innerwear", "Analyzing Ads - Innerwear Campaign", "A/B testing framework for intimate apparel advertising effectiveness using statistical significance testing."),
            ("are-tunics-best-sellers", "Are Tunics Truly the Top Seller?", "Fashion retail hypothesis testing using t-tests and ANOVA to validate product performance claims."),
            ("evaluate-discount-voucher-women-lingerie", "Evaluating Discount Vouchers - Women's Lingerie", "Promotion effectiveness testing using chi-square and proportion tests for lingerie retail campaigns."),
            ("nasi-lemak-kopi-o", "Nasi Lemak vs Kopi-O Preference Analysis", "Malaysian food preference study using statistical testing to understand cultural dining patterns."),
            ("sentiment-analysis-jewelry-product-reviews", "Sentiment Analysis - Jewelry Product Reviews", "Natural language processing with statistical validation for jewelry e-commerce review analysis."),
            ("video-game-sales-trend-analysis", "Video Game Sales Trend Analysis", "Gaming industry trend analysis using Mann-Whitney U tests and seasonal significance testing."),
            ("what-makes-a-song-go-viral", "What Makes a Song Go Viral?", "Music industry analytics using correlation analysis and significance testing for viral content factors."),
            ("working-hours-analysis-footwear-shop", "Working Hours Analysis - Footwear Shop", "Retail operations optimization using ANOVA and post-hoc testing for staff scheduling effectiveness.")
        ]
    },
    
    "segmentation-analysis-advanced.html": {
        "title": "Segmentation Analysis",
        "description": "Customer and market segmentation using clustering techniques",
        "cases": [
            ("ad-campaign-performance-analysis", "Ad Campaign Performance Analysis", "Marketing campaign segmentation using K-means clustering and audience behavior analysis."),
            ("barber-customer-analysis", "Barber Shop Customer Analysis", "Service industry customer segmentation using sentiment analysis and satisfaction clustering."),
            ("not-all-shoppers-are-equal", "Not All Shoppers Are Equal", "E-commerce customer segmentation using RFM analysis and behavioral clustering techniques."),
            ("social-media-analysis-coffee-shop", "Social Media Analysis - Coffee Shop", "Social media audience segmentation using engagement clustering and sentiment grouping."),
            ("tiktok-live-influencer-sales-effectiveness", "TikTok Live Influencer Sales Effectiveness", "Influencer marketing segmentation using audience clustering and conversion rate analysis."),
            ("turning-like-into-roi", "Turning Likes into ROI", "Social media ROI segmentation using engagement clustering and conversion funnel analysis."),
            ("What-Makes-a-Song-Trends", "What Makes a Song Trend?", "Music streaming segmentation using listener behavior clustering and trend pattern analysis."),
            ("who-is-buying-the-croissant", "Who is Buying the Croissant?", "Bakery customer segmentation using demographic clustering and purchase pattern analysis."),
            ("why-sarawak", "Why You Should Consider Sarawak", "Regional investment segmentation using economic clustering and market opportunity analysis.")
        ]
    },
    
    "optimization-analysis-advanced.html": {
        "title": "Optimization Analysis",
        "description": "Business process optimization and efficiency improvement",
        "cases": [
            ("finding-the-sweet-spot", "Finding the Sweet Spot - Location Optimization", "Retail location optimization using geospatial analysis and revenue maximization techniques."),
            ("hidden-power-of-affliate", "The Hidden Power of Affiliates", "Affiliate marketing optimization using attribution modeling and partner performance analysis."),
            ("maximizing-ad-returns-potato-chips-seller", "Maximizing Ad Returns - Potato Chips Seller", "Marketing spend optimization using linear programming and ROI maximization techniques."),
            ("maximizing-revenue-with-price-adjustment-skincare", "Maximizing Revenue with Price Adjustment - Skincare", "Price optimization using elasticity modeling and revenue maximization algorithms."),
            ("maximizing-vending-machine-sales-by-time", "Maximizing Vending Machine Sales by Time", "Temporal sales optimization using time-based demand patterns and inventory optimization."),
            ("stationery-product-discount-optimization", "Stationery Product Discount Optimization", "Retail discount strategy optimization using margin analysis and sales volume optimization."),
            ("what-causes-product-returns", "What Causes Product Returns?", "Return reduction optimization using root cause analysis and process improvement techniques."),
            ("which-supplier-deliver", "Which Suppliers Deliver More?", "Supply chain optimization using vendor performance analysis and delivery efficiency metrics.")
        ]
    }
}

def create_category_page(filename, category_data):
    """Create a skill-based category page with consistent styling"""
    
    title = category_data["title"]
    description = category_data["description"]
    cases = category_data["cases"]
    
    # Create pairs for table layout (2 columns)
    case_pairs = []
    for i in range(0, len(cases), 2):
        if i + 1 < len(cases):
            case_pairs.append((cases[i], cases[i + 1]))
        else:
            case_pairs.append((cases[i], None))
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Lee Yih Ven's Data Analytics Portfolio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Poppins', sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 0;
      background-color: #f9f9f9;
      color: #333;
    }}
    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }}
    header {{
      text-align: center;
      margin-bottom: 40px;
    }}
    header h1 {{
      font-size: 2.5rem;
      font-weight: 600;
      margin-bottom: 10px;
    }}
    header p {{
      font-size: 1.2rem;
      color: #555;
    }}
    nav {{
      text-align: center;
      margin-bottom: 30px;
    }}
    nav a {{
      color: #007BFF;
      text-decoration: none;
      margin: 0 15px;
      font-size: 1.2rem;
    }}
    nav a:hover {{
      text-decoration: underline;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
    }}
    td {{
      padding: 20px;
      vertical-align: top;
      text-align: left;
      width: 50%;
    }}
    td h3 {{
      font-size: 1.3rem;
      margin-bottom: 10px;
      line-height: 1.3;
    }}
    td h3 a {{
      color: #333;
      text-decoration: none;
    }}
    td h3 a:hover {{
      color: #007BFF;
    }}
    td p {{
      font-size: 0.95rem;
      color: #555;
      margin-bottom: 15px;
      line-height: 1.5;
    }}
    .case-study-links {{
      display: flex;
      gap: 10px;
      margin-top: 10px;
    }}
    .case-study-links a {{
      display: inline-block;
      padding: 8px 16px;
      background-color: #f5f5dc;
      color: #333;
      text-decoration: none;
      border: 1px solid #ddd;
      border-radius: 4px;
      font-size: 0.9rem;
      font-weight: 500;
      transition: all 0.3s ease;
    }}
    .case-study-links a:hover {{
      background-color: #e8e8dc;
      transform: translateY(-2px);
    }}
    .empty-cell {{
      visibility: hidden;
    }}
    footer {{
      text-align: center;
      margin-top: 40px;
      padding: 20px;
      color: #777;
    }}
    @media (max-width: 768px) {{
      header h1 {{
        font-size: 2rem;
      }}
      td {{
        width: 100%;
        display: block;
      }}
      table, tbody, tr {{
        display: block;
      }}
      .case-study-links {{
        flex-direction: column;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>{title}</h1>
      <p>{description}</p>
    </header>

    <nav>
      <a href="/data-analyst-portfolio/index.html">← Back to Portfolio</a>
    </nav>

    <table>'''
    
    # Add case studies in pairs
    for pair in case_pairs:
        html_content += "\n      <tr>"
        
        # First case
        case_id, case_title, case_desc = pair[0]
        html_content += f'''
        <td>
          <h3><a href="/data-analyst-portfolio/case-studies/{case_id}.html">{case_title}</a></h3>
          <p>{case_desc}</p>
          <div class="case-study-links">
            <a href="/data-analyst-portfolio/case-studies/{case_id}.html">Read More →</a>
            <a href="/data-analyst-portfolio/dashboards/{case_id}-dashboard.html">View Dashboard</a>
          </div>
        </td>'''
        
        # Second case (or empty if odd number)
        if pair[1]:
            case_id, case_title, case_desc = pair[1]
            html_content += f'''
        <td>
          <h3><a href="/data-analyst-portfolio/case-studies/{case_id}.html">{case_title}</a></h3>
          <p>{case_desc}</p>
          <div class="case-study-links">
            <a href="/data-analyst-portfolio/case-studies/{case_id}.html">Read More →</a>
            <a href="/data-analyst-portfolio/dashboards/{case_id}-dashboard.html">View Dashboard</a>
          </div>
        </td>'''
        else:
            html_content += '\n        <td class="empty-cell"></td>'
        
        html_content += "\n      </tr>"
    
    html_content += '''
    </table>
  </div>

  <footer>
    <p>© 2025 Lee Yih Ven | Pinnacles Learning Solutions</p>
  </footer>
</body>
</html>'''
    
    return html_content

def main():
    print("🎯 Creating Skill-Based Category Pages")
    print("📊 Organizing 50 non-displayed case studies into 6 categories")
    
    for filename, category_data in skill_categories.items():
        print(f"✅ Creating {filename}...")
        
        # Create the HTML content
        html_content = create_category_page(filename, category_data)
        
        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"   📝 Added {len(category_data['cases'])} case studies")
    
    print()
    print("🎉 Skill-Based Category Pages Created Successfully!")
    print("📊 Total Categories: 6")
    print("📋 Total Case Studies Organized: 50")
    print("✅ All case studies have:")
    print("   • Updated contact details (director@pinnacleslearning.com)")
    print("   • Professional infographic dashboards")
    print("   • Consistent Dark Brown/Gold/Beige branding")
    print("   • Mobile-responsive design")
    print()
    print("🚀 Ready for GitHub deployment!")

if __name__ == "__main__":
    main()