import re

shop_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\ShopScreen.js'
wishlist_path = r'c:\Users\NEW\OneDrive\Desktop\lensmakers-web\src\screens\WishlistScreen.js'

with open(shop_path, 'r', encoding='utf-8') as f:
    shop_content = f.read()

# Extract the product card
start_marker = '<div key={item.id} className="product-card-glass"'
end_marker = '</div>\n                  </div>\n                );'
start_idx = shop_content.find(start_marker)
end_idx = shop_content.find(end_marker, start_idx) + len('</div>\n                  </div>')

product_card_markup = shop_content[start_idx:end_idx]

# Replace some functions since we won't have them in WishlistScreen
product_card_markup = product_card_markup.replace('onClick={() => handleOpenPdp(item)}', 'onClick={() => onSelectTab("shop")}')
product_card_markup = product_card_markup.replace('onClick={(e) => handleToggleWishlist(e, item.id)}', 'onClick={(e) => { e.stopPropagation(); setWishlist(wishlist.filter(id => id !== item.id)); }}')
product_card_markup = product_card_markup.replace('onClick={(e) => handleAddToCart(e, item)}', 'onClick={(e) => { e.stopPropagation(); alert("Added to cart!"); }}')

# Clean up states
product_card_markup = product_card_markup.replace('activeColor === hex', 'false')
product_card_markup = product_card_markup.replace('setActiveColors((prev) => ({ ...prev, [item.id]: hex }))', 'null')
product_card_markup = product_card_markup.replace('isSaved ?', 'true ?')
product_card_markup = product_card_markup.replace('${isSaved ? \'saved\' : \'\'}', '${true ? \'saved\' : \'\'}')

wishlist_screen = """// WISHLIST SCREEN
const { useState, useEffect } = React;

const WishlistScreen = ({ onSelectTab }) => {
  // Mock wishlist data from ShopScreen
  const [wishlist, setWishlist] = useState(['101', '409']);
  
  const MOCK_PRODUCTS = [
    { id: '101', name: 'Aerospace Lite Titanium #101', brand: 'Lens Makers', price: 4999, originalPrice: 6999, sale: true, bogo: true, colors: ['#D4AF37', '#C0C0C0', '#2C3E50'], image: '🕶️' },
    { id: '409', name: 'Vintage Tortoiseshell #409', brand: 'Lens Makers', price: 3499, originalPrice: 4299, colors: ['#8B4513', '#A0522D', '#D2691E'], image: '👓', discount: '-18%' },
  ];

  const wishlistItems = MOCK_PRODUCTS.filter(p => wishlist.includes(p.id));

  return (
    <div className="fade-in-item" style={{ paddingBottom: '120px', minHeight: '100vh', background: 'var(--color-bg-primary)' }}>
      {/* Top Header Spacing */}
      <div style={{ height: '70px' }} />
      <div style={{ padding: 'var(--screen-padding)' }}>
        <h1 style={{ fontSize: '28px', fontWeight: '900', color: 'var(--color-text-primary)', marginBottom: '8px', letterSpacing: '-0.5px' }}>
          My Wishlist
        </h1>
        <p style={{ fontSize: '13px', color: 'var(--color-text-secondary)', marginBottom: '24px' }}>
          {wishlist.length} items saved
        </p>

        {wishlist.length === 0 ? (
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '50vh' }}>
            <div style={{ 
              background: 'var(--color-glass-surface)', 
              width: '80px', height: '80px', 
              borderRadius: '50%', 
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              marginBottom: '24px'
            }}>
              <i data-lucide="heart" style={{ width: '40px', height: '40px', color: 'var(--color-accent-primary)', fill: 'var(--color-accent-primary)' }}></i>
            </div>
            <h2 style={{ fontSize: '20px', fontWeight: '800', color: 'var(--color-text-primary)', marginBottom: '8px' }}>
              Your wishlist is empty
            </h2>
            <p style={{ fontSize: '14px', color: 'var(--color-text-secondary)', marginBottom: '32px' }}>
              Save items you love here
            </p>
            <button 
              onClick={() => onSelectTab('shop')}
              style={{
                background: 'var(--color-accent-primary)',
                color: 'var(--color-bg-primary)',
                border: 'none',
                padding: '16px 32px',
                borderRadius: '999px',
                fontSize: '15px',
                fontWeight: '800',
                cursor: 'pointer',
                boxShadow: '0 8px 24px var(--color-shadow)',
                transition: 'transform 200ms ease'
              }}
            >
              Browse Frames
            </button>
          </div>
        ) : (
          <div className="product-grid-2col">
            {wishlistItems.map(item => {
              const memberPrice = Math.floor(item.price * 0.75);
              return (
                __PRODUCT_CARD_MARKUP__
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
};

window.WishlistScreen = WishlistScreen;
"""

wishlist_screen = wishlist_screen.replace('__PRODUCT_CARD_MARKUP__', product_card_markup)

with open(wishlist_path, 'w', encoding='utf-8') as f:
    f.write(wishlist_screen)

print("WishlistScreen.js created successfully.")
