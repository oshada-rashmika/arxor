import type { LucideIcon } from 'lucide-react';
import { Compass, Map, Bookmark, Route, User } from 'lucide-react';

export interface NavItem {
  label: string;
  href: string;
  icon: LucideIcon;
  description?: string;
}

export const NAV_ITEMS: readonly NavItem[] = [
  {
    label: 'Explore',
    href: '/',
    icon: Compass,
    description: 'Discover places & cultural stories',
  },
  {
    label: 'Map',
    href: '/map',
    icon: Map,
    description: 'Spatial and interactive map',
  },
  {
    label: 'Saved',
    href: '/saved',
    icon: Bookmark,
    description: 'Saved places & routes',
  },
  {
    label: 'Trips',
    href: '/trips',
    icon: Route,
    description: 'Curated itineraries & journeys',
  },
  {
    label: 'Profile',
    href: '/profile',
    icon: User,
    description: 'Account settings & history',
  },
] as const;

/**
 * Helper to determine if a navigation item is currently active.
 * Accurately handles the root path '/' vs nested paths.
 */
export function isNavItemActive(pathname: string, itemHref: string): boolean {
  if (itemHref === '/') {
    return pathname === '/';
  }
  return pathname === itemHref || pathname.startsWith(`${itemHref}/`);
}
