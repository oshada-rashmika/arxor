'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { cn } from '@/lib/utils';
import { NAV_ITEMS, type NavItem, isNavItemActive } from './nav-config';

export interface MobileDockProps {
  items?: readonly NavItem[];
  className?: string;
}

export function MobileDock({ items = NAV_ITEMS, className }: MobileDockProps) {
  const pathname = usePathname();

  return (
    <div
      className={cn(
        'fixed inset-x-0 bottom-0 z-40 md:hidden',
        'border-t border-brand-border/60 bg-white/90 backdrop-blur-xl shadow-[0_-4px_24px_rgba(0,0,0,0.03)] dark:border-border/60 dark:bg-background/90',
        'transition-transform duration-200',
        className,
      )}
      style={{ paddingBottom: 'env(safe-area-inset-bottom, 0px)' }}
    >
      <nav
        role="navigation"
        aria-label="Mobile Bottom Navigation"
        className="mx-auto flex h-16 max-w-md items-center justify-around px-2"
      >
        {items.map((item) => {
          const active = isNavItemActive(pathname, item.href);
          const Icon = item.icon;

          return (
            <Link
              key={item.href}
              href={item.href}
              aria-label={item.label}
              aria-current={active ? 'page' : undefined}
              className={cn(
                'group relative flex min-h-[48px] min-w-[48px] flex-1 flex-col items-center justify-center gap-1 rounded-2xl px-1 py-1 transition-all duration-150',
                'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-forest/20',
                active
                  ? 'text-brand-forest font-semibold'
                  : 'text-brand-muted hover:text-brand-charcoal dark:text-muted-foreground',
              )}
            >
              {/* Icon Container with active highlight pill and terracotta indicator dot */}
              <div
                className={cn(
                  'relative flex items-center justify-center rounded-full px-3 py-1 transition-all duration-200',
                  active
                    ? 'bg-brand-cream border border-brand-border/70 text-brand-forest shadow-2xs dark:border-border dark:bg-muted dark:text-foreground'
                    : 'text-brand-muted group-hover:text-brand-charcoal dark:text-muted-foreground',
                )}
              >
                <Icon
                  className={cn(
                    'h-4 w-4 transition-transform duration-150 group-active:scale-90',
                    active
                      ? 'text-brand-terracotta'
                      : 'text-brand-muted group-hover:text-brand-charcoal dark:text-muted-foreground',
                  )}
                  aria-hidden="true"
                />

                {/* Subtle active status indicator dot */}
                {active && (
                  <span
                    className="absolute -right-0.5 top-0.5 h-1.5 w-1.5 rounded-full bg-brand-terracotta ring-2 ring-white dark:ring-background"
                    aria-hidden="true"
                  />
                )}
              </div>

              {/* Label */}
              <span
                className={cn(
                  'text-[10px] leading-none tracking-tight transition-colors',
                  active
                    ? 'font-semibold text-brand-forest dark:text-foreground'
                    : 'font-medium text-brand-muted group-hover:text-brand-charcoal dark:text-muted-foreground',
                )}
              >
                {item.label}
              </span>
            </Link>
          );
        })}
      </nav>
    </div>
  );
}
