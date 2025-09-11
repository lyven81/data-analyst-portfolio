#!/usr/bin/env python3

import os
import re

# List of 16 updated dashboards that need button styling fix
updated_dashboards = [
    "beyond-the-buzzwords-dashboard.html",
    "can-money-buy-happiness-dashboard.html",
    "cash-or-credit-card-dashboard.html",
    "experience-is-not-everthing-dashboard.html",
    "grow-smarter-dashboard.html",
    "hotel-sleep-analysis-dashboard.html",
    "is-the-price-right-dashboard.html",
    "overpriced-or-undervalued-dashboard.html",
    "pattern-behind-price-dashboard.html",
    "predict-product-sales-dashboard.html",
    "trend-or-trap-dashboard.html",
    "what-men-and-women-buy-dashboard.html",
    "what-sells-best-dashboard.html",
    "when-to-buy-google-dashboard.html",
    "who-is-likely-to-quit-dashboard.html",
    "who-stays-dashboard.html"
]

def fix_full_report_button_styling(file_path):
    """Fix the Full Report button styling to match Home button"""
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Define the old shiny button styling
        old_button_css = r'\.full-report-link \{[^}]*\}'
        old_button_hover_css = r'\.full-report-link:hover \{[^}]*\}'
        
        # New button styling to match Home button
        new_button_css = """.full-report-link {
            display: inline-block;
            padding: 10px 20px;
            background-color: #f5f5dc;
            color: #333;
            text-decoration: none;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 1em;
            font-weight: 500;
            transition: all 0.3s ease;
            margin-top: 10px;
        }"""
        
        new_button_hover_css = """.full-report-link:hover {
            background-color: #daa520;
            color: white;
            border-color: #daa520;
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(218, 165, 32, 0.3);
        }"""
        
        # Replace the old styling with new styling
        content = re.sub(old_button_css, new_button_css, content, flags=re.DOTALL)
        content = re.sub(old_button_hover_css, new_button_hover_css, content, flags=re.DOTALL)
        
        # Also update the button text to remove emoji and make it consistent
        content = content.replace('📄 View Full Report', 'Full Report')
        
        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

def fix_all_dashboard_buttons():
    """Fix Full Report button styling in all updated dashboards"""
    
    dashboards_dir = "C:/Users/Lenovo/Documents/data-analyst-portfolio/dashboards"
    fixed_count = 0
    
    for dashboard_file in updated_dashboards:
        file_path = os.path.join(dashboards_dir, dashboard_file)
        
        if os.path.exists(file_path):
            if fix_full_report_button_styling(file_path):
                print(f"✅ Fixed button styling: {dashboard_file}")
                fixed_count += 1
            else:
                print(f"❌ Failed to fix: {dashboard_file}")
        else:
            print(f"⚠️  File not found: {dashboard_file}")
    
    return fixed_count

if __name__ == "__main__":
    print("🔧 Fixing Full Report button styling to match Home button...")
    print("📝 Changes:")
    print("   • Reducing padding from 20px 40px to 10px 20px")
    print("   • Changing font-size from 1.2em to 1em")
    print("   • Changing font-weight from 700 to 500")
    print("   • Removing gradient background, using simple #f5f5dc")
    print("   • Reducing hover effects to match Home button")
    print("   • Removing emoji from button text")
    print()
    
    count = fix_all_dashboard_buttons()
    
    print(f"\n🎉 Button styling fix completed!")
    print(f"✅ Successfully fixed: {count}/{len(updated_dashboards)} dashboards")
    print(f"💫 Full Report buttons now match Home button styling!")