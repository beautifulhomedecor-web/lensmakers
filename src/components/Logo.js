// Logo Component — Exact Lensmakers Logo with Anti-Gravity Zero-G Floating Effect
const { useState, useEffect } = React;

const Logo = ({ iconOnly = false, size = 36, onClick }) => {
  // Use exact custom size or default height
  const h = iconOnly ? (size || 32) : size;
  const fontSize = Math.round(h * 0.72);

  // Inject anti-gravity zero-G keyframe animation styles once
  useEffect(() => {
    if (!document.getElementById('anti-gravity-logo-styles')) {
      const styleEl = document.createElement('style');
      styleEl.id = 'anti-gravity-logo-styles';
      styleEl.innerHTML = `
        @keyframes zeroGravityDrift {
          0% {
            transform: translate3d(0px, 0px, 0px) rotate(-3.5deg) scale(1);
            filter: drop-shadow(0 4px 12px rgba(1,62,55, 0.45));
          }
          20% {
            transform: translate3d(3px, -6px, 0px) rotate(2deg) scale(1.04);
            filter: drop-shadow(0 10px 18px rgba(118, 255, 3, 0.55));
          }
          40% {
            transform: translate3d(-5px, -10px, 0px) rotate(-1.5deg) scale(1.07);
            filter: drop-shadow(0 14px 24px rgba(1,62,55, 0.65));
          }
          60% {
            transform: translate3d(-4px, -4px, 0px) rotate(3deg) scale(1.03);
            filter: drop-shadow(0 8px 16px rgba(204, 255, 0, 0.5));
          }
          80% {
            transform: translate3d(2px, -2px, 0px) rotate(-2deg) scale(1.02);
            filter: drop-shadow(0 6px 14px rgba(1,62,55, 0.45));
          }
          100% {
            transform: translate3d(0px, 0px, 0px) rotate(-3.5deg) scale(1);
            filter: drop-shadow(0 4px 12px rgba(1,62,55, 0.45));
          }
        }

        .anti-gravity-floating {
          animation: zeroGravityDrift 7s ease-in-out infinite alternate;
          will-change: transform, filter;
          transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.4s ease;
        }

        .anti-gravity-floating:hover {
          transform: scale(1.12) rotate(0deg) translate3d(0px, -4px, 0px) !important;
          filter: drop-shadow(0 16px 28px 
    param($m)
    $opacity = $m.Groups[1].Value
    "rgba(11,31,28,0.$opacity)"
  ) drop-shadow(0 0 15px rgba(118, 255, 3, 0.6)) !important;
          animation-play-state: paused;
        }
      `;
      document.head.appendChild(styleEl);
    }
  }, []);

  return (
    <div
      className="logo-container"
      onClick={onClick}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: '8px',
        cursor: onClick ? 'pointer' : 'default',
        userSelect: 'none',
        padding: '2px'
      }}
    >
      {/* =========================================================================
          SVG DUAL-CIRCLE BRANDING (Cyan/Blue & Lime-Green strokes per Section 1)
          ========================================================================= */}
      <div
        className="anti-gravity-floating"
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          flexShrink: 0
        }}
        title="Lensmakers"
      >
        <img src="./logo-3d.png" alt="Lensmakers Logo" style={{ height: `${h * 1.5}px`, objectFit: 'contain' }} />
      </div>

      {/* =========================================================================
          CRISP WHITE SANS-SERIF TEXT: "lensmakers" per Section 1
          ========================================================================= */}
      {!iconOnly && (
        <span
          className="logo-wordmark"
          style={{
            fontFamily: "'Outfit', 'Inter', -apple-system, sans-serif",
            fontWeight: 800,
            fontSize: `${fontSize}px`,
            letterSpacing: '-0.6px',
            whiteSpace: 'nowrap',
            display: 'inline-flex',
            alignItems: 'center',
            lineHeight: 1
          }}
        >
          <span style={{ color: 'var(--color-text-primary)' }}>lens</span>
          <span style={{ color: '#C2FF27' }}>makers</span>
        </span>
      )}
    </div>
  );
};

window.Logo = Logo;
