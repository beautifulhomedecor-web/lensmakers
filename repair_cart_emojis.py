import re

path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\CartScreen.js'

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = [
    (r"Home \?\?", r"Home 🏠"),
    (r"Work \?\?", r"Work 🏢"),
    (r"image: '\?\?'", r"image: '👓'"), # Most common frame
    (r"image: '👓'", r"image: '👓'"), # placeholder if needed
    (r"icon: '\?\?'(.*?)UPI", r"icon: '⚡'\1UPI"),
    (r"icon: '\?\?'(.*?)HDFC", r"icon: '💳'\1HDFC"),
    (r"icon: '\?\?'(.*?)Apple", r"icon: '🍏'\1Apple"),
    (r"icon: '\?\?'(.*?)Pay on Delivery", r"icon: '💵'\1Pay on Delivery"),
    (r"🛍\?\? Continue Shopping", r"🛍️ Continue Shopping"),
    (r"\?\? Continue Shopping", r"🛍️ Continue Shopping"),
    (r"\?\? Track Order", r"📍 Track Order"),
    (r"\?\? Copied Order", r"📋 Copied Order"),
    (r"\?\? Confirmation sent", r"📧 Confirmation sent"),
    (r"fontSize: '32px' \}\}>\?\?\<", r"fontSize: '32px' }}>📦<"),
    (r"fontSize: '24px' \}\}>\?\?\<", r"fontSize: '24px' }}>🎁<"),
    (r"fontSize: '28px' \}\}>\?\?\<", r"fontSize: '28px' }}>🔬<"),
    (r"fontSize: '26px' \}\}>\?\?\<", r"fontSize: '26px' }}>👓<"),
    (r"fontSize: '42px', flexShrink: 0 \}\}>\s*\?\?\s*\<", r"fontSize: '42px', flexShrink: 0 }}>\n                    👓\n                  <"),
    (r"fontSize: '30px' \}\}>\s*\?\?\s*\<", r"fontSize: '30px' }}>\n                    👓\n                  <"),
    (r"Order Placed! \?\?", r"Order Placed! 🎉"),
    (r"\?\? BOGO 2nd Pair", r"🎁 BOGO 2nd Pair"),
    (r"\?\? FREE BOGO PAIR", r"🎁 FREE BOGO PAIR"),
    (r"\?\? PAIR #2", r"🎁 PAIR #2"),
    (r"Part of your BOGO offer \?\?", r"Part of your BOGO offer 🎁"),
    (r"\?\? You save", r"🎉 You save"),
    (r"\?\? Member Discount", r"👑 Member Discount"),
    (r"\?\? VIP Club Discount", r"👑 VIP Club Discount"),
    (r"\?\? Promo Code", r"🎉 Promo Code"),
    (r"\?\? Included:", r"🕶️ Included:"),
    (r"\?\? Rx:", r"👁️ Rx:"),
    (r"\?\? Lens Type:", r"✨ Lens Type:"),
    (r"\?\? Need to attach", r"📄 Need to attach"),
    (r"\?\? Edit Lenses", r"✏️ Edit Lenses"),
    (r"\?\? 100% Free Zeiss", r"🚀 100% Free Zeiss"),
    (r"\?\? Express Zeiss", r"🚀 Express Zeiss"),
    (r"\?\? Secure checkout", r"🔒 Secure checkout"),
    (r"\?\? 256-Bit SSL", r"🛡️ 256-Bit SSL"),
    (r"\?\? Remove", r"🗑️ Remove"),
    (r"\?\? Save for Later", r"♡ Save for Later"),
    (r"\?\? Saved Items", r"🔖 Saved Items"),
    (r"Choose Free Frame  ", r"Choose Free Frame →"),
    (r"Browse Frames  ", r"Browse Frames →"),
    (r"Continue to Lens Details  ", r"Continue to Lens Details →"),
    (r"Continue to Final Review  ", r"Continue to Final Review →"),
    (r"Proceed to Checkout \· (.*?)  ", r"Proceed to Checkout · \1 →"),
    (r"Join for \?99", r"Join for ₹99"),
    (r"\?(\d+)", r"₹\1"), # Any stray ? before a number is likely a rupee symbol
    (r"\?\? Opening", r"💳 Opening"),
    (r"\?\? Add New Delivery", r"📝 Add New Delivery"),
]

for old, new in replacements:
    text = re.sub(old, new, text)

# Specifically fix the main cart icon
text = re.sub(r"fontSize: '40px', margin: '0 auto 16px', border: '1px solid rgba\(255,255,255,0\.1\)' \}\}>\s*\?\?\s*\<", r"fontSize: '40px', margin: '0 auto 16px', border: '1px solid rgba(255,255,255,0.1)' }}>\n            🛒\n          <", text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Restored emojis successfully.")
