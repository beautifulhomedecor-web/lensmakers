// Bottom Navigation Bar Component — Pure White Dock, Deep Green-Black Text
const { useState, useEffect } = React;

const BottomNav = ({ activeTab, onSelectTab, cartCount = 2 }) => {
  const [pressedTabId, setPressedTabId] = useState(null);

  const getMainTabId = (route) => {
    if (['home', 'stores', 'eyetest', 'membership', 'welcomeclub', 'manageclub', 'tryon'].includes(route)) return 'home';
    if (['shop', 'explore', 'category'].includes(route)) return 'explore';
    if (['wishlist'].includes(route)) return 'wishlist';
    if (['cart', 'trackorder', 'orders'].includes(route)) return 'orders';
    if (['profile', 'prescription', 'rx_add', 'rx_checkout', 'settings', 'trackappt'].includes(route)) return 'profile';
    return route;
  };

  const activeMainTab = getMainTabId(activeTab);

  const tabs = [
    { id: 'home',    label: 'Home',     icon: 'home' },
    { id: 'explore', label: 'Explore',  icon: 'compass' },
    { id: 'wishlist',label: 'Wishlist', icon: 'heart' },
    { id: 'orders',  label: 'Orders',   icon: 'shopping-bag', badge: cartCount > 0 ? cartCount : 2 },
    { id: 'profile', label: 'Profile',  icon: 'user' },
  ];

  useEffect(() => {
    if (window.lucide && window.lucide.createIcons) {
      window.lucide.createIcons();
      setTimeout(() => {
        if (window.lucide && window.lucide.createIcons) window.lucide.createIcons();
      }, 15);
    }
  }, [activeMainTab]);

  const handleTabClick = (tabId) => {
    setPressedTabId(tabId);
    setTimeout(() => setPressedTabId(null), 250);
    if (onSelectTab) {
      if (tabId === 'explore') onSelectTab('shop');
      else if (tabId === 'orders') onSelectTab('cart');
      else if (tabId === 'wishlist') onSelectTab('wishlist');
      else onSelectTab(tabId);
    }
  };

  return (
    <nav
      className="bottom-nav nav-visible dark-anchor"
      style={{
        background: 'var(--color-glass-surface)',
        backdropFilter: 'blur(20px)',
        WebkitBackdropFilter: 'blur(20px)',
        borderTop: '1px solid var(--color-glass-border)',
        boxShadow: '0 -4px 24px var(--color-shadow)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-around',
        padding: '8px 4px 16px 4px',
        position: 'fixed',
        bottom: 0,
        left: 0,
        right: 0,
        width: '100%',
        maxWidth: '480px',
        margin: '0 auto',
        zIndex: 1000
      }}
    >
      {tabs.map((tab) => {
        const isActive = activeMainTab === tab.id;
        const isPressed = pressedTabId === tab.id;

        return (
          <div
            key={tab.id}
            onClick={() => handleTabClick(tab.id)}
            style={{
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              flex: 1,
              cursor: 'pointer',
              userSelect: 'none',
              transform: isPressed ? 'scale(0.88)' : 'scale(1)',
              transition: 'transform 280ms var(--spring-bezier)',
              padding: '4px 0',
              position: 'relative'
            }}
          >
            <div style={{ position: 'relative', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
              <i
                data-lucide={tab.icon}
                style={{
                  width: '22px',
                  height: '22px',
                  color: isActive ? 'var(--color-text-primary)' : 'var(--color-text-secondary)',
                  strokeWidth: isActive ? '2.5px' : '1.8px',
                  transition: 'color 200ms ease',
                  transform: 'none',
                  flexShrink: 0
                }}
              />
              {tab.badge > 0 && (
                <span
                  style={{
                    position: 'absolute',
                    top: '-5px',
                    right: '-10px',
                    background: 'var(--color-accent-primary)',
                    color: 'var(--color-bg-primary)',
                    fontSize: '10px',
                    fontWeight: '900',
                    minWidth: '16px',
                    height: '16px',
                    borderRadius: '8px',
                    padding: '0 4px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    boxShadow: 'none',
                    lineHeight: 1,
                    zIndex: 10
                  }}
                >
                  {tab.badge}
                </span>
              )}
            </div>

            <span
              style={{
                fontSize: '11px',
                fontWeight: isActive ? '700' : '500',
                color: isActive ? 'var(--color-text-primary)' : 'var(--color-text-secondary)',
                marginTop: '4px',
                letterSpacing: '0.2px',
                transition: 'color 200ms ease'
              }}
            >
              {tab.label}
            </span>

            {/* Active indicator pill */}
            {isActive && (
              <span
                style={{
                  position: 'absolute',
                  bottom: '-4px',
                  width: '20px',
                  height: '3px',
                  borderRadius: '2px',
                  background: 'var(--color-accent-primary)',
                  transition: 'opacity 200ms ease'
                }}
              />
            )}
          </div>
        );
      })}
    </nav>
  );
};

window.BottomNav = BottomNav;
