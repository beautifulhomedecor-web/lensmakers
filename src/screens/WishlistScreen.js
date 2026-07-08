// WISHLIST SCREEN
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
                <div key={item.id} className="product-card-glass" onClick={() => onSelectTab("shop")}>
                    {/* TOP IMAGE AREA (1:1 White Inset) */}
                    <div className="white-surface-inset">
                      {/* Discount / BOGO Badges */}
                      <div style={{ position: 'absolute', top: '8px', left: '8px', display: 'flex', flexDirection: 'column', gap: '4px', zIndex: 5 }}>
                        {item.discount && (
                          <span style={{ background: 'var(--color-accent-primary)', color: 'var(--color-text-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: '0 2px 6px var(--color-shadow)' }}>
                            {item.discount}
                          </span>
                        )}
                        {(item.bogo || item.price >= 1699) && (
                          <span style={{ background: 'var(--color-accent-primary)', color: 'var(--color-text-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900', boxShadow: '0 2px 6px var(--color-shadow)' }}>
                            BOGO FREE
                          </span>
                        )}
                      </div>

                      {/* Wishlist Heart Button */}
                      <button
                        type="button"
                        className={`wishlist-circle-btn heart-btn ${true ? 'saved'}`}
                        onClick={(e) => { e.stopPropagation(); setWishlist(wishlist.filter(id => id !== item.id)); }}
                      >
                        <span className="heart-icon" style={{ fontSize: '16px', color: true ? 'var(--color-accent-primary)' : 'var(--color-bg-primary)', transition: 'all 200ms ease' }}>
                          {true ? '♥' : '♡'}
                        </span>
                      </button>

                      {/* Product Visual (Emoji/Thumbnail simulated with tint) */}
                      <div style={{ fontSize: '64px', filter: `drop-shadow(0 8px 12px var(--color-shadow))` }}>
                        {item.image}
                      </div>

                      {/* Sale Ribbon Corner */}
                      {item.sale && (
                        <div style={{ position: 'absolute', bottom: '6px', right: '6px', background: 'rgba(1,62,55, 0.15)', color: 'var(--color-text-primary)', padding: '2px 6px', borderRadius: '6px', fontSize: '9px', fontWeight: '800' }}>
                          SALE ITEM
                        </div>
                      )}
                    </div>

                    {/* BOTTOM INFO AREA */}
                    <div style={{ padding: '14px 14px 16px', display: 'flex', flexDirection: 'column', flex: 1, justifyContent: 'space-between' }}>
                      <div>
                        <div style={{ fontSize: '10px', fontWeight: '700', color: 'var(--color-text-secondary)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                          {item.brand}
                        </div>
                        <h3 style={{ fontSize: '14px', fontWeight: '800', color: 'var(--color-text-primary)', margin: '4px 0 8px', lineHeight: '1.3', display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden', minHeight: '36px' }}>
                          {item.name}
                        </h3>

                        {/* Color Swatches Row */}
                        <div style={{ display: 'flex', gap: '6px', marginBottom: '10px', alignItems: 'center', minHeight: '18px' }}>
                          {item.colors.map((hex, idx) => (
                            <span
                              key={idx}
                              className={`swatch-dot ${false ? 'selected'}`}
                              style={{ background: hex }}
                              onClick={(e) => {
                                e.stopPropagation();
                                null;
                              }}
                              title={`Switch to color variant ${idx + 1}`}
                            />
                          ))}
                        </div>
                      </div>

                      {/* Price Row & Add to Cart */}
                      <div className="flex-between" style={{ alignItems: 'flex-end', marginTop: '4px' }}>
                        <div>
                          {window.userIsMember !== false ? (
                            <>
                              <div style={{ display: 'flex', alignItems: 'baseline', gap: '6px' }}>
                                <span style={{ fontSize: '16px', fontWeight: '900', color: 'var(--color-text-primary)' }}>₹{memberPrice}</span>
                                <span style={{ fontSize: '12px', color: 'var(--color-text-secondary)', textDecoration: 'line-through' }}>₹{item.price}</span>
                              </div>
                              <div style={{ fontSize: '10px', fontWeight: '800', color: 'var(--color-text-primary)', background: 'rgba(67,160,71,0.15)', padding: '2px 6px', borderRadius: '4px', display: 'inline-block', marginTop: '2px' }}>
                                ★ YOUR VIP PRICE
                              </div>
                            </>
                          ) : (
                            <>
                              <div style={{ display: 'flex', alignItems: 'baseline', gap: '6px' }}>
                                <span style={{ fontSize: '16px', fontWeight: '900', color: 'var(--color-text-primary)' }}>₹{item.price}</span>
                                {item.originalPrice && (
                                  <span style={{ fontSize: '12px', color: 'var(--color-text-secondary)', textDecoration: 'line-through' }}>₹{item.originalPrice}</span>
                                )}
                              </div>
                              <div style={{ fontSize: '11px', fontWeight: '700', color: 'var(--color-text-primary)', marginTop: '2px' }}>
                                Members: ₹{memberPrice}
                              </div>
                            </>
                          )}
                        </div>

                        {/* Small Pink Glass Cart Button */}
                        <button
                          type="button"
                          style={{
                            width: '34px', height: '34px', borderRadius: '50%',
                            background: 'linear-gradient(135deg, var(--color-accent-primary) 0%, var(--color-accent-primary) 100%)',
                            border: 'none', color: 'var(--color-text-primary)', display: 'flex', alignItems: 'center', justifyContent: 'center',
                            cursor: 'pointer', boxShadow: '0 4px 12px 

  '
                          }}
                          onClick={(e) => { e.stopPropagation(); alert("Added to cart!"); }}
                          title="Add to Cart"
                        >
                          🛒
                        </button>
                      </div>
                    </div>
                  </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
};

window.WishlistScreen = WishlistScreen;
