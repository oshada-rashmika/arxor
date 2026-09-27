'use client';

import Link from 'next/link';
import Image from 'next/image';
import { usePathname } from 'next/navigation';
import { Compass, Search } from 'lucide-react';
import { cn } from '@/lib/utils';
import { NAV_ITEMS, type NavItem, isNavItemActive } from './nav-config';
import { Button } from '@/components/ui/button';

export interface NavbarProps {
  items?: readonly NavItem[];
  className?: string;
}

export function Navbar({ items = NAV_ITEMS, className }: NavbarProps) {
  const pathname = usePathname();

  return (
    <header
      className={cn(
        'sticky top-0 z-40 w-full border-b border-brand-border/60 bg-white/80 backdrop-blur-xl backdrop-saturate-150 transition-colors dark:border-border/60 dark:bg-background/80',
        className,
      )}
    >
      {/* Accessible skip link */}
      <a
        href="#main-content"
        className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-3 focus:z-50 focus:rounded-md focus:bg-brand-forest focus:px-4 focus:py-2 focus:text-white focus:shadow-md focus:outline-none focus:ring-2 focus:ring-ring"
      >
        Skip to main content
      </a>

      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        {/* ARXOR Official Brand Logo */}
        <Link
          href="/"
          className="group flex items-center rounded-lg focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-forest/20"
          aria-label="ARXOR - Return to homepage"
        >
          <Image
            src="/logo.png"
            alt="ARXOR"
            width={144}
            height={32}
            priority
            className="h-8 w-auto object-contain transition-transform duration-200 group-hover:scale-[1.02]"
          />
        </Link>

        {/* Center Navigation Capsule (Desktop / Tablet) */}
        <nav
          aria-label="Desktop Primary Navigation"
          className="hidden md:flex items-center rounded-full border border-brand-border/70 bg-brand-cream/60 p-1 shadow-2xs backdrop-blur-sm dark:border-border/60 dark:bg-card/50"
        >
          <ul className="flex items-center gap-0.5" role="list">
            {items.map((item) => {
              const active = isNavItemActive(pathname, item.href);
              const Icon = item.icon;

              return (
                <li key={item.href}>
                  <Link
                    href={item.href}
                    aria-current={active ? 'page' : undefined}
                    className={cn(
                      'group relative flex items-center gap-1.5 rounded-full px-3.5 py-1.5 text-xs transition-all duration-200',
                      'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-forest/20',
                      active
                        ? 'bg-white font-semibold text-brand-forest shadow-xs border border-brand-border/60 dark:border-border dark:bg-muted dark:text-foreground'
                        : 'font-medium text-brand-muted hover:text-brand-charcoal hover:bg-white/60 dark:text-muted-foreground dark:hover:text-foreground dark:hover:bg-muted/40',
                    )}
                  >
                    <Icon
                      className={cn(
                        'h-3.5 w-3.5 transition-colors',
                        active
                          ? 'text-brand-terracotta'
                          : 'text-brand-muted/70 group-hover:text-brand-charcoal dark:text-muted-foreground',
                      )}
                      aria-hidden="true"
                    />
                    <span>{item.label}</span>

                    {/* Subtle active indicator dot */}
                    {active && (
                      <span
                        className="h-1 w-1 rounded-full bg-brand-terracotta"
                        aria-hidden="true"
                      />
                    )}
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>

        {/* Right-side Actions & Quick Triggers */}
        <div className="flex items-center gap-2.5">
          {/* Minimalist Search Capsule */}
          <button
            type="button"
            aria-label="Search places and routes"
            className="group flex items-center gap-2 rounded-full border border-brand-border/70 bg-brand-cream/50 px-3.5 py-1.5 text-xs text-brand-muted transition-all hover:border-brand-terracotta/40 hover:bg-white hover:text-brand-charcoal focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-forest/20 dark:border-border/60 dark:bg-card/40 dark:text-muted-foreground dark:hover:bg-card"
          >
            <Search
              className="h-3.5 w-3.5 text-brand-muted transition-colors group-hover:text-brand-terracotta dark:text-muted-foreground"
              aria-hidden="true"
            />
            <span className="hidden sm:inline font-normal">Search places...</span>
            <kbd className="hidden sm:inline-flex items-center rounded border border-brand-border bg-white px-1.5 py-0.2 font-mono text-[9px] text-brand-muted shadow-2xs dark:border-border dark:bg-muted">
              ⌘K
            </kbd>
          </button>

          {/* Action CTA Button */}
          <Link href="/map" className="hidden sm:inline-flex">
            <Button
              size="sm"
              className="rounded-full bg-brand-forest px-4 text-xs font-medium text-white shadow-xs transition-all hover:bg-brand-forest-light focus-visible:ring-brand-forest/20"
            >
              <Compass
                className="mr-1.5 h-3.5 w-3.5 text-brand-terracotta"
                aria-hidden="true"
              />
              <span>Open Map</span>
            </Button>
          </Link>
        </div>
      </div>
    </header>
  );
}
