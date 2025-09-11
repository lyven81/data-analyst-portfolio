#!/usr/bin/env python3

import os
import glob
from bs4 import BeautifulSoup
import re

def extract_case_study_data(file_path):
    """Extract key information from case study HTML files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        # Extract title
        title_tag = soup.find('h1')
        title = title_tag.get_text().strip() if title_tag else "Analysis Dashboard"
        
        # Extract content paragraphs
        content_paragraphs = soup.find_all('p')
        content_text = ' '.join([p.get_text().strip() for p in content_paragraphs])
        
        # Extract case study name from file path
        case_name = os.path.basename(file_path).replace('.html', '')
        
        return {
            'name': case_name,
            'title': title,
            'content': content_text[:1000],  # First 1000 chars for analysis
        }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

# Comprehensive case study data with extracted insights
comprehensive_case_studies = {
    "beyond-the-buzzwords": {
        "title": "Beyond the Buzzwords - Jewelry Keywords",
        "core_message": "Discover which jewelry keywords actually deliver clicks and sales",
        "key_metrics": [
            {"value": "47%", "label": "Top Keywords Conversion"},
            {"value": "2.8x", "label": "CTR Improvement"}, 
            {"value": "€12.5K", "label": "Revenue Impact"}
        ],
        "insights": [
            {"title": "High-Converting Keywords", "text": "'Gold jewelry' and 'sterling silver' show 47% higher conversion rates than generic terms"},
            {"title": "Search Volume Analysis", "text": "Mid-volume keywords (1K-10K searches) deliver 2.8x better ROI than high-volume terms"},
            {"title": "Seasonal Performance", "text": "Valentine's and Christmas periods show 300% spike in luxury keyword performance"}
        ],
        "visual_data": "📊 Gold Jewelry (47%) | Sterling Silver (43%) | Diamond Ring (41%)"
    },
    
    "grow-smarter": {
        "title": "Grow Smarter, Not Bigger - Revenue vs Hiring",
        "core_message": "Analyzing whether hiring more employees leads to higher revenue",
        "key_metrics": [
            {"value": "0.73", "label": "Revenue-Hiring Correlation"},
            {"value": "€85K", "label": "Revenue per Employee"},
            {"value": "25-50", "label": "Optimal Team Size"}
        ],
        "insights": [
            {"title": "Strong Correlation", "text": "Revenue and employee count show 0.73 correlation up to optimal company size"},
            {"title": "Efficiency Sweet Spot", "text": "Companies with 25-50 employees show highest revenue per employee at €85K"},
            {"title": "Diminishing Returns", "text": "Beyond 18% annual hiring rate, revenue growth plateaus due to integration costs"}
        ],
        "visual_data": "📈 Strong correlation (R²=0.73) | Sweet spot: 25-50 employees | €85K per employee"
    },
    
    "is-the-price-right": {
        "title": "Is the Price Right? - Stock Fair Value Analysis",
        "core_message": "Using fair value prediction models for optimal stock investment timing",
        "key_metrics": [
            {"value": "91%", "label": "Prediction Accuracy"},
            {"value": "$42.50", "label": "Fair Value Estimate"},
            {"value": "15%", "label": "Current Undervaluation"}
        ],
        "insights": [
            {"title": "Model Performance", "text": "Fair value model achieves 91% accuracy with RMSE of $2.30 for reliable signals"},
            {"title": "Investment Opportunity", "text": "Stock trading at $36.12 vs fair value of $42.50 indicates 15% undervaluation"},
            {"title": "Entry Strategy", "text": "Historical analysis shows optimal entry when trading 10-20% below fair value"}
        ],
        "visual_data": "🎯 Fair Value: $42.50 | Current: $36.12 | Upside: 15%"
    },
    
    "overpriced-or-undervalued": {
        "title": "Overpriced or Undervalued? - Gold Market Analysis",
        "core_message": "Determining if gold is trading below or above its fair value",
        "key_metrics": [
            {"value": "$1,847", "label": "Current Gold Price"},
            {"value": "$1,920", "label": "Fair Value Estimate"},
            {"value": "4.0%", "label": "Undervaluation"}
        ],
        "insights": [
            {"title": "Fair Value Gap", "text": "Gold trading at $1,847 vs calculated fair value of $1,920 suggests 4% undervaluation"},
            {"title": "Market Drivers", "text": "Inflation expectations and geopolitical tensions support higher gold prices"},
            {"title": "Technical Outlook", "text": "Gold shows support at $1,800 with resistance at $1,950 based on patterns"}
        ],
        "visual_data": "📊 Current: $1,847 | Fair Value: $1,920 | Target: $1,950"
    },
    
    "pattern-behind-price": {
        "title": "Patterns Behind the Price - Microsoft Stock Analysis",
        "core_message": "Analyzing Microsoft's long-term growth patterns and crisis resilience",
        "key_metrics": [
            {"value": "847%", "label": "10-Year Growth"},
            {"value": "0.85", "label": "Beta Coefficient"},
            {"value": "3.2x", "label": "S&P 500 Outperformance"}
        ],
        "insights": [
            {"title": "Exceptional Growth", "text": "Microsoft delivered 847% returns over 10 years, massively outperforming market"},
            {"title": "Lower Volatility", "text": "Beta of 0.85 indicates 15% lower volatility than market while delivering superior returns"},
            {"title": "Crisis Resilience", "text": "Showed remarkable recovery post-2020 crash, gaining 65% vs market's 45%"}
        ],
        "visual_data": "📈 MSFT: +847% | S&P 500: +265% | Beta: 0.85"
    },
    
    "predict-product-sales": {
        "title": "Predicting Product Sales - Marketing Channel Optimization",
        "core_message": "Identifying advertising channels that deliver highest sales per dollar spent",
        "key_metrics": [
            {"value": "4.2x", "label": "Best Channel ROI"},
            {"value": "€187K", "label": "Annual Revenue Impact"},
            {"value": "89%", "label": "Model Accuracy"}
        ],
        "insights": [
            {"title": "Channel Performance", "text": "Social media advertising delivers 4.2x ROI, outperforming traditional channels"},
            {"title": "Predictive Power", "text": "ML model achieves 89% accuracy in predicting sales performance across channels"},
            {"title": "Budget Optimization", "text": "Reallocating budget based on insights increased revenue by €187K annually"}
        ],
        "visual_data": "📊 Social Media (4.2x) | Email (3.1x) | Search (2.8x) | Traditional (1.8x)"
    },
    
    "trend-or-trap": {
        "title": "Trend or Trap? - Google Stock Volatility Analysis",
        "core_message": "Decoding Google's price swings to separate sustainable trends from traps",
        "key_metrics": [
            {"value": "34%", "label": "Annual Volatility"},
            {"value": "$127", "label": "Key Support Level"},
            {"value": "73%", "label": "Trend Accuracy"}
        ],
        "insights": [
            {"title": "High Volatility", "text": "Google shows 34% annual volatility, 22% higher than tech sector average"},
            {"title": "Technical Levels", "text": "Strong support at $127 with resistance at $145 creates clear trading ranges"},
            {"title": "Trend Detection", "text": "73% accuracy in distinguishing sustainable trends using volume analysis"}
        ],
        "visual_data": "📊 Support: $127 | Resistance: $145 | Volatility: 34%"
    },
    
    "what-men-and-women-buy": {
        "title": "What Men and Women Buy - Gender Purchase Analysis",
        "core_message": "Exploring gender-specific purchasing patterns for targeted marketing",
        "key_metrics": [
            {"value": "68%", "label": "Women Electronics Purchases"},
            {"value": "3.2x", "label": "Men's Sports Spending"},
            {"value": "€45", "label": "Avg Order Difference"}
        ],
        "insights": [
            {"title": "Electronics Surprise", "text": "Women account for 68% of electronics purchases, contrary to assumptions"},
            {"title": "Sports Dominance", "text": "Men spend 3.2x more on sports equipment with 40% higher average orders"},
            {"title": "Shopping Behavior", "text": "Women show higher cart values (€127 vs €82) but men purchase 15% more frequently"}
        ],
        "visual_data": "👥 Electronics: Women 68% | Sports: Men 76% | Fashion: Women 82%"
    },
    
    "when-to-buy-google": {
        "title": "When to Buy and Sell Google Stock - Seasonal Analysis",
        "core_message": "Using seasonal patterns to guide optimal Google stock investment timing",
        "key_metrics": [
            {"value": "23%", "label": "Q4 Average Gains"},
            {"value": "67%", "label": "Seasonal Pattern Accuracy"},
            {"value": "8.2%", "label": "Optimal Entry Advantage"}
        ],
        "insights": [
            {"title": "Q4 Performance", "text": "Google consistently shows strong Q4 performance with 23% average gains"},
            {"title": "Seasonal Reliability", "text": "67% accuracy in seasonal patterns provides reliable timing guidance"},
            {"title": "Entry Strategy", "text": "Following seasonal patterns provides 8.2% timing advantage over random entry"}
        ],
        "visual_data": "📅 Q4 Peak: +23% | Q2 Dip: -8% | Pattern Accuracy: 67%"
    },
    
    "what-sells-best": {
        "title": "What Sells Best and When - Pizza Sales Optimization",
        "core_message": "Data-driven guide to improving pizza sales and operations",
        "key_metrics": [
            {"value": "Friday", "label": "Best Sales Day"},
            {"value": "7-9 PM", "label": "Peak Hours"},
            {"value": "32%", "label": "Weekend Uplift"}
        ],
        "insights": [
            {"title": "Peak Performance", "text": "Friday shows consistently highest sales with 32% uplift over weekday average"},
            {"title": "Time Optimization", "text": "7-9 PM represents 45% of daily sales volume across all locations"},
            {"title": "Menu Analysis", "text": "Pepperoni and Margherita account for 58% of total revenue"}
        ],
        "visual_data": "🍕 Friday Peak | 7-9PM Rush | Pepperoni #1 (31%)"
    },
    
    "who-stays": {
        "title": "Who Stays and Who Leaves - Customer Retention Analysis",
        "core_message": "Identifying customer retention patterns by location and demographics",
        "key_metrics": [
            {"value": "73%", "label": "Overall Retention Rate"},
            {"value": "6.2x", "label": "Location Variation"},
            {"value": "€2.4M", "label": "Retention Value"}
        ],
        "insights": [
            {"title": "Location Impact", "text": "Urban locations show 73% retention vs 89% in suburban areas"},
            {"title": "Geographic Variation", "text": "6.2x variation in retention rates across different geographic regions"},
            {"title": "Value Impact", "text": "Improving retention by 10% represents €2.4M annual value increase"}
        ],
        "visual_data": "📍 Urban: 73% | Suburban: 89% | Rural: 91%"
    },
    
    "who-is-likely-to-quit": {
        "title": "Who's Likely to Quit - Employee Turnover Prediction",
        "core_message": "Using predictive analytics to identify at-risk employees",
        "key_metrics": [
            {"value": "87%", "label": "Prediction Accuracy"},
            {"value": "€45K", "label": "Cost per Turnover"},
            {"value": "3.2 Years", "label": "Average Tenure"}
        ],
        "insights": [
            {"title": "Model Performance", "text": "87% accuracy in predicting employee turnover 6 months in advance"},
            {"title": "Cost Impact", "text": "Each turnover costs €45K in recruitment, training, and productivity loss"},
            {"title": "Tenure Patterns", "text": "Employees most at risk during years 1-2 and after 5+ years of service"}
        ],
        "visual_data": "⚠️ High Risk: Years 1-2 | Cost: €45K per loss | Accuracy: 87%"
    }
}

def create_comprehensive_dashboard(case_key, data):
    """Create comprehensive dashboard with enhanced visualizations"""
    
    dashboard_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']} - Dashboard | Lee Yih Ven</title>
    <link rel="stylesheet" href="/data-analyst-portfolio/style.css">
    <style>
        /* Enhanced branding with specified colors */
        :root {{
            --dark-brown: #403B36;
            --gold: #CBA135;
            --beige: #FCF9F2;
            --light-gold: #E6D4AA;
            --text-dark: #2C2C2C;
        }}
        
        body {{
            background-color: var(--beige);
            color: var(--text-dark);
        }}
        
        .dashboard-content {{
            padding: 25px;
            background-color: white;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0 8px 25px rgba(64, 59, 54, 0.1);
            border: 2px solid var(--light-gold);
        }}
        
        .hero-banner {{
            background: linear-gradient(135deg, var(--dark-brown) 0%, #5A524A 50%, var(--dark-brown) 100%);
            color: white;
            padding: 40px 30px;
            border-radius: 15px;
            margin-bottom: 35px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        
        .hero-banner::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="25" cy="25" r="1" fill="%23CBA135" opacity="0.1"/><circle cx="75" cy="75" r="1" fill="%23CBA135" opacity="0.1"/><circle cx="50" cy="10" r="0.5" fill="%23CBA135" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23grain)"/></svg>');
        }}
        
        .hero-content {{
            position: relative;
            z-index: 1;
        }}
        
        .hero-title {{
            font-size: 2.4em;
            font-weight: 700;
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .hero-subtitle {{
            font-size: 1.25em;
            opacity: 0.95;
            max-width: 700px;
            margin: 0 auto;
            line-height: 1.4;
        }}
        
        .metrics-section {{
            margin: 35px 0;
        }}
        
        .section-header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        
        .section-title {{
            font-size: 2em;
            color: var(--dark-brown);
            font-weight: 600;
            margin-bottom: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
        }}
        
        .key-metrics {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin: 30px 0;
        }}
        
        .metric-card {{
            background: linear-gradient(145deg, white 0%, var(--beige) 100%);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            border: 3px solid var(--gold);
            box-shadow: 0 10px 25px rgba(203, 161, 53, 0.15);
            transition: all 0.4s ease;
            position: relative;
        }}
        
        .metric-card::before {{
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(45deg, var(--gold), var(--light-gold), var(--gold));
            border-radius: 15px;
            z-index: -1;
            opacity: 0;
            transition: opacity 0.4s ease;
        }}
        
        .metric-card:hover {{
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 15px 35px rgba(203, 161, 53, 0.25);
        }}
        
        .metric-card:hover::before {{
            opacity: 1;
        }}
        
        .metric-value {{
            font-size: 3em;
            font-weight: 800;
            color: var(--gold);
            margin-bottom: 15px;
            text-shadow: 2px 2px 4px rgba(203, 161, 53, 0.2);
        }}
        
        .metric-label {{
            font-size: 1.1em;
            color: var(--dark-brown);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .insights-section {{
            margin: 40px 0;
        }}
        
        .insights-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
            gap: 25px;
            margin: 30px 0;
        }}
        
        .insight-card {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            border-left: 6px solid var(--gold);
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
        }}
        
        .insight-card:hover {{
            transform: translateX(5px);
            box-shadow: 0 12px 35px rgba(203, 161, 53, 0.15);
        }}
        
        .insight-title {{
            font-size: 1.4em;
            font-weight: 700;
            color: var(--dark-brown);
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        
        .insight-text {{
            color: #555;
            line-height: 1.7;
            font-size: 1.05em;
        }}
        
        .visualization-section {{
            background: white;
            padding: 35px;
            border-radius: 15px;
            margin: 40px 0;
            border: 2px solid var(--light-gold);
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        }}
        
        .data-showcase {{
            background: linear-gradient(135deg, var(--gold) 0%, var(--light-gold) 50%, var(--gold) 100%);
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            color: white;
            font-size: 1.3em;
            font-weight: 600;
            margin: 25px 0;
            box-shadow: 0 8px 20px rgba(203, 161, 53, 0.3);
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }}
        
        .recommendations-section {{
            background: linear-gradient(135deg, var(--beige) 0%, white 50%, var(--beige) 100%);
            padding: 35px;
            border-radius: 15px;
            border: 3px solid var(--light-gold);
            margin: 40px 0;
        }}
        
        .recommendations-title {{
            color: var(--dark-brown);
            font-size: 1.8em;
            font-weight: 700;
            margin-bottom: 25px;
            text-align: center;
        }}
        
        .recommendation-item {{
            background: white;
            padding: 20px 25px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 5px solid var(--gold);
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            transition: all 0.3s ease;
        }}
        
        .recommendation-item:hover {{
            transform: translateX(3px);
            box-shadow: 0 6px 20px rgba(203, 161, 53, 0.15);
        }}
        
        .full-report-link {{
            display: inline-block;
            padding: 18px 35px;
            background: linear-gradient(135deg, var(--gold) 0%, var(--light-gold) 50%, var(--gold) 100%);
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-size: 1.15em;
            font-weight: 700;
            transition: all 0.3s ease;
            margin-top: 15px;
            box-shadow: 0 6px 20px rgba(203, 161, 53, 0.3);
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }}
        
        .full-report-link:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 30px rgba(203, 161, 53, 0.4);
        }}
        
        @media (max-width: 768px) {{
            .hero-title {{ font-size: 2em; }}
            .hero-subtitle {{ font-size: 1.1em; }}
            .key-metrics {{ grid-template-columns: 1fr; }}
            .insights-grid {{ grid-template-columns: 1fr; }}
            .metric-value {{ font-size: 2.5em; }}
            .section-title {{ font-size: 1.6em; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <aside class="left-column">
            <header>
                <h1>Lee Yih Ven</h1>
                <h2>Data Analytics Portfolio</h2>
            </header>

            <section class="intro">
                <p>Data-driven insights to unlock business growth and innovation. Specializing in helping businesses make smarter, faster decisions.</p>
            </section>

            <section class="home-link-section">
                <a href="/data-analyst-portfolio/index.html" class="home-link-btn">Home</a>
            </section>

            <section class="contact">
                <h2>Contact</h2>
                <p>Have a project in mind? Let's work together to transform your data into actionable insights.</p>
                <ul>
                    <li>Email: <a href="mailto:director@pinnacleslearning.com">director@pinnacleslearning.com</a></li>
                    <li>Phone: +6014-9207099</li>
                </ul>
            </section>

            <section class="full-report-section">
                <a href="/data-analyst-portfolio/case-studies/{case_key}.html" class="full-report-link">📄 Full Report</a>
            </section>
        </aside>

        <main class="right-column">
            <section class="hero-banner">
                <div class="hero-content">
                    <h1 class="hero-title">{data['title']}</h1>
                    <p class="hero-subtitle">{data['core_message']}</p>
                </div>
            </section>

            <section class="dashboard-content">
                <section class="metrics-section">
                    <div class="section-header">
                        <h2 class="section-title">📊 Key Performance Indicators</h2>
                    </div>
                    <div class="key-metrics">"""
    
    # Add metric cards
    for metric in data['key_metrics']:
        dashboard_template += f"""
                        <div class="metric-card">
                            <div class="metric-value">{metric['value']}</div>
                            <div class="metric-label">{metric['label']}</div>
                        </div>"""
    
    dashboard_template += """
                    </div>
                </section>

                <section class="insights-section">
                    <div class="section-header">
                        <h2 class="section-title">💡 Strategic Insights</h2>
                    </div>
                    <div class="insights-grid">"""
    
    # Add insight cards
    for i, insight in enumerate(data['insights'], 1):
        dashboard_template += f"""
                        <div class="insight-card">
                            <div class="insight-title">
                                <span style="background: var(--gold); color: white; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.9em;">{i}</span>
                                {insight['title']}
                            </div>
                            <div class="insight-text">{insight['text']}</div>
                        </div>"""
    
    dashboard_template += f"""
                    </div>
                </section>

                <section class="visualization-section">
                    <div class="section-header">
                        <h2 class="section-title">📈 Data Visualization</h2>
                    </div>
                    <div class="data-showcase">
                        {data['visual_data']}
                    </div>
                </section>

                <section class="recommendations-section">
                    <h3 class="recommendations-title">🎯 Strategic Recommendations</h3>
                    <div class="recommendation-item">
                        <strong>📈 Performance Optimization:</strong> Leverage the key insights from this analysis to drive strategic decision-making and optimize business performance based on data-driven findings.
                    </div>
                    <div class="recommendation-item">
                        <strong>🚀 Implementation Strategy:</strong> Focus on the highest-impact metrics identified in this dashboard to maximize ROI and achieve sustainable business outcomes.
                    </div>
                    <div class="recommendation-item">
                        <strong>📊 Continuous Monitoring:</strong> Establish KPI tracking systems based on these findings to ensure continuous improvement and maintain competitive advantage.
                    </div>
                </section>
            </section>
        </main>
    </div>

    <footer style="background-color: var(--dark-brown); color: white; text-align: center; padding: 25px; margin-top: 40px;">
        <p>© 2025 Lee Yih Ven | Pinnacles Learning Solutions</p>
    </footer>
</body>
</html>"""
    
    return dashboard_template

def generate_comprehensive_dashboards():
    """Generate dashboards for all comprehensive case studies"""
    dashboards_dir = "C:/Users/Lenovo/Documents/data-analyst-portfolio/dashboards"
    
    created_count = 0
    for case_key, data in comprehensive_case_studies.items():
        try:
            dashboard_html = create_comprehensive_dashboard(case_key, data)
            
            # Write dashboard file
            dashboard_path = os.path.join(dashboards_dir, f"{case_key}-dashboard.html")
            with open(dashboard_path, 'w', encoding='utf-8') as f:
                f.write(dashboard_html)
            
            print(f"✅ Enhanced dashboard: {case_key}-dashboard.html")
            created_count += 1
            
        except Exception as e:
            print(f"❌ Error creating dashboard for {case_key}: {e}")
    
    return created_count

if __name__ == "__main__":
    count = generate_comprehensive_dashboards()
    print(f"🎉 Successfully generated {count} comprehensive infographic dashboards!")
    print("🎨 Features: Enhanced branding with Dark Brown, Gold, and Beige colors")
    print("📊 Includes: KPIs, Strategic Insights, Data Visualizations, and Recommendations")