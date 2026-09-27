import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Compass, MapPin, Sparkles, ArrowRight } from 'lucide-react';

export default function Home() {
  return (
    <div className="mx-auto max-w-5xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
      {/* Hero preview showcasing responsive shell and ARXOR brand identity */}
      <section className="relative overflow-hidden rounded-3xl border border-brand-border bg-gradient-to-b from-brand-cream/80 to-background p-6 shadow-xs sm:p-10">
        <div className="flex flex-wrap items-center gap-2">
          <Badge
            variant="outline"
            className="rounded-full border-brand-forest/20 bg-brand-forest/10 font-medium text-brand-forest"
          >
            <Sparkles className="mr-1 h-3 w-3 text-brand-terracotta" />
            Step 8 Complete
          </Badge>
          <Badge
            variant="outline"
            className="rounded-full border-brand-border bg-white/80 text-brand-muted"
          >
            Base Layout Shell Active
          </Badge>
        </div>

        <div className="mt-6 max-w-2xl">
          <h1 className="text-3xl font-extrabold tracking-tight text-brand-forest sm:text-4xl md:text-5xl">
            Discover Sri Lanka{' '}
            <span className="text-brand-terracotta">differently.</span>
          </h1>
          <p className="mt-4 text-base text-brand-muted sm:text-lg">
            ARXOR spatial exploration platform. The responsive base shell is now
            ready with desktop navigation and mobile bottom dock.
          </p>
        </div>

        <div className="mt-8 flex flex-wrap items-center gap-3">
          <Button className="rounded-full bg-brand-terracotta px-5 font-medium text-white shadow-xs hover:bg-brand-terracotta-dark">
            ARXOR IS ALIVE 🔥
          </Button>
          <Link href="/map">
            <Button
              variant="outline"
              className="rounded-full border-brand-border bg-white hover:bg-muted text-brand-charcoal"
            >
              <MapPin className="mr-1.5 h-4 w-4 text-brand-forest" />
              View Spatial Map
              <ArrowRight className="ml-1.5 h-3.5 w-3.5 text-brand-muted" />
            </Button>
          </Link>
        </div>

        {/* Feature Highlights Grid */}
        <div className="mt-12 grid grid-cols-1 gap-4 sm:grid-cols-3">
          <div className="rounded-2xl border border-brand-border/70 bg-white/70 p-5 shadow-2xs backdrop-blur-xs">
            <div className="flex h-9 w-9 items-center justify-center rounded-xl border border-brand-border/70 bg-brand-cream text-brand-forest">
              <Compass className="h-4.5 w-4.5 text-brand-terracotta" />
            </div>
            <h2 className="mt-3.5 text-sm font-semibold text-brand-charcoal">
              Desktop Navbar
            </h2>
            <p className="mt-1 text-xs leading-relaxed text-brand-muted">
              Floating capsule navigation, official ARXOR logo, and quick actions.
            </p>
          </div>

          <div className="rounded-2xl border border-brand-border/70 bg-white/70 p-5 shadow-2xs backdrop-blur-xs">
            <div className="flex h-9 w-9 items-center justify-center rounded-xl border border-brand-border/70 bg-brand-cream text-brand-forest">
              <MapPin className="h-4.5 w-4.5 text-brand-forest" />
            </div>
            <h2 className="mt-3.5 text-sm font-semibold text-brand-charcoal">
              Mobile Dock
            </h2>
            <p className="mt-1 text-xs leading-relaxed text-brand-muted">
              Fixed bottom dock with 5 touch-friendly items and safe-area margins.
            </p>
          </div>

          <div className="rounded-2xl border border-brand-border/70 bg-white/70 p-5 shadow-2xs backdrop-blur-xs">
            <div className="flex h-9 w-9 items-center justify-center rounded-xl border border-brand-border/70 bg-brand-cream text-brand-forest">
              <Sparkles className="h-4.5 w-4.5 text-brand-gold" />
            </div>
            <h2 className="mt-3.5 text-sm font-semibold text-brand-charcoal">
              Safe Spacing
            </h2>
            <p className="mt-1 text-xs leading-relaxed text-brand-muted">
              Page content is cushioned to ensure it never hides behind either bar.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}