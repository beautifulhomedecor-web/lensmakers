// Lensmakers Promo Card Component (Summer Collection + Orange LENS20 Chip + Checklist)

const { useState } = React;

window.PromoCard = function PromoCard({ onApplyCode }) {
  const [copied, setCopied] = useState(false);

  const handleCopyCode = () => {
    navigator.clipboard?.writeText('LENS20');
    setCopied(true);
    if (onApplyCode) onApplyCode('LENS20');
    setTimeout(() => setCopied(false), 3000);
  };

  return (
    <section className="px-5 my-8">
      <div 
        className="glass-panel p-6 relative overflow-hidden shadow-2xl group"
        style={{
          background: 'var(--color-glass-surface)',
          borderColor: 'var(--color-glass-border)',
          borderWidth: '1px',
          borderStyle: 'solid'
        }}
      >
        
        {/* Warm-toned gradient overlay & sunburst aura using tokens */}
        <div className="absolute top-0 right-0 w-72 h-72 rounded-full blur-3xl pointer-events-none" style={{ background: 'var(--color-accent-tint)' }}></div>
        <div className="absolute -bottom-12 -left-12 w-48 h-48 rounded-full blur-2xl pointer-events-none" style={{ background: 'var(--color-accent-tint)' }}></div>

        {/* Content Container */}
        <div className="relative z-10">
          
          {/* Header */}
          <div className="flex items-center justify-between mb-2">
            <span className="text-[11px] font-extrabold uppercase tracking-widest flex items-center" style={{ color: 'var(--color-accent-primary)' }}>
              <span className="w-2 h-2 rounded-full mr-2 animate-ping" style={{ background: 'var(--color-accent-primary)' }}></span>
              LIMITED TIME OFFER
            </span>
            <span className="text-xs font-semibold" style={{ color: 'var(--color-text-secondary)' }}>Ends in 3 days</span>
          </div>

          <h2 className="font-heading font-extrabold text-2xl sm:text-3xl tracking-tight mb-3 drop-shadow" style={{ color: 'var(--color-text-primary)' }}>
            SUMMER COLLECTION
          </h2>

          {/* Discount text with highlighted chip */}
          <div className="flex flex-wrap items-center gap-2 text-sm sm:text-base font-medium mb-5" style={{ color: 'var(--color-text-primary)' }}>
            <span>Get 20% off your first order with code</span>
            <button 
              onClick={handleCopyCode}
              className="px-3 py-1 rounded-lg font-heading font-extrabold tracking-wider text-base btn-spring flex items-center space-x-1.5"
              style={{
                background: 'var(--color-accent-primary)',
                color: 'var(--color-bg-primary)',
                boxShadow: 'var(--color-shadow)',
                border: '1px solid var(--color-glass-border)'
              }}
              title="Click to copy & apply code"
            >
              <span>LENS20</span>
              <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                {copied ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2" />
                )}
              </svg>
            </button>
            {copied && (
              <span className="text-xs font-bold animate-fade-in-up" style={{ color: 'var(--color-success)' }}>
                ✓ Copied & Applied!
              </span>
            )}
          </div>

          {/* Checklist below with success checkmarks */}
          <div className="pt-4 flex flex-wrap items-center gap-6 text-sm font-semibold" style={{ borderTop: '1px solid var(--color-glass-border)', color: 'var(--color-text-primary)' }}>
            <div className="flex items-center space-x-2">
              <div className="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style={{ background: 'var(--color-accent-tint)', color: 'var(--color-success)', border: '1px solid var(--color-glass-border)' }}>
                <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <span>Free Shipping</span>
            </div>

            <div className="flex items-center space-x-2">
              <div className="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style={{ background: 'var(--color-accent-tint)', color: 'var(--color-success)', border: '1px solid var(--color-glass-border)' }}>
                <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <span>1-Year Warranty</span>
            </div>

            <div className="flex items-center space-x-2">
              <div className="w-5 h-5 rounded-full flex items-center justify-center flex-shrink-0" style={{ background: 'var(--color-accent-tint)', color: 'var(--color-success)', border: '1px solid var(--color-glass-border)' }}>
                <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                </svg>
              </div>
              <span>14-Day Free Returns</span>
            </div>
          </div>

        </div>
      </div>
    </section>
  );
};
