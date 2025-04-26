const CACHE_NAME = 'qr-code-generator-v3';
const urlsToCache = [
    '/',
    'https://cdn.tailwindcss.com'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(urlsToCache))
    );
});

self.addEventListener('fetch', event => {
    if (event.request.method === 'POST') {
        event.respondWith(fetch(event.request));
        return;
    }
    event.respondWith(
        caches.match(event.request)
            .then(response => response || fetch(event.request))
    );
});