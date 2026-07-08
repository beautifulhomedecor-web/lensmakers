// Top Header Bar Component — Exact Mobile App Layout (Image 3)
const { useState, useEffect } = React;

const Header = ({ onLogoClick, onSelectTab, onNotificationClick, onLogout, activeTab, selectedLocation = 'Hyderabad', onOpenLocation }) => {
  const [searchQuery, setSearchQuery] = useState('');
  const [debouncedQuery, setDebouncedQuery] = useState('');
  const [hasUnreadNotifs, setHasUnreadNotifs] = useState(true);
  const [isListening, setIsListening] = useState(false);
  const [voiceTranscript, setVoiceTranscript] = useState('');
  const [isSearchFocused, setIsSearchFocused] = useState(false);

  // Debounce search input (300ms)
  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedQuery(searchQuery.trim().toLowerCase());
    }, 300);
    return () => clearTimeout(timer);
  }, [searchQuery]);

  useEffect(() => {
    if (window.lucide && window.lucide.createIcons) {
      setTimeout(() => window.lucide.createIcons(), 30);
    }
  }, [isListening, searchQuery, activeTab]);



  // Sample catalog & services for live autocomplete
  const autocompleteSource = [
    { type: 'product', name: 'Aerospace Lite Titanium #101', sub: 'Eyeglasses • ₹4,999', thumb: '🕶️', tab: 'shop' },
    { type: 'product', name: 'Milan Aviator Gold #204', sub: 'Sunglasses • ₹3,499', thumb: '🥽', tab: 'shop' },
    { type: 'product', name: 'Tortoise Classic #305', sub: 'Premium • ₹3,899', thumb: '👓', tab: 'shop' },
    { type: 'product', name: 'Carbon Square #09', sub: 'Eyeglasses • ₹5,499', thumb: '🕶️', tab: 'shop' },
    { type: 'category', name: 'Eyeglasses (340+ Frames)', sub: 'Category • Blue Filter & Prescription', icon: 'glasses', tab: 'shop' },
    { type: 'category', name: 'Sunglasses (UV400 Luxury)', sub: 'Category • Polarized & Aviator', icon: 'sun', tab: 'shop' },
    { type: 'category', name: 'Contact Lenses & Care', sub: 'Category • Daily & Monthly Disposable', icon: 'eye', tab: 'shop' },
    { type: 'service', name: '3D AR Virtual Try-On', sub: 'Service • Real-time AI Face Scan', icon: 'camera', tab: 'tryon' },
    { type: 'service', name: 'Free Online Eye Check-Up', sub: 'Service • Certified Optometrist Consult', icon: 'profile' },
    { type: 'service', name: 'Lensmakers VIP Club Membership', sub: 'Service • Flat 25% Off Everything for ₹99', icon: 'award', tab: 'profile' }
  ];

  // Filter matched results
  const matchedResults = debouncedQuery
    ? autocompleteSource.filter(item =>
        item.name.toLowerCase().includes(debouncedQuery) ||
        item.sub.toLowerCase().includes(debouncedQuery)
      ).slice(0, 7)
    : [];

  const handleSelectResult = (item) => {
    setSearchQuery('');
    if (item.type === 'product') {
      window._selectedPdpName = item.name;
    }
    if (onSelectTab) onSelectTab(item.tab || 'shop');
  };

  return (
    <>
      <header
        className="top-header-wrapper dark-anchor"
        style={{
          position: 'relative',
          top: 0,
          left: 0,
          right: 0,
          margin: 0,
          width: '100%',
          maxWidth: '100%',
          zIndex: 100,
          background: 'var(--color-glass-surface)',
          backdropFilter: 'blur(24px) saturate(1.8)',
          WebkitBackdropFilter: 'blur(24px) saturate(1.8)',
          borderBottom: '1px solid var(--color-glass-border)',
          border: 'none',
          borderRadius: 0,
          boxShadow: 'none',
          padding: activeTab === 'home' ? '16px var(--screen-padding) 4px var(--screen-padding)' : '16px var(--screen-padding) 12px var(--screen-padding)',
          transition: 'all 300ms var(--spring-bezier)'
        }}
      >
        {/* =========================================================================
            TOP HEADER ASSETS (Row 1: Hamburger, Logo, Bell per Section 1)
            ========================================================================= */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', width: '100%', marginBottom: '14px' }}>
          {/* Top-left hamburger menu bars (Solid white var(--color-bg-primary)) */}
          <button
            type="button"
            onClick={() => onSelectTab && onSelectTab('explore')}
            style={{
              background: 'transparent',
              border: 'none',
              padding: '6px',
              cursor: 'pointer',
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
              gap: '5px',
              width: '36px',
              height: '36px',
              flexShrink: 0
            }}
            title="Menu / Explore"
          >
            <span style={{ width: '22px', height: '2.5px', background: 'var(--color-accent-primary)', borderRadius: '2px', display: 'block' }} />
            <span style={{ width: '16px', height: '2.5px', background: 'var(--color-accent-primary)', borderRadius: '2px', display: 'block' }} />
            <span style={{ width: '22px', height: '2.5px', background: 'var(--color-accent-primary)', borderRadius: '2px', display: 'block' }} />
          </button>

          {/* Centered Logo */}
          <div onClick={onLogoClick} style={{ cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <window.Logo size={26} />
          </div>

          {/* Top-right notification bell (Solid white var(--color-bg-primary) with lime badge '2') */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexShrink: 0 }}>
            {onLogout && (
              <button
                type="button"
                style={{
                  width: '32px', height: '32px', borderRadius: '16px',
                  background: 'var(--color-glass-surface)', border: '1px solid var(--color-glass-border)', color: 'var(--color-text-primary)', display: 'flex', alignItems: 'center', justifyContent: 'center',
                  cursor: 'pointer', transition: 'all 200ms ease'
                }}
                onClick={onLogout}
                title="Log Out"
              >
                <i data-lucide="log-out" style={{ width: '15px', height: '15px', color: 'var(--color-text-primary)' }} />
              </button>
            )}
            <button
              type="button"
              style={{
                position: 'relative', width: '36px', height: '36px',
                borderRadius: '18px', background: 'var(--color-glass-surface)',
                border: '1px solid var(--color-glass-border)',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
                cursor: 'pointer'
              }}
              onClick={() => {
                setHasUnreadNotifs(false);
                if (onNotificationClick) onNotificationClick();
              }}
              title="Notifications"
            >
              <i data-lucide="bell" style={{ width: '18px', height: '18px', color: 'var(--color-text-primary)' }} />
              {hasUnreadNotifs && (
                <span
                  style={{
                    position: 'absolute', top: '-2px', right: '-2px',
                    minWidth: '18px', height: '18px', borderRadius: '9px',
                    background: 'var(--color-accent-primary)', color: 'var(--color-bg-primary)',
                    fontSize: '11px', fontWeight: '900',
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    padding: '0 4px', boxShadow: '0 2px 6px var(--color-accent-tint)',
                    lineHeight: 1
                  }}
                >
                  2
                </span>
              )}
            </button>
          </div>
        </div>

        {/* =========================================================================
            LOCATION DROPDOWN (Centered below logo per Section 1)
            ========================================================================= */}
        <div style={{ display: 'flex', justifyContent: 'center', width: '100%' }}>
          <button
            type="button"
            onClick={() => onOpenLocation && onOpenLocation()}
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '6px',
              padding: '6px 14px',
              borderRadius: '999px',
              background: 'var(--color-glass-surface)',
              border: '1px solid var(--color-glass-border)',
              color: 'var(--color-text-primary)',
              fontSize: '13px',
              fontWeight: '600',
              cursor: 'pointer',
              transition: 'all 200ms ease'
            }}
          >
            <i data-lucide="map-pin" style={{ width: '14px', height: '14px', color: 'var(--color-text-primary)' }} />
            <span>{selectedLocation || 'Hyderabad'}</span>
            <i data-lucide="chevron-down" style={{ width: '14px', height: '14px', color: 'var(--color-text-primary)' }} />
          </button>
        </div>
      </header>

      {/* STANDALONE SEARCH BAR (Scrolls with page, shown on Explore/Shop tabs) */}
      {activeTab !== 'home' && (
        <div className="standalone-search-container fade-up-item" style={{ padding: '0 20px', marginTop: '6px', marginBottom: '24px', position: 'relative', zIndex: 90 }}>
          <div style={{ position: 'relative', width: '100%', height: '48px', display: 'flex', alignItems: 'center' }}>
            <i
              data-lucide="search"
              style={{
                position: 'absolute', left: '16px', width: '18px', height: '18px',
                color: 'var(--color-accent-primary)', pointerEvents: 'none', zIndex: 2
              }}
            />
            <input
              type="text"
              onFocus={() => setIsSearchFocused(true)}
              onBlur={() => setTimeout(() => setIsSearchFocused(false), 200)}
              style={{
                width: '100%',
                height: '48px',
                paddingLeft: '44px',
                paddingRight: searchQuery ? '110px' : '82px',
                margin: 0,
                borderRadius: '999px',
                fontSize: '14px',
                background: 'var(--color-glass-surface)',
                border: (isListening || isSearchFocused) ? '1.5px solid var(--color-accent-primary)' : '1px solid var(--color-glass-border)',
                color: 'var(--color-text-primary)',
                outline: 'none',
            boxShadow: (isListening || isSearchFocused) ? '0 0 0 3px var(--color-accent-tint), 0 16px 48px var(--color-shadow)' : 'inset 0 2px 4px var(--color-accent-tint)',
            transition: 'all 280ms var(--spring-bezier)'
          }}
          placeholder={isListening ? "🎙️ Listening for voice commands..." : "Search eyeglasses, sunglasses, brands"}
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
        {searchQuery && (
          <button
            style={{
              position: 'absolute', right: '84px', width: '22px', height: '22px',
              borderRadius: '11px', background: 'var(--color-glass-surface)', border: 'none',
              color: 'var(--color-accent-primary)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
              fontSize: '11px', zIndex: 3
            }}
            onClick={() => setSearchQuery('')}
            title="Clear Search"
          >
            ✕
          </button>
        )}

        {/* Voice Search Microphone Icon Button */}
        <button
          className="liquid-btn"
          style={{
            position: 'absolute', right: '50px', top: '8px', width: '32px', height: '32px',
            borderRadius: '16px',
            background: isListening ? 'var(--color-accent-primary)' : 'var(--color-accent-tint)',
            border: (isListening || isSearchFocused) ? '1.5px solid var(--color-accent-primary)' : '1px solid var(--color-glass-border)',
            boxShadow: (isListening || isSearchFocused) ? '0 0 0 3px var(--color-accent-tint), 0 16px 48px var(--color-shadow)' : 'inset 0 2px 4px var(--color-accent-tint)',
            color: 'var(--color-text-primary)', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center',
            transition: 'all 280ms var(--spring-bezier)', zIndex: 3,
            animation: isListening ? 'breatheGlow 1.5s infinite ease-in-out' : 'none'
          }}
          onClick={() => {
            const nextListening = !isListening;
            setIsListening(nextListening);
            if (nextListening) {
              setVoiceTranscript('🎙️ Listening... Say an eyewear brand, style, or command');
              setTimeout(() => {
                if (window.lucide && window.lucide.createIcons) window.lucide.createIcons();
              }, 20);
              setTimeout(() => setVoiceTranscript('“Show Titanium Aviators...”'), 1600);
              setTimeout(() => {
                setSearchQuery('titanium');
                setIsListening(false);
                setVoiceTranscript('');
              }, 3400);
            } else {
              setVoiceTranscript('');
            }
          }}
          title="Voice Search Navigation"
        >
          <i data-lucide="mic" style={{ width: '16px', height: '16px', color: isListening ? 'var(--color-bg-primary)' : 'var(--color-accent-primary)', transition: 'color 200ms ease' }} />
        </button>

        {/* Right side: notification bell in its own glass-circle (36px diameter) positioned 8px from right inside the bar */}
        <button
          className="liquid-btn"
          style={{
            position: 'absolute', right: '8px', top: '6px', width: '36px', height: '36px',
            borderRadius: '18px', background: 'var(--color-glass-surface)',
            border: '1px solid var(--color-glass-border)',
            boxShadow: '0 2px 8px rgba(0,0,0,0.3)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            cursor: 'pointer', zIndex: 3
          }}
          onClick={() => {
            setHasUnreadNotifs(false);
            if (onNotificationClick) onNotificationClick();
          }}
          title="Notifications"
        >
          <i data-lucide="bell" style={{ width: '18px', height: '18px', color: 'var(--color-text-primary)' }} />
          {hasUnreadNotifs && (
            <span
              style={{
                position: 'absolute', top: '6px', right: '6px',
                width: '8px', height: '8px', borderRadius: '4px',
                background: 'var(--color-accent-primary)', boxShadow: '0 0 6px var(--color-accent-tint)'
              }}
            />
          )}
        </button>
      </div>

      {/* AI VOICE NAVIGATION HUD OVERLAY */}
      {isListening && (
        <div 
          className="voice-search-hud fade-up-item"
          style={{
            position: 'absolute', top: '100%', left: 'var(--screen-padding)', right: 'var(--screen-padding)',
            background: 'var(--color-bg-primary)',
            border: '1.5px solid var(--color-glass-border)', borderRadius: '18px', padding: '16px', marginTop: '10px',
            boxShadow: '0 12px 36px var(--color-accent-tint)',
            backdropFilter: 'blur(30px)', zIndex: 300, animation: 'screenFadeSlideIn 300ms forwards'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '12px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--color-text-primary)', fontWeight: '800', fontSize: '12px', letterSpacing: '0.6px' }}>
              AI VOICE NAVIGATION ACTIVE
            </div>
            <button
              onClick={() => setIsListening(false)}
              style={{ background: 'var(--color-accent-tint)', border: '1px solid var(--color-accent-tint)', color: 'var(--color-text-primary)', cursor: 'pointer', width: '24px', height: '24px', borderRadius: '12px', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '12px', fontWeight: 'bold' }}
            >
              ✕
            </button>
          </div>
          <div style={{ padding: '14px', background: 'var(--color-accent-tint)', borderRadius: '12px', color: 'var(--color-text-primary)', fontSize: '14px', textAlign: 'center', fontWeight: '700', marginBottom: '14px', border: '1px dashed var(--color-accent-tint)' }}>
            {voiceTranscript || '🎙️ Listening... Say your command'}
          </div>
          <div style={{ fontSize: '11px', color: 'rgba(11,31,28,0.5)
  ', fontWeight: '700', marginBottom: '10px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
            Try saying or tapping an instant voice command:
          </div>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
            {[
              { label: '🕶️ "Show Titanium Aviators"', query: 'titanium' },
              { label: '👓 "Try on Blue Light glasses"', tab: 'tryon' },
              { label: '👑 "Join ₹99 VIP Club"', tab: 'profile' },
              { label: '📍 "Find Nearby Stores"', tab: 'home' }
            ].map((cmd, i) => (
              <button
                key={i}
                style={{
                  padding: '8px 14px', borderRadius: '20px', background: 'var(--color-glass-surface)',
                  border: '1px solid var(--color-glass-border)', color: 'var(--color-text-primary)', fontSize: '12px', fontWeight: '600',
                  cursor: 'pointer', transition: 'all 200ms ease', display: 'flex', alignItems: 'center', gap: '6px'
                }}
                onClick={() => {
                  setIsListening(false);
                  if (cmd.tab && onSelectTab) onSelectTab(cmd.tab);
                  else if (cmd.query) setSearchQuery(cmd.query);
                }}
              >
                {cmd.label}
              </button>
            ))}
          </div>
        </div>
      )}

      {/* EXPANDED DROPDOWN (Recent & Results) */}
      {(debouncedQuery.length > 0 || isSearchFocused) && (
        <div 
          className="autocomplete-dropdown"
          style={{
            position: 'absolute', top: '100%', left: 'var(--screen-padding)', right: 'var(--screen-padding)',
            background: 'var(--color-bg-primary)',
            border: '1px solid var(--color-glass-border)',
            borderRadius: '16px',
            marginTop: '8px',
            boxShadow: '0 12px 36px var(--color-shadow)',
            overflow: 'hidden',
            zIndex: 999999
          }}
        >
          {/* RECENT SEARCHES */}
          {debouncedQuery.length === 0 && (
            <div style={{ padding: '16px' }}>
              <div style={{ fontSize: '11px', color: 'var(--color-text-secondary)', fontWeight: '700', letterSpacing: '0.8px', marginBottom: '12px' }}>
                RECENT SEARCHES
              </div>
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                {['Titanium', 'Aviator', 'VIP Club', 'Blue Light'].map((term) => (
                  <button
                    key={term}
                    className="recent-search-chip"
                    style={{
                      padding: '6px 14px', borderRadius: '999px', background: 'var(--color-glass-surface)',
                      border: '1px solid var(--color-glass-border)', color: 'var(--color-text-secondary)',
                      fontSize: '12px', fontWeight: '600', cursor: 'pointer', transition: 'all 200ms ease'
                    }}
                    onClick={() => setSearchQuery(term)}
                  >
                    {term}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* SEARCH RESULTS GRID */}
          {debouncedQuery.length > 0 && (
            <div style={{ padding: '16px' }}>
              <div style={{ fontSize: '11px', color: 'var(--color-text-secondary)', fontWeight: '700', letterSpacing: '0.8px', marginBottom: '12px', borderBottom: '1px solid var(--color-glass-border)', paddingBottom: '8px' }}>
                SEARCH RESULTS FOR "{debouncedQuery.toUpperCase()}"
              </div>
              
              {matchedResults.length === 0 ? (
                <div style={{ padding: '24px 0', textAlign: 'center', color: 'var(--color-text-secondary)', fontSize: '13px' }}>
                  No exact matches found. Try searching for "Titanium", "VIP", or "Try-On".
                </div>
              ) : (
                <div className="product-grid-2col">
                  {matchedResults.map((item, index) => {
                    const price = item.sub.includes('₹') ? item.sub.split('₹')[1] : '3,499';
                    const category = item.sub.split(' • ')[0] || item.type;
                    
                    return (
                      <div key={index} className="product-card-glass" onClick={() => handleSelectResult(item)}>
                        <div className="white-surface-inset">
                          <div style={{ position: 'absolute', top: '8px', left: '8px', display: 'flex', flexDirection: 'column', gap: '4px', zIndex: 5 }}>
                            {item.type === 'product' && (
                              <span style={{ background: 'var(--color-accent-primary)', color: 'var(--color-text-primary)', padding: '2px 8px', borderRadius: '999px', fontSize: '10px', fontWeight: '900' }}>
                                BOGO FREE
                              </span>
                            )}
                          </div>
                          <div style={{ fontSize: '64px', filter: 'drop-shadow(0 8px 12px var(--color-shadow))', display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%' }}>
                            {item.thumb || (item.icon === 'camera' ? '📷' : '⭐')}
                          </div>
                        </div>
                        <div style={{ padding: '14px 14px 16px', display: 'flex', flexDirection: 'column', flex: 1, justifyContent: 'space-between' }}>
                          <div>
                            <div style={{ fontSize: '10px', fontWeight: '700', color: 'var(--color-text-secondary)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                              {category}
                            </div>
                            <h3 style={{ fontSize: '14px', fontWeight: '800', color: 'var(--color-text-primary)', margin: '4px 0 8px', lineHeight: '1.3' }}>
                              {item.name}
                            </h3>
                          </div>
                          <div className="flex-between" style={{ alignItems: 'flex-end', marginTop: '4px' }}>
                            <div>
                              <div style={{ display: 'flex', alignItems: 'baseline', gap: '6px' }}>
                                <span style={{ fontSize: '16px', fontWeight: '900', color: 'var(--color-text-primary)' }}>₹{price}</span>
                              </div>
                            </div>
                            <button
                              type="button"
                              style={{
                                width: '34px', height: '34px', borderRadius: '50%',
                                background: 'var(--color-accent-primary)', border: 'none', color: 'var(--color-text-primary)', 
                                display: 'flex', alignItems: 'center', justifyContent: 'center', cursor: 'pointer'
                              }}
                            >
                              →
                            </button>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          )}
        </div>
      )}
      </div>
      )}
    </>
  );
};

window.Header = Header;
