'use client';

import type { ReactNode } from 'react';
import { cn } from '@/lib/utils';
import { Navbar } from './navbar';
import { MobileDock } from './mobile-dock';
import type { NavItem } from './nav-config';

export interface AppShellProps {
  children: ReactNode;
  navItems?: readonly NavItem[];
  className?: string;
  mainClassName?: string;
  hideNavbar?: boolean;
  hideMobileDock?: boolean;
}

export function AppShell({
  children,
  navItems,
  className,
  mainClassName,
  hideNavbar = false,
  hideMobileDock = false,
}: AppShellProps) {
  return (
    <div
      className={cn(
        'relative flex min-h-screen flex-col bg-background text-foreground selection:bg-brand-forest/20 selection:text-brand-forest',
        className,
      )}
    >
      {/* Fixed/Sticky Top Navbar */}
      {!hideNavbar && <Navbar items={navItems} />}

      {/* Main Content Area: non-overlapping spacing for both desktop and mobile docks */}
      <main
        id="main-content"
        tabIndex={-1}
        className={cn(
          'flex-1 w-full',
          // Mobile: comfortable padding so fixed bottom dock never covers content
          'pb-[calc(5rem+env(safe-area-inset-bottom,0px))]',
          // Desktop / Tablet: standard clean bottom padding
          'md:pb-10',
          'focus:outline-none',
          mainClassName,
        )}
      >
        {children}
      </main>

      {/* Mobile Fixed Bottom Navigation Dock */}
      {!hideMobileDock && <MobileDock items={navItems} />}
    </div>
  );
}
