import re

app_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\App.js'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

bad_snippet = """              {activeTab === 'tryon' && (
              )}
              {activeTab === 'trackappt' && ("""

good_snippet = """              {activeTab === 'tryon' && (
                <window.TryOnScreen onSelectTab={handleSelectTab} />
              )}
              {activeTab === 'cart' && (
                <window.CartScreen onSelectTab={handleSelectTab} />
              )}
              {activeTab === 'profile' && (
                <window.ProfileScreen
                  onLogout={handleLogout}
                  onReplayOnboarding={handleReplayOnboarding}
                  onSelectTab={handleSelectTab}
                />
              )}
              {activeTab === 'wishlist' && (
                <window.WishlistScreen onSelectTab={handleSelectTab} />
              )}
              {activeTab === 'eyetest' && (
                <window.EyeCheckupScreen onSelectTab={handleSelectTab} initialViewMode="landing" />
              )}
              {activeTab === 'trackorder' && (
                <window.EyeCheckupScreen onSelectTab={handleSelectTab} initialViewMode="order_tracking" />
              )}
              {activeTab === 'trackappt' && ("""

content = content.replace(bad_snippet, good_snippet)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored App.js")
