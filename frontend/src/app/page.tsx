export default function Home() {
  return (
    <main className="min-h-screen bg-brand-cream p-10">
      <div className="mx-auto max-w-3xl rounded-2xl bg-white p-8 shadow-sm">
        <span className="inline-block rounded-full bg-brand-forest-light px-4 py-2 text-sm text-white">
          ARXOR
        </span>

        <h1 className="mt-6 text-4xl font-bold text-brand-forest">
          Discover Sri Lanka differently.
        </h1>

        <p className="mt-4 text-brand-muted">
          Your ARXOR platform is ready.
        </p>

        <button className="mt-6 rounded-xl bg-brand-terracotta px-6 py-3 font-semibold text-white transition hover:bg-brand-terracotta-dark">
          Get Started
        </button>
      </div>
    </main>
  );
}